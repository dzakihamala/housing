import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import skew

df = pd.read_csv("train.csv")
dft = pd.read_csv("test.csv")

y_train = df['SalePrice']
train_ID = df['Id']
test_ID = dft['Id']

ntrain = df.shape[0]
ntest = dft.shape[0]

LotFrontage_median = df.groupby('Neighborhood')['LotFrontage'].median()
Exterior1st_mode = df['Exterior1st'].mode()[0]
Exterior2nd_mode = df['Exterior2nd'].mode()[0]
Functional_mode = df['Functional'].mode()[0]
MoSold_mode = df["MoSold"].mode()[0]
YrSold_mode = df["YrSold"].mode()[0]
SaleType_mode = df['SaleType'].mode()[0]
SaleCondition_mode = df['SaleCondition'].mode()[0]


df.drop(['Id', 'SalePrice'], axis=1, inplace=True)
dft.drop('Id', axis=1, inplace=True)
all_data = pd.concat((df, dft)).reset_index(drop=True)


# -----MSSubClass udah di getdummies-----

#MSZoning
all_data['MSZoning'] = all_data['MSZoning'].fillna('RL')
#selebihnya di getdummies

#---LotFrontage
#isi data yang kosong dengan median neighborhood
all_data['LotFrontage'] = all_data['LotFrontage'].fillna(all_data['Neighborhood'].map(LotFrontage_median))
#---LotFrontage

#LotArea dibiarkan apa adanya

# -----Street udah di getdummies-----

#---Alley
all_data['Alley'] = all_data['Alley'].fillna('NoAlley')
#selebihnya di getdummies
#---Alley

lotshape_fin_map = {
    'IR3' : 0,
    'IR2' : 1,
    'IR1' : 2,
    'Reg' : 3,
    'NA'  : 0
}
all_data['LotShape'] = all_data['LotShape'].map(lotshape_fin_map)

# -----LandContour udah di getdummies-----

#---Utilities
all_data.drop('Utilities', axis=1, inplace=True)
#didrop karena 99% AllPub

# -----LotConfig sudah di getdummies

#---LandSlope
landslope_fin_map = {
    'Gtl' : 2,
    'Mod' : 1,
    'Sev' : 0
}
all_data['LandSlope'] = all_data['LandSlope'].map(landslope_fin_map)

# -----Neighborhood udah di getdummies-----
# -----Condition1 udah di getdummies-----
# -----Condition2 udah di getdummies-----
# -----BldgType udah di getdummies-----
# -----HouseStyle udah di getdummies-----
# -----OverallQual dibiarkan apa adanya-----
# -----OverallCond dibiarkan apa adanya-----
# -----YearBuilt dibiarkan apa adanya-----
# -----YearRemodAdd dibiarkan apa adanya-----
# -----RoofStyle masuk ke getdummies-----
# -----RoofMatl masuk ke getdummies-----

#---Exterior1st dan 2nd
all_data['Exterior1st'] = all_data['Exterior1st'].fillna(Exterior1st_mode)
all_data['Exterior2nd'] = all_data['Exterior2nd'].fillna(Exterior2nd_mode)
#selebihnya di getdummies

#---MasVnrType
all_data['MasVnrType'] = all_data['MasVnrType'].fillna('None')
#selebihnya di getdummies

#---MasVnrArea
all_data['MasVnrArea'] = all_data['MasVnrArea'].fillna(0)
#selebihnya dibiarkan apa adanya

# -----ExterQual sudah di QC-----
# -----ExterCond sudah di QC-----
# -----Foundation di getdummies-----
# -----BsmtQual sudah di QC-----
# -----BsmtCond sudah di QC-----

#---BsmtExposure
bsmt_exp_map = {
    'Gd': 4,
    'Av': 3,
    'Mn': 2,
    'No': 1,
    'NA': 0
}
all_data['BsmtExposure'] = all_data['BsmtExposure'].fillna('NA')
all_data['BsmtExposure'] = all_data['BsmtExposure'].map(bsmt_exp_map)

#---BsmtFinSF2
all_data['BsmtFinSF2'] = all_data['BsmtFinSF2'].fillna(0)
#selebihnya dibiarkan

#---BsmtFinType1
bsmt_fin_map = {
    'GLQ': 6,
    'ALQ': 5,
    'BLQ': 4,
    'Rec': 3,
    'LwQ': 2,
    'Unf': 1,
    'NA': 0
}
all_data['BsmtFinType1'] = all_data['BsmtFinType1'].fillna('NA')
all_data['BsmtFinType1'] = all_data['BsmtFinType1'].map(bsmt_fin_map)

#---BsmtFinSF1
all_data['BsmtFinSF1'] = all_data['BsmtFinSF1'].fillna(0)
#selebihnya dibiarkan

#---BsmtFinType2
all_data['BsmtFinType2'] = all_data['BsmtFinType2'].fillna('NA')
all_data['BsmtFinType2'] = all_data['BsmtFinType2'].map(bsmt_fin_map)

#---BsmtFinSF2
all_data['BsmtFinSF1'] = all_data['BsmtFinSF1'].fillna(0)
#selebihnya dibiarkan

