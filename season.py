import pandas as pd

df = pd.read_csv('/Users/raghuvarapadma/PycharmProjects/Ctrl-Alt-Elite/NFLDATA_EDITED_stat_diff/NFLDATA2013.csv')

df['season'] = 2013

print(df)

df.to_csv('/Users/raghuvarapadma/PycharmProjects/Ctrl-Alt-Elite/NFLDATA_EDITED_stat_diff/NFLDATA2013.csv')
