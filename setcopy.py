'''
Sets are used to store multiple items in a single variable.
It is a collection of unordered, unchangable and unindexed items.
Items in a set are unchangable but can be removed and added. 
Set cannot have duplicate value and once it is created cannot 
change its value. 
A set can have any number of items and different datatypes(heterogeneous).
Items in a set is enclosed in {} and separated by comma.
To create an empty set, set() function is used.
The major advantage of using a set as opposed to a list,
is that it has highly optimized method for checking whether a 
specific element is contained in the set. This is based on a data 
structure known as hash table.

Methods for Sets
set.add() => adding element to set

'''

#Operators vs Methods
'''
Set operations can be performed in 2 different ways:
by operator or by method. 
'''
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x3 = {1, 2, 3, 4}
x4 = {2, 3, 4, 5}

#Union - reurn the set of all elements in either x1 or x2.
x1 | x2 #operator
x1.union(x2) #method
x1.union(x2, x3, x4) #or
x1 | x2 | x3 | x4

#Difference - return set of all elements that are in x1 but not in x2. 
x1 - x2
x1.difference(x2)
x1 - x2 - x3 - x4 #with multiple sets, operation is performed from left to right.
x1.difference(x2, x3, x4)

#intersection - return set elements common to both x1 and x2
x1 & x2
x1.intersection(x2)
x1 & x2 & x3 & x4

#Symmetric difference - returns elements in either x1 or x2, but not both.
x1.symmetric_difference(x2) # method doesn't allow multiple sets
x3 ^ x4
x1 ^ x2 ^ x3

#Superset check - retrn True if x1 is a superset of x2
x1.issuperset(x2) 
x1 >= x2
#A proper superset is the same as superset, 
#except the set can't be identical. 
# A set x5 is considered a proper superset of another set
#x6 if x5 and x6 are not equal.
x5 = {'vim', 'bim', 'tim'}
x6 = {'vim', 'bim'}
x5 > x6
#output True
x5 = {'vim', 'bim', 'tim'}
x6 = {'vim', 'bim', 'tim'}
x5 > x6  
#output False
#The > operator is the only way to test whether
#a set is a proper subset. There is no corresponding method.
 
#Subset check - return Trueif x1 is a subset of x2
x1.issubset(x2)
x1 <= x2
#The < operator is the only way to test whether
#a set is a proper subset. There is no corresponding method.
#While a set is considered a subset of itself,
#it is not a proper subset of itself.
x1 <= x1
#output True
x1 < x1
#output False

#Disjoint check - returns true if x1 and x2 have no elements in common.
x1.isdisjoint(x2)
{1, 2}.isdisjoint({3, 4})
#There is no operator that corresponds to the .isdisjoint() method

#Existence check
2 in {1,2,3}
4 in {1,2,3}
4 not in {1,2,3}


#Modifying a set
#Modify a set by union
x1.update(x2) #add to x1 any elements in x2 that x1 doesn't have already
x1 |= x2 
x1.update(x2[x3, x4]) #multiple sets
x1 |= x2[x3, x4]
#Modify a set by intersection
x1.intersection_update(x2) #updates x1, retaining only elements found in both x1 and x2
x1 &= x2
x1.intersection_update(x2[x3, x4]) #multiple sets
x1 &= x2[x3, x4]
#Modify a set by difference
x1.difference_update(x2) #updates x1, removing elements found in x2
x1 -= x2
#Modify a set by symmetric difference
x1.symmetric_difference_update(x2) 
x1 ^= x2 #updates x1, retaining elements found in either x1 or x2, but not in both

s = {1,2,3}
s.add(4) #adds an element to a set(must be single immutable object)
s.discard(3) #removes an element from a set. doesn't raise exception
s.remove(2) #removes an element from a set also raises exception if element is not found in set
s.pop() # removes random element from a set/raises exception if element is not found/set is empty
s.clear() # removes all elements in a set

#Frozenset
#Frozenset is immutable. 
#Non-modifying operations can be performed on a frozenset
f = frozenset(['ho', 'ha', 'he'])



#note: {1} creates a set of one element, but {} creates an empty dict.
#The correct way to create an empty set is set().

#Using Method in Set Operatios
a = {1,2,2,3,4}
b = {3,3,4,4,5}

#intersection
a.intersection(b) # a & b - returns a new set with elements present in a and b
#union
a.union(b) # a| b - returns a new set with elements present in either a and b.
#difference
a.difference(b) # a - b - returns a new set with  elements present in a but not in b.
#symmetric_difference works both ways
a.symmetric_difference(b) # a ^ b -returns new set with elements either present in a or b but not in both.
#subset 
b.issubset(a) # b <= a -tests whether each element in b is in a
#superset
a.issuperset(b) # a >= b -tests wheter each element of a is in b.

#Sets vs multisets
#Set discards duplicated elements when printed causing loss of data. 
#To avoid this, save elements in list.