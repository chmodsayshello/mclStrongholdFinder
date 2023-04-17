import numpy as np
import math
from Random import PseudoRandom

stronghold_rings = [
    [3,1408,2688],
    [6,4480,5760],
    [10,7552,8832],
    [15,10624,11904],
    [21,13696,14976],
    [28,16768,18048],
    [36,19840,21120],
    [9,22912,24192]
]

bedrock_max = -58
overworld_min = -62

worldseed = int(input("Please enter your world seed (No text seeds, numberic form only!): "))
print("\nEnter 'Y' if your world is superflat, anything else if its not!")
print("If you don't specify this correctly, you'll get wrong coords!\n")

superflat = input("Superflat? :") == 'Y'

pr = PseudoRandom(worldseed)

print("Starting looking for strongholds on world with seed {seed}, superflat: {superflat}".format(seed=worldseed,superflat=superflat))
print("\n\n")


for s in range(0, len(stronghold_rings)):
    ring = stronghold_rings[s]

    angle = pr.rand()

    angle = (angle / 32767) * (math.pi*2)

    for a in range(1, ring[0]+1):
        dist = pr.randminmax(ring[1],ring[2])

        if superflat != True:
            pr.randminmax(bedrock_max+1,overworld_min+68) #mineclone would do height calculations here, and uses "random" numbers if world is NOT superflat
            #however, that changed the next number, so I have to do that here as well

        pos = np.array([math.cos(angle) * dist , math.sin(angle) * dist])
        pos = np.round(pos,2)

        print("found stronghold in the {ring}th stronghold ring! Position: {pos}".format(ring=s+1,pos=str(pos)))

        angle = math.fmod(angle + ((math.pi*2) / ring[0]), math.pi*2)