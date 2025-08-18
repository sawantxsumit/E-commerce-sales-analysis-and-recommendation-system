
# 🛍️ E-Commerce Customer Segmentation

This project performs **customer segmentation** for an e-commerce platform using **Machine Learning (KMeans clustering)**.  
It helps in identifying customer groups for **targeted marketing, personalization, and business insights**.

---

🚀 **Live App**: [Click Here to Try](https://e-commerce-sales-analysis-and-recommendation-system-icql6evf3a.streamlit.app/)  

---

## 📌 Features  
- 🔍 **Customer Lookup** – Enter a valid customer ID to view details.  
- 📊 **Sales Analysis** – Visualizations of customer clusters and purchasing behavior.  
- 🎯 **Recommendation System** – Suggests top products based on clustering.  
- ⚡ **Interactive Dashboard** – Built with [Streamlit](https://streamlit.io/) for simplicity and speed.  

---

## 🛠️ Tech Stack  
- **Python 3.12**  
- **Pandas** – Data handling & preprocessing  
- **Scikit-learn** – Machine learning & clustering  
- **Matplotlib / Seaborn** – Visualizations  
- **Streamlit** – Interactive web app deployment  

---

## 📂 Project Structure  
├── data/
│ ├── raw/ # Original datasets
│ ├── processed/ # Cleaned datasets (used for modeling)
├── notebooks/
│ ├── 1_data_cleaning.ipynb
│ ├── 2_feature_engineering.ipynb
│ ├── 3_model_training.ipynb
├── app.py # Streamlit app for deployment
├── requirements.txt # Dependencies
└── README.md



---

## ⚙️ Workflow

1. **Data Cleaning** – Handle missing values, convert datatypes.  
2. **Feature Engineering** – Extract features like favorite shopping day, country, etc.  
3. **Data Scaling** – Normalize numerical features using `StandardScaler`.  
4. **Dimensionality Reduction (PCA)** – Reduce feature space for better clustering.  
5. **Clustering (KMeans)** – Segment customers into groups.  
6. **Deployment** – Streamlit app for interactive visualization and prediction.

---
## ⚙️ Installation & Usage  
Clone the repository and run the app locally:  

```bash
# Clone repo
git clone https://github.com/your-username/your-repo-link.git
cd your-repo-link

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py

👨‍💻 Author

Developed by Sumit sawant 👋

Linked in: www.linkedin.com/in/sumit-sawant-249370354
