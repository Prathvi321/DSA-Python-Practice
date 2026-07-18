# Priority Queue

import heapq

hospital = []
#lower number = higher priority

heapq.heappush(hospital, (3, "Broken Leg"))
heapq.heappush(hospital, (1, "Heart attack"))
heapq.heappush(hospital, (2, "high fever"))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))

#heapq.heappush(hospital,)