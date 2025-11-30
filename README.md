California Housing Median Value Prediction (Normal Equation)
This project implements Multiple Linear Regression from scratch using the Normal Equation, without using scikit-learn. I practiced NumPy, Pandas, dataset cleaning, missing value handling, train–test split, matrix math, and creating visualizations.

Project Structure
ML-project1/
│
├── PRACTICE/
│   ├── numpy_prac_1.py
│   ├── prac_pandaas.py
│   ├── linear_regression_prac.py
│   └── normal_equation_prac.py
│
├── PROJECT/
│   └── California_housing_median.py   ← (Main project script)
│
└── README.md
What this project does
Loads and explores the California Housing dataset
Handles missing values using median imputation
Performs 80:20 random train–test split (without sklearn)
Implements Multiple Linear Regression using the Normal Equation
Calculates Train MSE, Test MSE, and R² Score
Visualizes Median Income vs Median House Value
📊 Results
Train MSE: 0.52359
Test MSE: 0.529377
Test R² Score: 0.614
These values show that the model explains ~61% of the variance in house prices using the selected features.

Plot Interpretation
Median Income vs Median House Value
The scatter plot shows that:

As median income increases, median house value increases too.
The relationship is positively correlated but not perfectly linear.
There is a capped/saturation effect where values hit the upper limit.
This confirms that income is one of the strongest predictors of house price.

▶ How to Run
python -m venv .venv
source .venv/bin/activate       # On Windows → .venv\Scripts\activate
pip install numpy pandas matplotlib
python PROJECT/California_housing_median.py
Learnings
Practiced NumPy operations & Pandas basics
Data cleaning & handling missing values
Implemented normal equation manually
Built multiple linear regression without sklearn
Created visualization using matplotlib
Understood matrix multiplication & evaluation metrics
Notes
No ML libraries like sklearn were used
Only NumPy + Pandas + Matplotlib
This is my first end-to-end ML project