#---BsmtUnfSF
all_data['BsmtUnfSF'] = all_data['BsmtUnfSF'].fillna(0) 

#---TotalBsmtSF
all_data['TotalBsmtSF'] = all_data['TotalBsmtSF'].fillna(0) 

# -----Heating sudah di getdummies-----
# -----HeatingQC sudah di QC-----

#---CentralAir
all_data['CentralAir'] = all_data['CentralAir'].map({'Y': 1, 'N': 0})

electrical_map = {
    'FuseP': 1,   # poor
    'FuseF': 2,   # fair
    'FuseA': 3,   # average
    'Mix': 4,     # mixed
    'SBrkr': 5  # standard breakers & Romex
}
all_data['Electrical'] = all_data['Electrical'].fillna('SBrkr')
all_data['Electrical'] = all_data['Electrical'].map(electrical_map)

#--- 1stFlrSF dibiarkan apa adanya
#--- 2ndFlrSF dibiarkan apa adanya
#--- LowQualFinSF dibiarkan apa adanya
#--- GrLivArea dibiarkan apa adanya

#---BsmtFullBath
all_data['BsmtFullBath'] = all_data['BsmtFullBath'].fillna(0) 

#---BsmtHalfBath
all_data['BsmtHalfBath'] = all_data['BsmtHalfBath'].fillna(0) 

#---FullBath dibiarkan apa adanya
#---HalfBath dibiarkan apa adanya
#---Bedroom dibiarkan apa adanya
#---Kitchen dibiarkan apa adanya
# -----KitchenQual udah di QS-----
#---TotRmsAbvGrd dibiarkan apa adanya

#---Functional
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
all_data['Functional'] = all_data['Functional'].fillna(Functional_mode)
all_data['Functional'] = all_data['Functional'].map(functional_map)

#---Fireplaces dibiarkan apa adanya
# -----FireplaceQu udah di QS-----

#---GarageType
all_data['GarageType'] = all_data['GarageType'].fillna('NA') 
#selebihnya di getdummies

#---GarageYrBlt
all_data['GarageYrBlt'] = all_data['GarageYrBlt'].fillna(0)

#---GarageFinish
garage_fin_map = {
    'Fin': 3,
    'RFn': 2,
    'Unf': 1,
    'NA': 0
}
all_data['GarageFinish'] = all_data['GarageFinish'].fillna('NA')
all_data['GarageFinish'] = all_data['GarageFinish'].map(garage_fin_map)

#---GarageCars
all_data['GarageCars'] = all_data['GarageCars'].fillna(0)

#---GarageArea
all_data['GarageArea'] = all_data['GarageArea'].fillna(0) 

# -----GarageQual udah di QS-----
# -----GarageCond udah di QS-----

#---PavedDrive
paveddrive_map = {
    'Y': 2,
    'P': 1,
    'N': 0
}
all_data['PavedDrive'] = all_data['PavedDrive'].map(paveddrive_map)

#---WoodDeckSF dibiarkan
#---OpenPorchSF dibiarkan
#---EnclosedPorch dibiarkan
#---3SsnPorch dibiarkan
#---ScreenPorch dibiarkan
#---PoolArea dibiarkan

# -----PoolQC udah di QS-----

#---Fence
fence_map = {
    'GdPrv': 4,
    'MnPrv': 3,
    'GdWo': 2,
    'MnWw': 1,
    'NA': 0
}
all_data['Fence'] = all_data['Fence'].fillna('NA')
all_data['Fence'] = all_data['Fence'].map(fence_map)

#---MiscFeature
all_data['MiscFeature'] = all_data['MiscFeature'].fillna('None')
#selebihnya di getdummies

#---MiscVal dibiarkan

#---MoSold
all_data["MoSold"] = all_data["MoSold"].fillna(MoSold_mode)

#---YrSold
all_data["YrSold"] = all_data["YrSold"].fillna(YrSold_mode)

#---SaleType
all_data['SaleType'] = all_data['SaleType'].fillna(SaleType_mode)
#selebihnya di getdummies

#---SaleCondition
all_data['SaleCondition'] = all_data['SaleCondition'].fillna(SaleCondition_mode)
#selebihnya di getdummies

# -------------------------QC
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
    all_data[col] = all_data[col].fillna("NA")
for col in qual_cond_cols:
    all_data[col] = all_data[col].map(qual_cond_map)
#--------------------------QC

#--------------------------getdummies
getdummies_cols = ['MSSubClass','MSZoning','Alley','Street','LandContour',
                   'LotConfig','Neighborhood','Condition1','Condition2',
                   'BldgType','HouseStyle','RoofStyle','RoofMatl',
                   'Exterior1st','Exterior2nd','MasVnrType','Foundation'
                   ,'Heating','MiscFeature','SaleType','SaleCondition','GarageType']


all_data[getdummies_cols] = all_data[getdummies_cols].astype(str)
all_data = pd.get_dummies(all_data, columns=getdummies_cols, drop_first=True)
#--------------------------getdummies

df_processed = all_data[:ntrain]
dft_processed = all_data[ntrain:]


# done
# alhamdulillah
# real kejar tayang
# iya anjer aowkoawko
# up igs