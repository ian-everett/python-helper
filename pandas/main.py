import numpy as np
import pandas as pd

#
# cvs history data '2019-09-17__14_05.csv' is controller data:-
#   8 Probe zones with only the first two turned on and controlling
#   1 IO zone reading room temp
#
# The two zones are heated to 175°C and left running
#
filename = '2019-09-17__14_05.csv'
df = pd.read_csv(filename, sep='\t', skip_blank_lines=True, header=[0,1])

# Remove Unnamed columns from second header
# Mode, Total Amps etc...
cols = df.columns.get_level_values(1)
df = df.loc[:, ~cols.str.contains('^Unnamed')]

# Drop columns from frame
#df.drop(df.columns[[0, 1, 2, 3]], axis=1, inplace=True)

print(df.columns)
#print(df[('Probe  1', 'Temp')])
#print(df.columns.get_level_values(1))