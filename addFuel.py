#The modified dataset is already present in the 
#file, NO need to run this file
# 
# This file is required to generate the fuel burn 
# of flights using passengers and distance. In Ideal 
# scenario if FDR data available, we would have 
# past records of fuel burn data available, which 
# would make this calculation unnecessarry.  
import pandas as pd 

#3.5 per 100 passenger kilometer 
# no of passenger * distance * 3.5 / 100 
df = pd.read_csv('Original_Dataset/T_T100D_SEGMENT_US_CARRIER_ONLY.csv')
df['FUEL_BURN'] = df['PASSENGERS'] * df['DISTANCE'] * 3.5 / 100 
df.to_csv('US_CARRIER_DATASET.csv')