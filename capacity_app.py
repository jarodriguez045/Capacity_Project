import pandas
from pathlib import Path

# modify file location before deployment
workbook = Path("/home/jose_rodriguez/Desktop/github/Capacity_Project/workbooks/capacity_metrics2.csv")

securesync = "SecureSync"
data_tbl = pandas.read_csv(workbook, index_col='WK', parse_dates=['Date'], header=0)

data_tbl['Actual Time'].where(data_tbl['Product #']==securesync)

