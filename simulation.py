import numpy as np
import matplotlib.pyplot as plt

def free_space_path_loss(d, f, Pt, Gt, Gr):
    """
    Compute the received power using Free Space Path Loss (FSPL) model.
    """
    c = 3e8  # Speed of light (m/s)
    lambda_ = c / f  # Wavelength (m)
    Lfs = (lambda_ / (4 * np.pi * d)) ** 2  # FSPL equation
    Pr = Pt * Gt * Gr * Lfs
    return np.maximum(Pr, 1e-30)  # Avoid log of zero

def two_ray_model(d, f, Pt, Gt, Gr, ht, hr):
    """
    Compute the received power using Two-Ray Ground Reflection model.
    """
    c = 3e8  # Speed of light (m/s)
    lambda_ = c / f  # Wavelength (m)
    d_break = (4 * ht * hr) / lambda_  # Breakpoint distance

    Pr_fspl = free_space_path_loss(d, f, Pt, Gt, Gr)
    Pr_tr = (Pt * Gt * Gr * (ht**2) * (hr**2)) / (d ** 4)

    return Pr_fspl, Pr_tr, d_break

# Simulation parameters
f = 2.4e9  # Frequency (2.4 GHz)
Pt = 1  # Transmitter power (1W)
Gt = 1  # Transmitter gain
Gr = 1  # Receiver gain
ht = 50  # Transmitter height (m)
hr = 2  # Receiver height (m)
d = np.linspace(1, 5000, 2000)  # Distance range (1m to 5000m)

# Compute received power for both models
Pr_fspl, Pr_tr, d_break = two_ray_model(d, f, Pt, Gt, Gr, ht, hr)

# Plot result in log scale
plt.figure(figsize=(10, 6))
plt.semilogy(d, Pr_fspl, label='Free Space Path Loss (FSPL)', color='blue', linestyle='--', linewidth=2)
plt.semilogy(d, Pr_tr, label='Two-Ray Model', color='red', linestyle='-', linewidth=2)
plt.axvline(x=d_break, color='g', linestyle='dotted', linewidth=2, label='Breakpoint Distance')
plt.xlabel('Distance (m)')
plt.ylabel('Received Power (W) [Log Scale]')
plt.title('Comparison of FSPL and Two-Ray Model with Breakpoint (Log Scale)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
