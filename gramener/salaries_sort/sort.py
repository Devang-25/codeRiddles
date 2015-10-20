import pandas as pd
df = pd.read_csv('salaries.csv')
df = df.sort_values('Job')

lawyers_order = df.set_index(['Job'])\
                  .ix['Lawyers']\
                  .sort_values('Salary',ascending=False)
# if just lawyers' salaries are needed, don't go to 2nd part
# for i,j in lawyers_order.values: print "%s,%s"%(i,j)

# 2nd part
df['City'] = pd.Categorical(df['City'],
                            lawyers_order.City[::-1])
jobs = df.Job.unique()
df = df.set_index(['Job','City'])
idx = pd.IndexSlice
for _job in jobs:
    print "\n\t",_job
    for v in df.loc[idx[_job,:]].reset_index().values[::-1]:
        print "%s,%s"%(v[0],v[-1])        
