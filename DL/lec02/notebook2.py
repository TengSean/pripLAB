# %%
import pandas as pd

df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
    , header = None)
df.columns = [
    'Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash',
    'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols',
    'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
    'Proline'
]
x = df.drop('Class label', 1)
y = df['Class label']
df.head(5)

#%%
%time
import os
import matplotlib.pyplot as plt
import seaborn as sns

imgPath = 'c:\\Users\\prip\\Documents\\Sean\\vscode\\python\\NTHU\\DL\\output'
COLOR = 'white'

# plt.rcParams['axes.labelcolor'] = COLOR
# plt.rcParams['xtick.color'] = COLOR
# plt.rcParams['ytick.color'] = COLOR
sns.set(style='whitegrid')
# sns.reset_orig()
sns.pairplot(df, hue="Class label", size=2.5)
# plt.tight_layout()
plt.rcParams['text.color'] = COLOR
# print(os.getcwd())
if not os.path.exists(imgPath):
    os.makedirs(imgPath)
plt.savefig(os.path.join(imgPath, "fig-wine-scatter.png"), dpi=300)
plt.show()
#%%
import numpy as np
from sklearn.preprocessing import StandardScaler

#Z-normalize data
sc = StandardScaler()
Z = sc.fit_transform(x)
#Estimate the correlation matrix
R = np.dot(Z.T, Z) / df.shape[0]

sns.set(font_scale = 1.0)

ticklabels = [ s for s in x.columns ]

hm = sns.heatmap(R,
                cbar = True,
                square = True,
                yticklabels = ticklabels,
                xticklabels = ticklabels)

plt.tight_layout()
plt.savefig(os.path.join(imgPath, "fit-wine-corr.png"), dpi=300)
plt.show()

sns.reset_orig()
#%%

#%%
