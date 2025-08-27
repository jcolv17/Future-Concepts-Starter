# 20250827-004
import numpy as np

def kf_step(x, P, z, F, H, Q, R):
    x = F @ x
    P = F @ P @ F.T + Q
    y = z - H @ x
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    x = x + K @ y
    P = (np.eye(len(P)) - K @ H) @ P
    return x, P

def run_filter(n=20, dt=1.0):
    F = np.array([[1,0,dt,0],[0,1,0,dt],[0,0,1,0],[0,0,0,1]], dtype=float)
    H = np.array([[1,0,0,0],[0,1,0,0]], dtype=float)
    Q = np.eye(4)*0.01
    R = np.eye(2)*2.0
    x = np.array([0,0,1,1], dtype=float)
    P = np.eye(4)
    rng = np.random.default_rng(7)
    zs = [np.array([i + rng.normal(0,2), i + rng.normal(0,2)]) for i in range(n)]
    for z in zs:
        x, P = kf_step(x, P, z, F, H, Q, R)
    return x

if __name__ == "__main__":
    x = run_filter()
    print("final_state", np.round(x, 3).tolist())
