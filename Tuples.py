#Tuples are an ordered set of unmutable (unchangeable) items
#Tuples support indexing and slicing
#titles are good at holding hetrogenous types of data that will not change (e.g. an album title, artist, and year released are all static)

# t = "a", "b", "c"
# #this is a tuple
# print(t)
#
# print("a", "b", "c")
# #this is a tuple, need two brackets to print a tuple
# print(("a", "b,", "c"))

#another tuple, you can have multiple data types within a tuple
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
#imelda is an example of a tuple with tuples contained in it for the track list
imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (2, "Pyscho"), (3, "Mayhem")
metallica = "Ride the Lightning", "Metallica", 1984
#prints the entire tuple
print(metallica)
#Only prints the element at position 0
print(metallica[0])

#Changing data within a tuple, for example if there is a typo
#we can do this by recreating the entire tuple
#This can either be done by referencing data from an index in the initial tuple or by entering all new data
# imelda = imelda[0], "Imelda May", 2011
# print(imelda)

#lists are mutable, for example we can directly edit data in a list
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)

#Example of unpacking the tuple so that we are able to assign values from within the tuple to specific variables
title, artist, year, track1, track2, track3 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
