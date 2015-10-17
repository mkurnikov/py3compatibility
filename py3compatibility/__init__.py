# __future__ imports are local to module imported it
from __future__ import division
from __future__ import print_function

try:
    from future_builtins import *
except ImportError:
    pass

try:
    input = raw_input
    range = xrange
except NameError:
    pass


import resource
soft, hard = 2 ** 32, 2 ** 32 #4 gigabyte
#soft, hard = 2 * soft, 2 * hard
resource.setrlimit(resource.RLIMIT_AS,(soft, hard))
