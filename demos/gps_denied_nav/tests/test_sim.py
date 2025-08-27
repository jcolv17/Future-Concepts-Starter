# 20250827-004
from sim import simulate

def test_error_reasonable():
    err2 = simulate(steps=100, gps_dropout_every=10, process_noise=0.05)
    assert err2 < 2500.0
