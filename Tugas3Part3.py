# %%
import pandas as pd

# %%
data = pd.read_csv("students.csv")

# %%
print(data.head(10))
data.info()

print(data.isna().sum())

data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)
data['reading score'].fillna(data['reading score'].mean(), inplace=True)
data['grade'].fillna(data['grade'].median(), inplace=True)
data.info()
data['reading score'] = data['reading score'].interpolate(method='linear')
data['reading score'] = data['reading score'].bfill()
data['reading score'] = data['reading score'].ffill()
data.dropna(axis=0, inplace=True)

threshold = len(data) * 0.5
data.dropna(thresh=threshold, axis=1, inplace=True)
