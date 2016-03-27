#!/usr/bin/env python3

import operator
from collections import Counter

x = """ Their caching tier services 120 million queries every 
second and it's the core of the site. The problem is memcached 
is hard to use because it requires programmer cooperation. It's 
also easy to corrupt. They've developed a complicated system to 
keep data in the caching tier consistent with the database, 
even across multiple distributed data centers. Remember, they 
are caching user data here, not HTML pages or page fragments. 
Given how much their data changes it's would be hard to make 
page caching work."""

print(x,"\n")
x = x.replace('\n', ' ')
x = x.strip()
c = Counter(x.split())

print(sorted(c.items(), key=operator.itemgetter(1), reverse=True)[:3])
