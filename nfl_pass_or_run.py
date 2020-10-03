import pandas as pd

df = pd.read_csv('/Users/raghuvarapadma/PycharmProjects/data_challenge/NFLDATA_ORIGINAL/NFLDATA2013.csv',
                 usecols=['Date', 'TeamName', 'ScoreOff', 'RushAttOff', 'RushYdsOff', 'PassAttOff', 'PassCompOff',
                          'PassYdsOff', 'PassIntOff', 'Opponent', 'ScoreDef', 'RushAttDef', 'RushYdsDef', 'PassAttDef',
                          'PassCompDef', 'PassYdsDef', 'PassIntDef'])

print(len(df))
df.dropna(inplace=True)
print(len(df))

df['ScoreDiff'] = df['ScoreOff'] - df['ScoreDef']

df['RushAvgOff'] = (df['RushYdsOff'] / df['RushAttOff']).round(2)
df['PassCompRateOff'] = (df['PassCompOff'] / df['PassAttOff']).round(2)
df['PassYardsAttOff'] = (df['PassYdsOff'] / df['PassAttOff']).round(2)

df['RushAvgDef'] = (df['RushYdsDef'] / df['RushAttDef']).round(2)
df['PassCompRateDef'] = (df['PassCompDef'] / df['PassAttDef']).round(2)
df['PassYardsAttDef'] = (df['PassYdsDef'] / df['PassAttDef']).round(2)

df = df[df['ScoreDiff']>0]

print(df)
df.to_csv('/Users/raghuvarapadma/PycharmProjects/data_challenge/NFLDATA_EDITED_pass_run/NFLDATA2013.csv')
