
# how to think about this problem: Given a point p, and other n points in two-dimensional space, find k points out of n points which are nearest to p.

# note: Distance between two points is measured by the standard Euclidean method.

import heapq

def get_squared_distance(p1, p2):
    """
    Helper function to calculate squared Euclidean distance.
    (x2 - x1)^2 + (y2 - y1)^2
    """
    sq_dist = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
    return sq_dist


def k_nearest_points(p, points, k):
    # (p: Tuple[int, int], points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    # Edge case: if k is greater than or equal to the total number of points
    
    if k >= len(points):
        return print(points)
    max_heap = []
    for point in points:
        dist = get_squared_distance(p, point)
        heapq.heappush(max_heap, (-dist, point))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return print([item[1] for item in max_heap])

# def k_nearest_points_heapify(p, points, k):
#     if k >= len(points):
#         return print(points)

#     # 1. Gather ALL points into a list first
#     min_heap = []
#     for point in points:
#         dist = get_squared_distance(p, point)
#         # Notice we are pushing POSITIVE distances now, and just appending to a normal list
#         min_heap.append((dist, point))
        
#     # 2. Organize the entire list into a Min-Heap in one shot
#     heapq.heapify(min_heap)
    
#     # 3. Pop the K closest points
#     ans = []
#     for _ in range(k):
#         # We pop the top (closest) item K times
#         closest_point = heapq.heappop(min_heap)[1]
#         ans.append(closest_point)
        
#     return print(ans)


k_nearest_points((5, 5), [], 5)
# ((0, 0), [(1, 1), (2, 2), (3, 3), (-1, 0)], 2), [(-2, (1, 1)), (-1, (-1, 0))]
#((2, 2), [(2, 4), (4, 2), (0, 2), (2, 0), (9, 9)], 3), [(-4, (2, 0)), (-4, (2, 4)), (-4, (4, 2))]
#((5, 5), [(1, 1), (2, 2)], 5), [(1, 1), (2, 2)]