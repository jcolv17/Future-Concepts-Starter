# 20250827-004
import math
import random

def simulate(steps=200, gps_dropout_every=10, process_noise=0.1):
    x, y = 0.0, 0.0
    vx, vy = 1.0, 0.8
    est_x, est_y = 0.0, 0.0
    for t in range(steps):
        x += vx + random.gauss(0, process_noise)
        y += vy + random.gauss(0, process_noise)
        est_x += vx
        est_y += vy
        if t % gps_dropout_every == 0 and t != 0:
            est_x = 0.8*est_x + 0.2*x
            est_y = 0.8*est_y + 0.2*y
    return (x - est_x)**2 + (y - est_y)**2

if __name__ == "__main__":
    err2 = simulate()
    print("final_position_error_sq", round(err2, 2))
