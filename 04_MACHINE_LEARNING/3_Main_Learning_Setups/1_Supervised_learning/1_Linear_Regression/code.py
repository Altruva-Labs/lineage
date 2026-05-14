"""Chapter 4.3.1: Linear Regression as a Learning Setup.

This file demonstrates linear regression in a practical learning setup:
- How to prepare data
- How to train and evaluate the model
- How to make predictions on new data

We'll use the **California housing dataset** (a classic for regression) loaded via `sklearn.datasets`.
"""

# IMPORT MODULES

# data manipulation
import pandas as pd
import numpy as np
# visualization
import matplotlib.pyplot as plt
import seaborn as sns

# preprocessing and modeling
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# dataset
from sklearn.datasets import fetch_california_housing

# load datset
df = fetch_california_housing()


# check dataset
df
# print(df.data)
# print(df.feature_names)
# print(df.target_names)

# split and convert data to a pd dataframe
X = pd.DataFrame(df.data, columns=df.feature_names)
y = pd.Series(df.target, name="MedHouseVal")

# check X and y
print(X.info())
print(y.info())

# print(X.shape)
# print(y.shape)

# check data

## info
print("INFO:")
print(X.info())

## null values
print("\nNULL Values:")
print(X.isnull().sum())
print(X.isnull().sum().sum())


## duplicates
print("\nDUPLICATE Values:")
print(X.duplicated().sum().sum())
print(X.duplicated().sum())

## columns
print("Columns:")
print(X.columns)

# Split data into tran and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

print(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")


