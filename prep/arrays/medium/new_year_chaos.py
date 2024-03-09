"""It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n. 
Any person can bribe the person directly in front of them to swap positions, but they 
still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to a given queue order. 
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Function Description
Complete the function minimumBribes.
minimumBribes has the following parameter(s):
int q[n]: the positions of the people after all bribes
"""

# 1 2 5 3 7 8 6 4


def minimum_bribes(q: list) -> str:
    bribes = 0
    for i, person in enumerate(q, 1):
        if person - i > 2:
            return "Too chaotic"
        else:
            increment = 0
            for p in q[i:]:
                if person > p:
                    bribes += 1
                    increment += 1
                    if increment == 2:
                        break
    return str(bribes)
