# this is the all basics
#
#
#
# enjoy

# arithmetic
1 + 1 # 2
1 - 1 # 0
1 * 1 # 1
1 / 1 # 1

# division round
5 // 2 # 2
-5 // 2 # -3
5.0 // 2.0 # 2.0
-5.0 // 2.0 # -3.0

# modulo
5 % 2 # 1
-5 % 2 # 1

# exponention
5 ** 2 # 25

# ensure priority
1 + 2 * 3 # 7
(1 + 2) * 3 # 9

# boolean
True
False
not True # False
not False # True

# boolean operators
True and False # False
True or False # True

# True, False also are 1, 0
True + True # 2
True + True * False # 1

# True, False comparison operators
1 == False # False
0 == False # True

### fun ###
# None, 0, empty strings,lists,dicts,tuples,sets == to False
# all other values are True
bool(0) # False
bool("") # False
bool([]) # False
bool({}) # False
bool(()) # False
bool(set()) # False
bool(1) # True
bool(-1) # True

''' i dont fucking care
# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
bool(0)     # => False
bool(2)     # => True
0 and 2     # => 0
bool(-5)    # => True
bool(2)     # => True
-5 or 0     # => -5
what's written here
'''

# ==
1 == 1 # True
0 == 1 # False

# !=
1 != 1 # False
0 != 1 # True

# comparisons
0 < 1 # True
0 > 1 # False
0 <= 1 # True
0 >= 1 # False