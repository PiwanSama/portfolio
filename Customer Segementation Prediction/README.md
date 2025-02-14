# **Customer Segmentation and Classification Using Machine Learning** 🎯

This project identifies distinct customer segments and predicts the segment for new customers using machine learning. It also includes an interactive **Flask web app** for real-time predictions.

---

## **Key Features**

### **Machine Learning Models**
- **Clustering (Unsupervised Learning)**: Group customers into distinct segments using K-Means.
- **Classification (Supervised Learning)**: Predict customer segments using models like Random Forest and Logistic Regression.
- **Model Optimization**: Feature selection, hyperparameter tuning, and debugging with learning curves.

### **Interactive Web App**
- Input customer data directly into the app.
- Get instant predictions of the customer's segment.
- Scaled inputs ensure accurate results.

### **Data Insights**
- Comprehensive exploratory data analysis (EDA) with visualizations.
- Analyze spending habits, credit limits, payment behavior, and more.

---

## **How It Works**

1. **Data Preparation**:
   - Handle missing values, outliers, and scale features.
2. **Clustering**:
   - Group customers into segments based on behavioral patterns.
3. **Labeling**:
   - Use clustering results to label the dataset for supervised learning.
4. **Classification**:
   - Train models to predict segments for new customers.
5. **Deployment**:
   - Serve predictions via a Flask-based web app.

---

## **Dataset**

The dataset contains 18 features describing customer behavior with credit cards includung:

| Feature                  | Description                              |
|--------------------------|------------------------------------------|
| `BALANCE`                | Average balance amount                  |
| `PURCHASES`              | Total purchases made                    |
| `CREDIT_LIMIT`           | Credit limit assigned                   |
| `MINIMUM_PAYMENTS`       | Minimum payments made                   |
| `PRC_FULL_PAYMENT`       | Percentage of full payments             |

---

## **Results**

### Clustering
- Identified distinct customer groups using K-Means clustering.
- Evaluated clusters with metrics like silhouette score.

### Classification
- Achieved high accuracy with Random Forest after hyperparameter tuning.
- Debugged models using learning curves to ensure no overfitting or underfitting.

---

## **Quick Start**

### Prerequisites
1. Install Python 3.x
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Run Locally
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open in your browser at `http://localhost:5000`.

---

## **Web App Preview**

### Input Page
Input customer data directly into the form.

### Results Page
View the predicted segment instantly!

---

## **Future Improvements**
1. Explore advanced clustering techniques like DBSCAN or hierarchical clustering.
2. Enhance the web application's UI/UX for better usability.
3. Incorporate additional datasets for richer insights.

---

## **License**

This project is open-source under the MIT License.
