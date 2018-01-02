import random

# age_data is /usr/shar/dict/words stripped of lines with comma

fin = open('age_data')
fout = open('age_data_remodelled', 'w')

while True:
    data = fin.readline()
    if not data:
        break
    fout.write('%s,%s,%s\n' % (
        data.rstrip('\n'),
        random.randint(10,100),
        random.sample(['M','F'], 1)[0]
    ))

# egrep ',M$' -c age_data_remodelled 
# 224624
# egrep ',F$' -c age_data_remodelled 
# 225376

fin.close()
fout.close()

# TODO: replace buffer in line
