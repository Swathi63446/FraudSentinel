from flask import Flask, request, render_template, jsonify
from datetime import datetime
import pandas
import pickle
import os
import numpy
from sklearn.preprocessing import LabelEncoder

model_path = 'saved_models/model.pkl'
model = pickle.load(open(model_path, 'rb'))

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predictRouteClient():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.lower().endswith('.csv'):
            return jsonify({'error': 'Please upload a CSV file'}), 400
        
        # Read the uploaded CSV file
        data = pandas.read_csv(file)
        
        # Check if required columns exist
        required_columns = ['step', 'trans_type', 'amount', 'nameOrig', 'oldbalanceOrg', 
                           'nameDest', 'oldbalanceDest', 'accountType']
        
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            return jsonify({
                'error': f'Missing required columns: {", ".join(missing_columns)}',
                'expected_columns': required_columns
            }), 400
        
        # Add segment column (required by the model)
        data['segment'] = 0  # Default segment value
        
        # Store original data for display
        original_data = data.copy()
        
        # Preprocess the data (encode categorical features)
        # Reorder columns to match model training order: segment, step, trans_type, amount, nameOrig, oldbalanceOrg, nameDest, oldbalanceDest, accountType
        model_columns = ['segment', 'step', 'trans_type', 'amount', 'nameOrig', 'oldbalanceOrg', 'nameDest', 'oldbalanceDest', 'accountType']
        data_processed = data[model_columns].copy()
        
        # Identify categorical features
        categorical_features = ['trans_type', 'nameOrig', 'nameDest']
        
        # Encode categorical features
        for feature in categorical_features:
            if feature in data_processed.columns:
                le = LabelEncoder()
                data_processed[feature] = le.fit_transform(data_processed[feature].astype(str))
        
        # Get prediction probabilities
        y_proba = model.predict_proba(data_processed)
        
        # Use a lower threshold for fraud detection (default is 0.5)
        fraud_threshold = 0.1  # Lower threshold to catch more potential fraud
        y_pred = (y_proba[:, 1] > fraud_threshold).astype(int)
        original_data['isFraud'] = y_pred
        
        # Calculate statistics
        total_transactions = len(original_data)
        fraud_count = sum(y_pred)
        fraud_percentage = (fraud_count / total_transactions) * 100 if total_transactions > 0 else 0
        
        # Prepare results for display
        results = {
            'total_transactions': int(total_transactions),
            'fraud_count': int(fraud_count),
            'fraud_percentage': round(fraud_percentage, 2),
            'legitimate_count': int(total_transactions - fraud_count),
            'legitimate_percentage': round(100 - fraud_percentage, 2),
            'predictions': original_data[['step', 'trans_type', 'amount', 'nameOrig', 'nameDest', 'isFraud']].to_dict('records')
        }
        
        return jsonify({
            'success': True,
            'message': 'Analysis completed successfully',
            'results': results
        })
        
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500
    

if __name__ == "__main__":
    app.run()