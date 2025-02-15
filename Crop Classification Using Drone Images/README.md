# **Crop Classification Using Drone Images** 🌾📸

This project uses **drone-captured images** and **machine learning models** to classify different types of crops, vegetation, and land structures. By leveraging advanced computer vision techniques, this project aims to assist in precision agriculture and land-use monitoring.

---

## **Project Highlights**

### **Drone Image Dataset**
- High-resolution drone images sourced from Kaggle.
- Classes include:
  - 🌳 Forest
  - 🌽 Maize
  - 🍌 Banana
  - 🥬 Legumes
  - 🏗️ Structures (e.g., buildings, roads)
  - 🗺️ Other land types

### **Machine Learning Models**
- **Random Forest Classifier**: Achieved high accuracy for crop classification.
- **Convolutional Neural Networks (CNNs)**: Used for image feature extraction and classification.
- Hyperparameter tuning to optimize model performance.

### **Key Features**
1. Preprocessing drone images:
   - Resizing and normalizing images for input into models.
   - Augmenting data to improve model generalization.
2. Training machine learning models:
   - Random Forest Classifier for structured data.
   - CNNs for image-based classification.
3. Evaluation metrics:
   - Accuracy, Precision, Recall, and F1-Score for model performance.

---

## **Dataset Overview**

This project uses a Kaggle Drone Image Dataset. The dataset contains high-resolution images of various crop types and land structures.

### Training Data
| **Image Count** | **Crop Type/Label** |
|------------------|---------------------|
| 3,282            | Forest             |
| 2,562            | Structure          |
| 1,904            | Maize              |
| 4,896            | Banana             |
| 2,342            | Legumes            |

### Test Data
- Includes unlabeled drone-captured images for evaluation.

---

## **📊 Results**

### Random Forest Classifier
- **Accuracy**: ~85%
- Performed well on structured features (e.g., vegetation indices).

### CNN Model
- **Accuracy**: ~92%
- Outperformed traditional machine learning models by leveraging image patterns.

---

## **🚀 How to Run**

### Steps

You can view the full implementation on Kaggle:  
[View Kaggle Notebook](https://www.kaggle.com/code/samaliepiwan/crop-classification-using-drone-images)

---

## **Tools & Technologies**
- Python 🐍  
- TensorFlow & Keras 🤖  
- OpenCV 📷  
- Scikit-learn 📊  

---

## **Applications**
This project has real-world applications in:
1. 🌾 Precision agriculture: Monitoring crop health and type distribution.
2. 🗺️ Land-use mapping: Identifying forests, urban areas, and agricultural zones.
3. 🌍 Environmental monitoring: Tracking deforestation or urban encroachment.