import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import skew

df = pd.read_csv("train.csv")
dft = pd.read_csv("test.csv")

lotshape_fin_map = {
    'IR3' : 0,
    'IR2' : 1,
    'IR1' : 2,
    'Reg' : 3
}
df['LotShape'] = df['LotShape'].map(lotshape_fin_map)
dft['LotShape'] = dft['LotShape'].map(lotshape_fin_map)

utilities_map = {
    'AllPub': 3,
    'NoSewr': 2,
    'NoSeWa': 1,
    'ELO': 0
}
df['Utilities'] = df['Utilities'].map(utilities_map)
dft['Utilities'] = dft['Utilities'].map(utilities_map)

landslope_fin_map = {
    'Gtl' : 2,
    'Mod' : 1,
    'Sev' : 0
}
df['LandSlope'] = df['LandSlope'].map(landslope_fin_map)
dft['LandSlope'] = dft['LandSlope'].map(landslope_fin_map)

qual_cond_map = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1,
    'NA': 0 
}
qual_cond_cols = [
    'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'HeatingQC', 
    'KitchenQual', 'FireplaceQu', 'GarageQual', 'GarageCond', 'PoolQC'
]
for col in qual_cond_cols:
    df[col] = df[col].fillna("NA")
    dft[col] = dft[col].fillna("NA")
for col in qual_cond_cols:
    df[col] = df[col].map(qual_cond_map)
    dft[col] = dft[col].map(qual_cond_map)

bsmt_exp_map = {
    'Gd': 4,
    'Av': 3,
    'Mn': 2,
    'No': 1,
    'None': 0
}
df['BsmtExposure'] = df['BsmtExposure'].map(bsmt_exp_map)
dft['BsmtExposure'] = dft['BsmtExposure'].map(bsmt_exp_map)

bsmt_fin_map = {
    'GLQ': 6,
    'ALQ': 5,
    'BLQ': 4,
    'Rec': 3,
    'LwQ': 2,
    'Unf': 1,
    'None': 0
}
df['BsmtFinType1'] = df['BsmtFinType1'].map(bsmt_fin_map)
dft['BsmtFinType1'] = dft['BsmtFinType1'].map(bsmt_fin_map)
df['BsmtFinType2'] = df['BsmtFinType2'].map(bsmt_fin_map)
dft['BsmtFinType2'] = dft['BsmtFinType2'].map(bsmt_fin_map)

electrical_map = {
    'FuseP': 1,   # poor
    'FuseF': 2,   # fair
    'FuseA': 3,   # average
    'Mix': 4,     # mixed
    'SBrkr': 5   # standard breakers & Romex
}
df['Electrical'] = df['Electrical'].fillna('SBrkr')
dft['Electrical'] = dft['Electrical'].fillna('SBrkr')
df['Electrical'] = df['Electrical'].map(electrical_map)
dft['Electrical'] = dft['Electrical'].map(electrical_map)

functional_map = {
    'Typ': 7,
    'Min1': 6,
    'Min2': 5,
    'Mod': 4,
    'Maj1': 3,
    'Maj2': 2,
    'Sev': 1,  
    'Sal': 0
}
df['Functional'] = df['Functional'].map(functional_map)
dft['Functional'] = dft['Functional'].map(functional_map)

garage_fin_map = {
    'Fin': 3,
    'RFn': 2,
    'Unf': 1,
    'None': 0
}
df['GarageFinish'] = df['GarageFinish'].map(garage_fin_map)
dft['GarageFinish'] = dft['GarageFinish'].map(garage_fin_map)

paveddrive_map = {
    'Y': 2,
    'P': 1,
    'N': 0
}
df['PavedDrive'] = df['PavedDrive'].map(paveddrive_map)
dft['PavedDrive'] = dft['PavedDrive'].map(paveddrive_map)

fence_map = {
    'GdPrv': 4,
    'MnPrv': 3,
    'GdWo': 2,
    'MnWw': 1,
    'NA': 0
}
df['Fence'] = df['Fence'].fillna('NA')
dft['Fence'] = dft['Fence'].fillna('NA')
df['Fence'] = df['Fence'].map(fence_map)
dft['Fence'] = dft['Fence'].map(fence_map)

alley_map = {
    'Grvl': 1,
    'Pave': 2,
    'NA': 0
}
df['Alley'] = df['Alley'].fillna('NA')
dft['Alley'] = dft['Alley'].fillna('NA')
df['Alley'] = df['Alley'].map(alley_map)
dft['Alley'] = dft['Alley'].map(alley_map)