import pandas as pd

df = pd.read_csv('/Users/raghuvarapadma/PycharmProjects/Ctrl-Alt-Elite/COLLEGE_EDITED_stat_diff/COLLEGEDATA2000.csv')

df.rename(columns={"Week":"Date", "Team":"TeamName"}, inplace=True)

df.to_csv('/Users/raghuvarapadma/PycharmProjects/Ctrl-Alt-Elite/COLLEGE_EDITED_stat_diff/COLLEGEDATA2000.csv')
