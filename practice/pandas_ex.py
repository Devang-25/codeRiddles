import numpy as np
import pandas as pd
from itertools import product

np.random.seed(1)

team_names = ['Yankees', 'Mets', 'Dodgers']
jersey_numbers = [35, 71, 84]
game_numbers = [1, 2]
observer_names = ['Bill', 'John']
observation_types = ['Speed', 'Strength']

row_indices = list(product(team_names, jersey_numbers, game_numbers, observer_names, observation_types))
observation_values = np.random.randn(len(row_indices))

tns, jns, gns, ons, ots = zip(*row_indices)

data = pd.DataFrame({'team': tns, 'jersey': jns, 'game': gns, 'observer': ons, 'obstype': ots, 'value': observation_values})
print "raw data: \n", data.to_string(),"\n"

print "After doing data.T: \n",data.T,"\n"

data1 = pd.pivot_table(data, values='value', cols=['observer', 'obstype'], rows=['team', 'jersey', 'game'])
print "After using pivot_table: \n",data1.to_string(),"\n"

data2 = data1.unstack()
data2.columns = data2.columns.droplevel(0)
print "After using unstack and droplevel:\n", data2.to_string(),"\n"
