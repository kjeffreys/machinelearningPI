import os
import tarfile
import pandas as pd
import matplotlib.pyplot as plt

HOUSING_PATH = os.path.join("D:\\", "datasets", "housing")

def fetchHousingData(housing_path=HOUSING_PATH):
    #os.makedirs(housing_path, exist_ok=True)
    #download tar file, done manually due to bad link
    tgz_path = os.path.join(housing_path, "housing.tgz")
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    
def loadHousingData(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    
    return pd.read_csv(csv_path)

def getAttributeValueCounts(df, attr='ocean_proximity'):
    return df[attr].value_counts()


if __name__ == "__main__":
    df = loadHousingData()
    print("df.head():")
    print(df.head())
    print("df.info():")
    print(df.info())
    print("df[attr].value_counts():")
    print(getAttributeValueCounts(df))
    print("describe():")
    print(df.describe())
    print("histogram with plt")
    df.hist(bins=50, figsize=(20,15))
    plt.show() # see housingHistogram.jpg
