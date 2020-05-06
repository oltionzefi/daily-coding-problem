# Monte Carlo methods are a broad class of computational algorithms
# that rely on repeated random sampling to obtain numerical results
# The beauty of this algorithm is that we don’t need any graphics
# or simulation to display the generated points.
# We simply generate random (x, y) pairs and then check if  x^{2} + y^{2} <= 1
# If yes, we increment the number of points that appears inside the circle.
# In randomized and simulation algorithms like Monte Carlo,
# the more the number of iterations, the more accurate the result is.
# Thus, the title is “Estimating the value of Pi” and not “Calculating the value of Pi”.
# The Algorithm
# 1. Initialize circle_points, square_points and interval to 0.
# 2. Generate random point x.
# 3. Generate random point y.
# 4. Calculate d = x*x + y*y.
# 5. If d <= 1, increment circle_points.
# 6. Increment square_points.
# 7. Increment interval.
# 8. If increment < NO_OF_ITERATIONS, repeat from 2.
# 9. Calculate pi = 4*(circle_points/square_points).
# 10. Terminate.
import random

INTERVAL = 1000


def estimate_pi(dp):
    circle_points = 0
    square_points = 0

    for i in range(INTERVAL**2):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        origin_distance = rand_x**2 + rand_y**2

        if origin_distance <= 1:
            circle_points += 1

        square_points += 1

    return round(4 * circle_points / square_points, dp)
