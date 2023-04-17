from Finder import Finder
import numpy as np

worldseed = int(input("Please enter your world seed (No text seeds, numberic form only!): "))
print("\nEnter 'Y' if your world is superflat, anything else if its not!")
print("If you don't specify this correctly, you'll get wrong coords!\n")

superflat = input("Superflat? :") == 'Y'
print("\n\n")

mode_max = 3
mode = 0

while mode < 1 or mode > mode_max:
    print("""
        Which Search-Mode would you like to use?\n
        \t1: All strongholds\n
        \t2: Strongholds within ring\n
        \t3: nearest x strongholds\n\n
    """)

    mode = int(input("Please select your mode: "))

#would like to use match cases here, but python 3.9 isn't old enoght *yet*
out = []

finder = Finder(worldseed,superflat)

if mode == 1:
    out = finder.findAll()
elif mode == 2:
    ring = 0
    while ring < 1 or ring > 8:
        ring = int(input("Please enter your ring: "))

    out = finder.findRing(ring)
else:
    x = int(input("Please enter your x coordinate: "))
    z = int(input("Please enter your z coordinate: "))
    amount = int(input("How many strongholds would you like to find: "))

    out =finder.findNearestX(np.array([x,z]),amount)


print("Done looking for your strongholds! Here is a list of coordinates: ")

if mode != 3:
    for coordinate in out:
        print(str(coordinate))
else:
    positions = out[0]
    distances = out[1]

    for i in range(0, len(positions)):
        print("{pos}  Distance: {dis}".format(pos=positions[i],dis=distances[i]))