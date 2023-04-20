#take dummy dataset file  from kaggle using pyspark make EDA with visualization and prediction model.
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# read data
df = pd.read_csv('/Users/komal/Desktop/titanic_train.csv')
# check shape of data
print(df.shape)
# check head of data
print(df.head())
# check info of data
print(df.info())
# check null values
print(df.isnull().sum())
# check unique values
print(df.nunique())
# check describe of data
print(df.describe())
# check correlation
# print(df.corr())
# check skewness
print(df.skew())
# check target variable
print(df['survived'].value_counts())
# check target variable
sns.countplot(df['survived'])
plt.show()
# check distribution of data
df.hist(figsize=(20, 20))
plt.show()
# check distribution of data
df.plot(kind='density', subplots=True, layout=(5, 5), sharex=False, legend=False, fontsize=1, figsize=(20, 20))
plt.show()
# check distribution of data
df.plot(kind='box', subplots=True, layout=(5, 5), sharex=False, sharey=False, fontsize=8, figsize=(20, 20))
plt.show()
# check distribution of data
sns.pairplot(df)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.2)
fig=plt.gcf()
fig.set_size_inches(20,12)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.2, linecolor='white', mask=np.zeros_like(df.corr(), dtype=np.bool), square=True)
fig=plt.gcf()
fig.set_size_inches(20,12)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.2, linecolor='white', mask=np.zeros_like(df.corr(), dtype=np.bool), square=True, annot_kws={'size':20})
fig=plt.gcf()
fig.set_size_inches(20,12)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.2, linecolor='white', mask=np.zeros_like(df.corr(), dtype=np.bool), square=True, annot_kws={'size':20}, fmt='.2f')
fig=plt.gcf()
fig.set_size_inches(20,12)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.2, linecolor='white', mask=np.zeros_like(df.corr(), dtype=np.bool), square=True, annot_kws={'size':20}, fmt='.2f', cbar=False)
fig=plt.gcf()
fig.set_size_inches(20,12)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.2, linecolor='white', mask=np.zeros_like(df.corr(), dtype=np.bool), square=True, annot_kws={'size':20}, fmt='.2f', cbar=False, vmin=-1, vmax=1)
fig=plt.gcf()
fig.set_size_inches(20,12)
plt.show()
# check distribution of data
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.2, linecolor='white', mask=np.zeros_like(df.corr(), dtype=np.bool), square=True, annot_kws={'size':20}, fmt='.2f', cbar=False, vmin=-1, vmax=1, center=0)
fig=plt.gcf()
fig.set_size_inches(20,12)
