# Question 02, Lab 09
# AB Satyaprkash, 180123062

# imports
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# functions


def plotGraphs(fileName):
    df = pd.read_csv(fileName)
    # extract and rename columns
    df = df[['Expiry', 'Strike Price', 'Close']]
    mapper = dict(
        zip(df.columns, ['Maturity', 'Strike Price', 'Option Price']))
    df = df.rename(columns=mapper)
    df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
    print(df)
    plotTitle = fileName.split('/')[-1][:-4]

    # 2D Plot of Option Price vs Maturity
    df.plot(x='Maturity', y='Option Price', kind='scatter',
            title=f'Option Price vs Maturity for {plotTitle}', rot=45, s=0.6, figsize=(8, 8), color='blue')
    plt.savefig(f'Plots/Question 2/{plotTitle}_1.png')
    plt.show()

    # 2D Plot of Option Price vs Strike Price
    df.plot(x='Strike Price', y='Option Price', kind='scatter',
            title=f'Option Price vs Strike Price for {plotTitle}', s=0.6, figsize=(8, 8), color='red')
    plt.savefig(f'Plots/Question 2/{plotTitle}_2.png')
    plt.show()

    df['Maturity'] = df['Maturity'].astype('datetime64[ns]')
    fig = plt.figure(figsize=(10, 10))
    ax = Axes3D(fig)
    ax.plot_trisurf(df['Maturity'], df['Strike Price'],
                    df['Option Price'])
    ax.set_title(f'3D Plot for {plotTitle}')
    ax.set_xlabel('Maturity in Nanoseconds')
    ax.set_ylabel('Strike Price')
    ax.set_zlabel('Option Price')
    plt.savefig(f'Plots/Question 2/{plotTitle}_3.png')
    plt.show()

# program body


fileNameArray = ['Stock Options/Index/INDEX_CE.csv', 'Stock Options/Index/INDEX_PE.csv', 'Stock Options/GAIL/GAIL_CE.csv', 'Stock Options/GAIL/GAIL_PE.csv',
                 'Stock Options/IOC/IOC_CE.csv', 'Stock Options/IOC/IOC_PE.csv', 'Stock Options/ONGC/ONGC_CE.csv', 'Stock Options/ONGC/ONGC_PE.csv', 'Stock Options/TATAMOTORS/TATAMOTORS_CE.csv',
                 'Stock Options/TATAMOTORS/TATAMOTORS_PE.csv']

for fileName in fileNameArray:
    plotGraphs(fileName)
