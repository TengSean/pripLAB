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
%%time
allKeys = plt.rcParams.keys()
for key in allKeys:
    if 'text' in key:
        print( key)
#%%
print(plt.style.available)

#%%
