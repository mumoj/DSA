import math

def solution(area):
    sq_area_list = []
    while area>=1 and area<=1000000:
        largest_sq_area = math.floor(math.sqrt(area)) * math.floor(math.sqrt(area))
        print(largest_sq_area)
        sq_area_list.append(int(largest_sq_area))
        area -= largest_sq_area
    return sq_area_list

print (solution(area=12))
