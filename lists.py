# List Compregensions:

squares = []
for x in range(10):
     squares.append(x**2)

print squares

# or more coincise:

squares = [x**2 for x in range(10)]

print squares

# another example:
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

print combs

# is equivalent to:
combs = []
for x in [1,2,3]:
     for y in [3,1,4]:
          if x != y:
               combs.append((x,y))

print combs

# anothere example:
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled:
new_vec = [x*2 for x in vec]
print new_vec
# filter the list to exclude negative numbers:
no_neg = [x for x in new_vec if x >= 0]
print no_neg
# apply a function to all the elements:
func = [abs(x) for x in vec]
print func
