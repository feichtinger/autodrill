
import math

# find a (short) path through the set of points
def findPath(points):
	
	path=[points.pop()]		# start with a random point
	
	
	while points:
	
		# find the next point using nearest neighbour search
		
		base=path[-1]			# last path point is base point for NN search
		mindist=float("inf")	# minimal distance
		
		for p in points:
			if distance(base, p) < mindist:
				mindist = distance(base, p)
				bestPoint = p
		
		path.append(bestPoint)		# append nearest point to path
		points.remove(bestPoint)
		
	return path



# euclidian distance between 2 points
def distance(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
