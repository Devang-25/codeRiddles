import pandas as pd
df = pd.read_csv('salaries.csv')
df = df.sort_values('Job').set_index(['Job'])
df1 = df.ix['Lawyers'].copy()
df1 = df1.sort_values('Salary',ascending=False)
for i,j in df1.values: print "%s,%s"%(i,j)

# order = df1.sort_values('Salary',ascending=False).index.tolist()
# df = df.set_index(['Job','City'])
# df.sortlevel(0)
# df.sort_index(0)
# question: how to custom sort using `order` ?
