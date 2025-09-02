import math
import csv

# --- Constants ---
g = 9.81        # m/s^2, gravity
rho = 1000      # kg/m^3, density of water

# --- System parameters (change these as needed) ---
D = 0.05        # pipe diameter (m)
L = 804.672        # pipe length (m)
Ar = 2.0        # reservoir cross-sectional area (m^2)
Hr0 = 3.0       # initial water height in reservoir (m)
Cd = 0.65       # discharge coefficient
Av_max = 0.002  # max valve area (m^2)
alpha = 0.5     # valve opening (0 to 1)
f = 0.02        # Darcy friction factor

# --- Time step settings ---
dt = 0.5        # seconds per step
T_max = 300     # max simulation time (s)

# --- Derived values ---
Ap = math.pi * (D**2) / 4.0
V_pipe = Ap * L
Av = alpha * Av_max

# --- Function to compute flow with friction ---
def compute_flow(Hr, Ap, Av, Cd, f, L, D):
    if Hr <= 0:
        return 0.0
    Q = Cd * Av * math.sqrt(2 * g * Hr)  # initial guess
    for _ in range(10):  # iterate for head loss correction
        v = Q / Ap if Ap > 0 else 0
        h_loss = f * (L / D) * (v**2) / (2 * g)
        deltaH = max(Hr - h_loss, 0)
        Q = Cd * Av * math.sqrt(2 * g * deltaH)
    return Q

# --- Simulation loop ---
time = 0.0
Hr = Hr0
Vr = Hr * Ar   # initial volume
cumulative_water = 0.0  # m^3 delivered
results = []

while time <= T_max and Hr > 0:
    Q = compute_flow(Hr, Ap, Av, Cd, f, L, D)  # m^3/s
    v = Q / Ap if Ap > 0 else 0
    purge_time = V_pipe / Q if Q > 0 else float("inf")

    # Update reservoir and cumulative delivered
    delivered = Q * dt        # m^3 this step
    cumulative_water += delivered
    Vr -= delivered
    Hr = max(Vr / Ar, 0)

    # Store results (convert flow to L/s, cumulative to liters)
    results.append([time, Hr, Q*1000, v, purge_time, cumulative_water*1000])

    # Step forward in time
    time += dt

# --- Save to CSV file ---
with open("irrigation_simulation.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Time (s)",
        "Reservoir Height (m)",
        "Flow Rate (L/s)",
        "Velocity (m/s)",
        "Purge Time (s)",
        "Cumulative Delivered (L)"
    ])
    writer.writerows(results)

print("Simulation complete. Results saved to irrigation_simulation.csv")
