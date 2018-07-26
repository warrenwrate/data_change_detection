
d = {}

old_d = {}

def splitline(strtext, _dict):
	key = strtext.split('-')[0] + '-' + strtext.split('-')[1]
	_dict[key] = strtext

with open('newdata.txt', 'r') as f:
	for line in f:
		splitline(line, d)

with open('olddata.txt', 'r') as o:
	for line in o:
		splitline(line, old_d)

count = 0

new_rows = set(d.keys()) - set(old_d.keys())
changed_rows = set(d.keys()) & set(old_d.keys())
ended_rows = set(old_d.keys()) - set(d.keys())

print('new rows', new_rows)
print('ended_rows', ended_rows)

