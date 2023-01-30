#Sets and Frozen Sets

#Lists and sets are very similar
#Sets are unordered

#Create a set

car_parts = {"Wheels", "Doors","Exhaust"}

print(car_parts)
#remove things from the set
car_parts.discard("Doors")
print(car_parts)

# add things to a set

car_parts.add("windows")
print(car_parts)

#Frozen sets

#frozen sets a immutable (cannot be changed) versions of a set. still un-ordered and un-indexed.
#we a

x = frozenset([1, 2, 3, "Five"])
print(x)