from fractions import Fraction

    
def solution(pegs):

    if len(pegs)%2 == 0:
        x = 2.0/3.0
    else:
        x = 2.0

    def valid_gear_arrangement(first_radius, distances_btn_pegs):
        if len(pegs) <2:
            return False

        current_radius=first_radius
        for distance in distances_btn_pegs:
            if current_radius < 1:
                return False
            else:
                current_radius = distance - current_radius
        return True
        
    distances_btn_pegs = [pegs[i]-pegs[i-1] for i in xrange(1, len(pegs))]

    sumof_even_indexed_distances = 0
    sumof_odd_indexed_distances = 0
    for i,distance in enumerate(distances_btn_pegs):
        if i%2 == 0:
           sumof_even_indexed_distances += distance
        else:
           sumof_odd_indexed_distances += distance

    first_radius = x * (sumof_even_indexed_distances - sumof_odd_indexed_distances)

    if valid_gear_arrangement(first_radius, distances_btn_pegs):
        fraction = Fraction(first_radius).limit_denominator()
        return [fraction.numerator, fraction.denominator]
    else:
        return [-1,-1]


print(solution([4, 30, 50]))