# Money Laundering Detection System

A sophisticated AI-powered web application for detecting fraudulent financial transactions using machine learning algorithms. The system analyzes transaction patterns and identifies potentially suspicious activities in real-time.

## 🚀 Features

- **AI-Powered Detection**: Advanced CatBoost machine learning model for accurate fraud detection
- **Real-time Analysis**: Instant processing and results delivery
- **User-friendly Interface**: Modern, responsive web interface with drag-and-drop file upload
- **Comprehensive Reporting**: Detailed analysis results with statistics and transaction details
- **Secure Processing**: Data is processed securely and confidentially
- **Batch Processing**: Analyze multiple transactions simultaneously

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Machine Learning**: CatBoost, scikit-learn
- **Data Processing**: pandas, numpy
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Visualization**: matplotlib, plotly

## 📋 Prerequisites

- Python 3.7+ (tested with Python 3.13.3)
- pip (Python package installer)

## 🔧 Installation

1. **Clone or download the project**
   ```bash
   # If you have git installed
   git clone <repository-url>
   cd MLD
   
   # Or simply download and extract the project folder
   ```

2. **Install required packages**
   ```bash
   pip install numpy pandas scikit-learn flask catboost requests matplotlib gunicorn
   ```

   Or install from requirements.txt (note: versions may need adjustment for newer Python versions):
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **Upload and analyze data**
   - Click "Upload CSV File" or drag and drop your CSV file
   - Click "Analyze Transactions" to process the data
   - View the analysis results

## 📊 Input Data Format

The system expects CSV files with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `step` | Time step of the transaction | 1, 2, 3... |
| `trans_type` | Type of transaction | PAYMENT, TRANSFER, CASH_OUT, CASH_IN, DEBIT |
| `amount` | Transaction amount | 9839.64 |
| `nameOrig` | Name of the originator | C1231006815 |
| `oldbalanceOrg` | Initial balance of originator | 170136.0 |
| `nameDest` | Name of the destination | M1979787155 |
| `oldbalanceDest` | Initial balance of destination | 0.0 |
| `accountType` | Account type | 0 or 1 |

### Sample Data
```csv
segment,step,trans_type,amount,nameOrig,oldbalanceOrg,nameDest,oldbalanceDest,accountType
0,1,PAYMENT,9839.64,C1231006815,170136.0,M1979787155,0.0,0
0,1,PAYMENT,1864.28,C1666544295,21249.0,M2044282225,0.0,0
0,2,TRANSFER,181.0,C1305486145,181.0,C553264065,0.0,0
```

## 📈 Output Results

The system provides comprehensive analysis results including:

- **Total Transactions**: Number of transactions analyzed
- **Fraud Detection**: Count and percentage of fraudulent transactions
- **Legitimate Transactions**: Count and percentage of legitimate transactions
- **Risk Assessment**: Overall risk level based on detected patterns
- **Transaction Details**: Detailed table showing each transaction with fraud status
- **Visual Indicators**: Color-coded results for easy interpretation

## 🏗️ Project Structure

```
MLD/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # Project documentation
├── templates/
│   └── index.html                 # Web interface template
├── src/                           # Source code modules
│   ├── data_preprocessing_1.py    # Data filtering and preprocessing
│   ├── data_preprocessing_2.py    # Additional data processing
│   ├── data_preprocessing_3.py    # Final data preparation
│   ├── feature_selection.py       # Feature importance analysis
│   ├── model_creation.py          # ML model training
│   └── segmentGenerator.py        # Customer segmentation
├── saved_models/
│   └── model.pkl                  # Trained CatBoost model
├── reports/                       # Analysis reports
│   ├── feature_importances.csv    # Feature importance scores
│   ├── missing_values.csv         # Missing data analysis
│   ├── performance.json           # Model performance metrics
│   └── silhoutte_scores.csv       # Clustering analysis
└── sample_transactions.csv        # Sample data for testing
```

## 🧠 Machine Learning Model

The system uses a **CatBoost Classifier** with the following characteristics:

- **Algorithm**: Gradient boosting with categorical features support
- **Class Weights**: {0: 1, 1: 12} (handles imbalanced fraud data)
- **Features**: 8 input features including transaction type, amounts, and account details
- **Performance**: 
  - Precision: 87.5%
  - Recall: 70%
  - F1-Score: 74.9%

### Model Training Process

1. **Data Preprocessing**: Filtering and cleaning transaction data
2. **Feature Engineering**: Creating meaningful features from raw data
3. **Customer Segmentation**: K-means clustering for customer behavior analysis
4. **Feature Selection**: Random Forest-based feature importance analysis
5. **Model Training**: CatBoost classifier with optimized hyperparameters
6. **Validation**: Cross-validation and performance evaluation

## 🔍 Usage Examples

### Basic Usage
1. Prepare your transaction data in CSV format
2. Ensure all required columns are present
3. Upload the file through the web interface
4. Review the analysis results

### API Usage
The system also provides a REST API endpoint:

```bash
curl -X POST -F "file=@your_data.csv" http://localhost:5000/predict
```

## 🛡️ Security Features

- **Input Validation**: Comprehensive validation of uploaded files
- **Error Handling**: Graceful error handling and user feedback
- **Data Privacy**: No data is stored permanently on the server
- **File Type Validation**: Only CSV files are accepted

## 📊 Performance Metrics

The system tracks various performance metrics:

- **Confusion Matrix**: True/False positives and negatives
- **Precision**: Accuracy of fraud predictions
- **Recall**: Ability to detect actual fraud cases
- **F1-Score**: Harmonic mean of precision and recall

## 🚨 Troubleshooting

### Common Issues

1. **Python Version Compatibility**
   - Ensure you're using Python 3.7 or higher
   - Some packages may need version adjustments for newer Python versions

2. **Missing Dependencies**
   - Run `pip install -r requirements.txt` to install all dependencies
   - For Python 3.13+, install packages individually if version conflicts occur

3. **Model File Missing**
   - Ensure `saved_models/model.pkl` exists
   - The model file should be present for the application to work

4. **Port Already in Use**
   - If port 5000 is busy, modify `app.py` to use a different port
   - Change `app.run()` to `app.run(port=5001)` for port 5001

### Error Messages

- **"No file uploaded"**: Ensure you select a CSV file before submitting
- **"Missing required columns"**: Check that your CSV has all required columns
- **"Please upload a CSV file"**: Only CSV files are supported

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Check the troubleshooting section above
- Review the error messages for specific guidance
- Ensure all dependencies are properly installed

## 🔮 Future Enhancements

- Real-time streaming data processing
- Advanced visualization dashboards
- Multiple model ensemble methods
- API rate limiting and authentication
- Database integration for historical analysis
- Mobile-responsive improvements

---

**Note**: This system is designed for educational and research purposes. For production use in financial institutions, additional security measures and compliance requirements should be implemented.
