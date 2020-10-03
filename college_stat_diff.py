import pandas as pd

df = pd.read_csv('/Users/raghuvarapadma/PycharmProjects/data_challenge/COLLEGE_ORIGINAL/COLLEGEDATA2013.csv')

print(len(df))
df.dropna(inplace=True)
print(len(df))
df['ScoreOff'] = df['ScoreOff'].astype(int)
df['ScoreDef'] = df['ScoreDef'].astype(int)
df['RushAttOff'] = df['RushAttOff'].astype(int)
df['RushAttDef'] = df['RushAttDef'].astype(int)
df['PassAttOff'] = df['PassAttOff'].astype(int)
df['PassAttDef'] = df['PassAttDef'].astype(int)
df['PassCompOff'] = df['PassCompOff'].astype(int)
df['PassCompDef'] = df['PassCompDef'].astype(int)
df['PassYdsOff'] = df['PassYdsOff'].astype(int)
df['PassYdsDef'] = df['PassYdsDef'].astype(int)
df['PassIntOff'] = df['PassIntOff'].astype(int)
df['PassIntDef'] = df['PassIntDef'].astype(int)
df['FumblesOff'] = df['FumblesOff'].astype(int)
df['FumblesDef'] = df['FumblesDef'].astype(int)

df['ScoreDiff'] = df['ScoreOff'] - df['ScoreDef']
df['RushAttDiff'] = df['RushAttOff'] - df['RushAttDef']
df['RushYdsDiff'] = df['RushYdsOff'] - df['RushYdsDef']
df['PassAttDiff'] = df['PassAttOff'] - df['PassAttDef']
df['PassCompDiff'] = df['PassCompOff'] - df['PassCompDef']
df['PassYdsDiff'] = df['PassYdsOff'] - df['PassYdsDef']
df['PassIntDiff'] = df['PassIntOff'] - df['PassIntDef']
df['FumblesDiff'] = df['FumblesOff'] - df['FumblesDef']

df.to_csv('/Users/raghuvarapadma/PycharmProjects/data_challenge/COLLEGE_EDITED_stat_diff/COLLEGEDATA2013.csv')
