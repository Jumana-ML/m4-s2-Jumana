import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = file_path = "amman_market_data.csv"
df = pd.read_csv(file_path)
df = df.copy()
print(df.head())