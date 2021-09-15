# Script Begins

# Tuple Structure
myTuple = ()                                        # Creating an empty touple
print (myTuple)

myTuple = (1, 2, 3, 4, 5)                           # Creating a tuple with values
print (myTuple)

print (myTuple[:])                                  # Prints all the items
print (myTuple[:2])                                 # Prints from starting to before the defined index
print (myTuple[2:4])                                # Prints from 1st defined index to before the 2nd defined index
print (myTuple[0])                                  # Prints item of defined index
print (myTuple[::1])                                # Prints all the items forward direction
print (myTuple[::-1])                               # Prints all the items reverse direction

myTuple = myTuple + (6, 7, 8)                       # Adding new items or adding another tuple
print (myTuple)

tuple2 = (9, 10)
myTuple = myTuple + tuple2
print (myTuple)

myTuple = myTuple + (10, [10, 'python'])
print (myTuple)

myTuple[11][1] = 13                                 # Can manipulate items if the item is mutable inside the tuple
print (myTuple)

print (myTuple.count(10))                           # Counts all the matches at items at top level

print (myTuple.index(10))                           # Provides the index of first matched item

# Script Ends