import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from model import tumor_model
from params import rS, rR, K

y0 = [9e5, 1e4]
t_span = (0, 200)
t_eval = np.linspace(0, 200, 1000)

sol = solve_ivp(
    tumor_model,
    t_span,
    y0,
    t_eval=t_eval,
    args=(rS, rR, K)
)

plt.plot(sol.t, sol.y[0], label="Sensitive")
plt.plot(sol.t, sol.y[1], label="Resistant")
plt.legend()
plt.show()
