from Random import PseudoRandom
import numpy as np
import math

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


class Finder:
    def __init__(self,worldseed,superflat):
        self.worldseed = worldseed
        self.superflat = superflat
        self.pr = PseudoRandom(worldseed)

    def getSeed(self):
        return self.worldseed


    def findRingUnsafe(self, ring_num): #carefull! this one does NOT set random to the correct values before doing anything
        out = []
        ring = stronghold_rings[ring_num-1]

        angle = self.pr.rand()
        angle = (angle / 32767) * (math.pi*2)

        for a in range(1, ring[0]+1):
            dist = self.pr.randminmax(ring[1],ring[2])

            if self.superflat != True:
                self.pr.randminmax(bedrock_max+1,overworld_min+68) #mineclone would do height calculations here, and uses "random" numbers if world is NOT superflat
                #however, that changed the next number, so I have to do that here as well

            pos = np.array([math.cos(angle) * dist , math.sin(angle) * dist])
            pos = np.round(pos,2)

            out.append(pos)

            angle = math.fmod(angle + ((math.pi*2) / ring[0]), math.pi*2)

        return out


    def findRing(self,ring_num): #when you aren't in this class, you may only use this method
        self.pr.reset()
        for i in range(0,ring_num-1):
            self.pr.rand()
            for p in range(0, stronghold_rings[i][0]):
                self.pr.rand()
                if not self.superflat:
                    self.pr.rand()
 
        return self.findRingUnsafe(ring_num)

    def findAll(self):
        out = []
        for i in range(1,len(stronghold_rings)+1):
            out += self.findRing(i)

        self.pr.reset()
        return out

    def findNearestX(self,pos, amount):
        positions = []
        distances = []
        for i in range(0,amount):
            positions.append(None)
            distances.append(0xffff)
            
        for stronghold in self.findAll():
            if (np.linalg.norm(stronghold-pos) < max(distances)):
                maxindex = distances.index(max(distances))
                distances[maxindex] = np.linalg.norm(stronghold-pos)
                positions[maxindex] = stronghold


        return [positions,distances]