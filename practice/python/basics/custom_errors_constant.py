#!/bin/env python3

# ref
# - https://www.python-course.eu/python3_exception_handling.php
# related discussion (comments) at http://code.activestate.com/recipes/65207-constants-in-python/?in=user-97991


import const
# and bind an attribute ONCE:
const.magic = 23
# but NOT re-bind it:
const.magic = 88      # raises const.ConstError
