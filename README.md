# 🚢 Project 1: Exploratory Data Analysis (EDA) — Titanic Dataset

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?logo=googlecolab&logoColor=white)

---

## 📌 Overview

This project performs *Exploratory Data Analysis (EDA)* on the classic *Titanic dataset* to uncover patterns and insights about passenger survival. It also serves as a hands-on introduction to core Python programming concepts and data visualization techniques.

---

## 🎯 Objectives

- Load and inspect a real-world dataset using *Pandas*
- Understand the structure, data types, and statistical properties of the data
- Detect and handle *missing values*
- Perform basic *survival analysis* across different passenger groups
- Create meaningful *visualizations* using Matplotlib
- Practice core Python fundamentals alongside data science workflows

---

## 📂 Dataset

| Property | Details |
|---|---|
| *Name* | Titanic Passenger Dataset |
| *Source* | [datasciencedojo/datasets](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv) |
| *Rows* | 891 |
| *Columns* | 12 |

### Key Features

| Column | Description |
|---|---|
| Survived | Survival status (0 = No, 1 = Yes) |
| Pclass | Passenger class (1st, 2nd, 3rd) |
| Sex | Gender of the passenger |
| Age | Age in years |
| SibSp | Number of siblings/spouses aboard |
| Parch | Number of parents/children aboard |
| Fare | Ticket fare paid |
| Embarked | Port of embarkation (C, Q, S) |

---

## 🛠️ Tech Stack

- *Python 3.x*
- *Pandas* — data loading, manipulation, and analysis
- *Matplotlib* — data visualization and plotting
- *NumPy* — numerical operations
- *Google Colab* — development environment

---

## 📋 Project Workflow

### Step 1 — Import Libraries
Import pandas, matplotlib, numpy, and other required libraries.

### Step 2 — Load Dataset
Read the Titanic CSV directly from a public GitHub URL using pd.read_csv().

### Step 3 — Understand the Data
- Inspect shape, column names, and data types with df.info()
- Generate descriptive statistics using df.describe()
- Preview the first few rows with df.head()

### Step 4 — Handle Missing Values
Identified missing data in three columns:

| Column | Missing Values | Strategy |
|---|---|---|
| Age | 177 | Filled with mean age |
| Cabin | 687 | Left as-is (too many missing) |
| Embarked | 2 | Filled with mode |

### Step 5 — Simple Analysis
- Counted survival distribution: *549 did not survive, **342 survived*
- Analyzed survival rates by gender and passenger class

### Step 6 — Visualizations
Created charts including:
- Bar charts for survival counts
- Line plots for pulse vs. calorie burnage (Sports Watch dataset demo)
- Additional plots demonstrating Matplotlib's flexibility

---

## 🔍 Key Findings

- The overall survival rate was approximately *38.4%*
- Significant disparities existed in survival rates across *passenger class* and *gender*
- The Cabin column had over *77% missing data*, making it unsuitable for direct analysis
- Age had ~20% missing values, imputed using the mean (~29.7 years)

---

## 🐍 Python Concepts Practiced

This notebook also covers Python fundamentals as part of the learning journey:

- *Built-in modules*: math, datetime
- *Control flow*: for loops, while loops, nested loops
- *String methods*: .upper(), .lower(), .index()
- *User-defined functions*: defining, calling, parameters vs. arguments

---

## 🚀 Getting Started

### Prerequisites

bash
pip install pandas matplotlib numpy


### Run the Notebook

1. Clone this repository:
   bash
   git clone https://github.com/your-username/your-repo-name.git
   
2. Open the notebook in Google Colab or Jupyter:
   bash
   jupyter notebook "Project_1__EDA_.ipynb"
   
3. Run all cells from top to bottom.

> *Note:* The dataset is loaded directly from a public URL — no manual download required.

---

## 📁 Repository Structure


📦 your-repo-name
 ┣ 📓 Project_1__EDA_.ipynb   # Main notebook
 ┗ 📄 README.md               # Project documentation


---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤Author

*Your Name*
- GitHub: [@sandipanmaity102-pixel](https://github.com/sandipanmaity102-pixel)
- LinkedIn: [Sandipan Maity] (https://www.linkedin.com/in/sandipan-maity-35447839a?utm_source=share_via&utm_content=profile&utm_medium=member_android)
