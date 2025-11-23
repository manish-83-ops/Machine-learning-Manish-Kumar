import numpy as np
import pandas as pd

df = pd.read_csv("housing.csv")
print(df.info())
print(df.head())
print(df.describe())
#So we got 10 columns to work with
print(df.isnull().sum())
#total_bedrooms has 207 missing values
#Filling the missing values with median values :)
df["total_bedrooms"]=df["total_bedrooms"].fillna(df["total_bedrooms"].median())
print(df.isnull().sum())
x=df.drop(columns=["median_house_value"]) 
y=df["median_house_value"]
print(x["total_bedrooms"])
print(y)
training_size=0.8
split_size=np.random.rand(len(x))< training_size
training_x=x[split_size]
training_y=y[split_size]
test_x=x[~split_size]
test_y=y[~split_size]
print(len(training_x))
print(len(training_y))
#scaling 
mean_1=training_x.drop(columns=["ocean_proximity"]).mean(axis=0)
standard_dev=training_x.drop(columns=["ocean_proximity"]).std(axis=0)

training_x_scaled=(training_x-mean_1)/standard_dev
test_x_scaled=(test_x-mean_1)/standard_dev
print(training_x_scaled)

