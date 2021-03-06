'''
Preprocessing for metadata script
1. remove metadata entries that have no mapping in the dataset
2. remove duplicated metadata entries (identified by IDs)
'''

import os

metadata_csv_in = './Env1_meta/Env1_meta.csv'
metadata_csv_out = './Env1_meta/Env1_meta_aligned.csv'

f = open(metadata_csv_in)
lines = f.readlines()
f.close()

new_lines = []
s = set()

for line in lines:
	item = line.split(',')
	pt = '../data/Env1/' + str(item[0]) + '.wav'
	if os.path.exists(pt) and item[0] not in s:
		new_lines.append(line)
		s.add(item[0])

f_out = open(metadata_csv_out,'w')
l = ''.join(new_lines)
f_out.write(l)
f.close()