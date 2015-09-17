I used a euclidian distance multiplied by the cost of moving one unit (10) as my second heuristic.
It works by finding the straight line distance between the current location and the goal by using pythagorean theorem and multiplying by the cost of movement.
The equation is 10*(sqrt((x2-x1)^2 + (y2-y1)^2)).
This heuristic is valid because it will provide an underestimate of distance in all cases, but be somewhat close to the diagonal distance.
I chose it because I wanted to compare the results of using the manahattan distance to the true straight line distance.
My heuristic discoverd the exact same solutions as the manhattan heuristic and visited the same number of squares to do it.
This showed that the manhattan distance does produce the same results as a true (non integer) straight line distance.


TO RUN THIS PROGRAM VIA COMMAND LINE:

use "python3 Schiller_Justin_HW3.py [world text file] [heuristic: can be either manhattan or euclidian]"
