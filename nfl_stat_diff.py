import pandas as pd

df = pd.read_csv('/Users/raghuvarapadma/PycharmProjects/data_challenge/NFLDATA_ORIGINAL/NFLDATA2004.csv')

print(len(df))
df.dropna(inplace=True)
print(len(df))

df['ThirdDownPctOff'] = df['ThirdDownPctOff'].apply(lambda x: x[:len(x)-1])
df['ThirdDownPctOff'] = pd.to_numeric(df['ThirdDownPctOff'])
df['ThirdDownPctDef'] = df['ThirdDownPctDef'].apply(lambda x: x[:len(x)-1])
df['ThirdDownPctDef'] = pd.to_numeric(df['ThirdDownPctDef'])

df['TimePossOff'] = df['TimePossOff'].astype(str)
df['TimePossDef'] = df['TimePossDef'].astype(str)
df['TimePossOff'] = df['TimePossOff'].apply(lambda x: int(x[:x.find(':')]))
df['TimePossDef'] = df['TimePossDef'].apply(lambda x: int(x[:x.find(':')]))

df['ScoreDiff'] = df['ScoreOff'] - df['ScoreDef']
df['FirstDownDiff'] = df['FirstDownOff'] - df['FirstDownDef']
df['ThirdDownPctDiff'] = df['ThirdDownPctOff'] - df['ThirdDownPctDef']
df['RushAttDiff'] = df['RushAttOff'] - df['RushAttDef']
df['RushYdsDiff'] = df['RushYdsOff'] - df['RushYdsDef']
df['PassAttDiff'] = df['PassAttOff'] - df['PassAttDef']
df['PassCompDiff'] = df['PassCompOff'] - df['PassCompDef']
df['PassYdsDiff'] = df['PassYdsOff'] - df['PassYdsDef']
df['PassIntDiff'] = df['PassIntOff'] - df['PassIntDef']
df['FumblesDiff'] = df['FumblesOff'] - df['FumblesDef']
df['SackYdsDiff'] = df['SackYdsOff'] - df['SackYdsDef']
df['PenYdsDiff'] = df['PenYdsOff'] - df['PenYdsDef']
df['TimePossDiff'] = df['TimePossOff'] - df['TimePossDef']

df['ThirdDownPctDiff'] = df['ThirdDownPctDiff'].round(1)
df.to_csv('/Users/raghuvarapadma/PycharmProjects/data_challenge/NFLDATA_EDITED_stat_diff/NFLDATA2004.csv')