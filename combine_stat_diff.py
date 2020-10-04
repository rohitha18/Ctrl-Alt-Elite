import os
import glob
import pandas as pd

os.chdir("/Users/raghuvarapadma/PycharmProjects/Ctrl-Alt-Elite/COLLEGE_EDITED_stat_diff")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Site', 'Line', 'Unnamed: 0.1.1', 'Unnamed: 0.1.1.1', 'Line '], inplace=True, axis=1)
combined_csv.to_csv( "/Users/raghuvarapadma/PycharmProjects/Ctrl-Alt-Elite/COLLEGE_EDITED_stat_diff/combined.csv", index=True, encoding='utf-8-sig')