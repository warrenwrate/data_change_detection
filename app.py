
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
changed_rows = list(set(d.keys()) & set(old_d.keys()))
ended_rows = set(old_d.keys()) - set(d.keys())

print('new rows', new_rows)
print('ended_rows', ended_rows)
print('new row count', len(new_rows))

for n in new_rows:
	ptpid, benid, startdate, tier, plan, coverageamount = d[n].split('-')
	print('ParticipantID:{}, StatDate:{}, Tier:{}, Plan:{}'.format(ptpid, startdate, tier, plan))

for x in changed_rows:
	ptpid, benid, startdate, tier, plan, coverageamount = d[x].split('-')
	o_ptpid, o_benid, o_startdate, o_tier, o_plan,  o_coverageamount = old_d[x].split('-')
	if d[x] != old_d[x]:
		print('New Values: ParticipantID:{}, StatDate:{}, Tier:{}, Plan:{}'.format(ptpid, startdate, tier, plan))
		print('Old Values: ParticipantID:{}, StatDate:{}, Tier:{}, Plan:{}'.format(o_ptpid, o_startdate, o_tier, o_plan))
		count += 1
		

print('changes:', count)
