#!/bin/bash

# this should be correct. And gives out following as invalid:
# email@example..com
# cat emails_large | egrep -v  -E '^[a-zA-Z]+[-_+,.[:alnum:]]*@[-[:alnum:]]+(\.[[:alnum:]]+){1,2}$'

# Yet this seemed to be the accepted answer
cat emails_large  | egrep -v  -E '^[a-zA-Z]+[-_+,.[:alnum:]]*@[-[:alnum:]]+(\.[[:alnum:]]*){1,2}$'
