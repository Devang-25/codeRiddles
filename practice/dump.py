import scipy
scipy.sort_complex
# OUT: <function sort_complex at 0x972cb1c>
scipy.sort_complex(1,33,12)
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: sort_complex() takes exactly 1 argument (3 given)
a=[2,33,1,12,3]
scipy.sort_complex(a)
# OUT: array([  1.+0.j,   2.+0.j,   3.+0.j,  12.+0.j,  33.+0.j])
a=[2+12.j,33+1.j,1+13.j,12,3+10.j]
scipy.sort_complex(a)
# OUT: array([  1.+13.j,   2.+12.j,   3.+10.j,  12. +0.j,  33. +1.j])
a=[2+12.j,33+1.j,1+13.j,12,3+10.j,3+3.j]
scipy.sort_complex(a)
# OUT: array([  1.+13.j,   2.+12.j,   3. +3.j,   3.+10.j,  12. +0.j,  33. +1.j])


