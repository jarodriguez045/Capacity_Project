import pandas as pd
import numpy as np
from pathlib import Path

# modify file location before deployment
workbook = Path("/home/jose_rodriguez/Desktop/github/Capacity_Project/workbooks/capacity_metrics2.csv")

# edit to allow user input. 
# sort csv to read line dataframe
dt = pd.read_csv(workbook, index_col='WK', parse_dates=['Date'], header=0)

# sort data by variable and create list of values
is_ss = dt['Product Family']=='SecureSync'
dt_pf = dt[is_ss]
lst_atime = dt_pf['Actual Time'].to_list()

# Calculate Average
avg = np.nanmean(lst_atime)
print(avg)