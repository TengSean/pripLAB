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
plt.rcParams["figure.figsize"] = (80,80)
sns.set(style='whitegrid')
# sns.reset_orig()
sns.pairplot(df, hue="Class label", size=2.5)
plt.tight_layout()

# print(os.getcwd())
if not os.path.exists(imgPath):
    os.makedirs(imgPath)
# plt.savefig(os.path.join(imgPath, "fig-wine-scatter.png"), dpi=300)
plt.show()
#%%
import numpy as np
from sklearn.preprocessing import StandardScaler
plt.rcParams["figure.figsize"] = (18,18)
plt.rcParams["xtick.labelsize"]=20
plt.rcParams["ytick.labelsize"]=20
#Z-normalize data
sc = StandardScaler()
Z = sc.fit_transform(x)
#Estimate the correlation matrix
R = np.dot(Z.T, Z) / df.shape[0]


ticklabels = [ s for s in x.columns ]

hm = sns.heatmap(R,
                cbar = True,
                square = True,
                yticklabels = ticklabels,
                xticklabels = ticklabels)

plt.tight_layout()
# plt.savefig(os.path.join(imgPath, "fit-wine-corr.png"), dpi=300)
plt.show()


#%%
def xticklabels_example():
    fig = plt.figure() 

    x = np.arange(20)
    y1 = np.cos(x)
    y2 = (x**2)
    y3 = (x**3)
    yn = (y1,y2,y3)
    COLORS = ('b','g','k')

    for i,y in enumerate(yn):
        ax = fig.add_subplot(len(yn),1,i+1)

        ax.plot(x, y, ls='solid', color=COLORS[i]) 

        if i != len(yn) - 1:
            # all but last 
            ax.set_xticklabels( () )
        else:
            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(20) 
                # specify integer or one of preset strings, e.g.
                #tick.label.set_fontsize('x-small') 
                tick.label.set_rotation('vertical')

    fig.suptitle('Matplotlib xticklabels Example')
    plt.show()

if __name__ == '__main__':
    xticklabels_example()
#%%
