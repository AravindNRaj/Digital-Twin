def tumor_model(t, y, rS, rR, K):
    S, R = y
    dSdt = rS * S * (1 - (S + R) / K)
    dRdt = rR * R * (1 - (S + R) / K)
    return [dSdt, dRdt]
