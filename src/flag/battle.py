from collections import namedtuple
DODGED = object()
BLOCKED = object()
CRIT = namedtuple('CRIT', ['damage'])
ATTACKED = namedtuple('ATTACKED', ['damage'])
