#!/usr/bin/env python3

import numpy as np

x = np.random.random_integers(-1, 1, (4,4))
print(x)
y = np.matrix([np.linspace(-1, 1, 4) for x in range(4)])
print(y)
