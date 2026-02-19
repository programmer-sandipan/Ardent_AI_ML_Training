# 🏠 House Price Prediction — Linear Regression

A machine learning project that predicts California house prices using Linear Regression, built with Python and scikit-learn.

---

## 📌 Project Overview

This project trains a supervised regression model on the *California Housing Dataset* (built into scikit-learn) to predict median house values based on demographic and geographic features. The workflow covers everything from data loading and EDA to model training, evaluation, feature importance analysis, and a log-transform improvement experiment.

---

## 🎯 Objective

> Train a Linear Regression model that accurately predicts house prices based on features such as income, house age, number of rooms, population, and location.

---

## 📂 Repository Structure


├── Project_2.ipynb               # Main Jupyter Notebook
├── house_price_prediction.csv    # Saved prediction results (Actual vs Predicted)
└── README.md


---

## 📊 Dataset

| Property | Details |
|---|---|
| *Source* | sklearn.datasets.fetch_california_housing |
| *Samples* | 20,640 |
| *Features* | 8 |
| *Target* | Median house value (in $100,000s) |

*Features:*

| Feature | Description |
|---|---|
| MedInc | Median income in block group |
| HouseAge | Median house age in block group |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms per household |
| Population | Block group population |
| AveOccup | Average number of household members |
| Latitude | Block group latitude |
| Longitude | Block group longitude |

---

## 🔧 Tech Stack

- *Language:* Python 3
- *Environment:* Google Colab
- *Libraries:*
  - NumPy — numerical operations
  - Pandas — data manipulation
  - Matplotlib — data visualization
  - Scikit-learn — model training & evaluation

---

## 🧪 Project Workflow

The notebook follows a structured 14-step pipeline:

1. *Import Libraries*
2. *Load Dataset* from scikit-learn (no download required)
3. *Exploratory Data Analysis* — df.head(), df.describe()
4. *Check Missing Values*
5. *Data Visualization* — distributions, correlations
6. *Feature & Target Split* — X and y
7. *Train/Test Split* — 80/20 with random_state=42
8. *Train Linear Regression Model*
9. *Make Predictions*
10. *Evaluate Model* — RMSE and R² Score
11. *Visualize Results* — Actual vs Predicted plot
12. *Feature Importance* — Coefficient analysis
13. *Model Improvement* — Log transformation on target variable
14. *Save Results* — Export predictions to CSV

---

## 📈 Model Performance

| Metric | Baseline Model | After Log Transform |
|---|---|---|
| *RMSE* | — | 0.2244 |
| *R² Score* | — | 0.6006 |

> Log-transforming the target variable (np.log1p(y)) was applied as a feature engineering technique to reduce skewness and improve model fit.

---

## 🔍 Key Insights

- *MedInc (Median Income)* had the highest positive coefficient (~0.78), making it the strongest predictor of house price.
- *AveBedrms* showed a notable positive influence (~0.78), while *AveRooms* had a slight negative coefficient.
- Geographic features (Latitude, Longitude) contributed meaningfully, reflecting California's coastal price premiums.

---

## 🚀 Getting Started

### Run Locally

bash
# Clone the repository
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction

# Install dependencies
pip install numpy pandas matplotlib scikit-learn jupyter

# Launch the notebook
jupyter notebook Project_2.ipynb


### Run on Google Colab

Click the badge below to open directly in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

> No dataset download needed — the California Housing dataset loads automatically via sklearn.datasets.

---

## 📋 Requirements


numpy
pandas
matplotlib
scikit-learn


---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ using Python & scikit-learn
