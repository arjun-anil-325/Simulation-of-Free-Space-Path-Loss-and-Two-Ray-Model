# 📡 Free Space vs Two-Ray Ground Reflection Path Loss Models

This project simulates and compares two fundamental wireless propagation models:

- **Free Space Path Loss (FSPL)**
- **Two-Ray Ground Reflection Model**

It visualizes how the received power changes with distance using both models and marks the **breakpoint distance**, beyond which two-ray behavior dominates.

---

## 📘 Theory Overview

### 1. Free Space Path Loss (FSPL)

The FSPL model assumes an ideal propagation environment with no obstacles, reflections, or scattering. It's used to estimate the received signal power over a line-of-sight (LOS) path.

#### **Formula:**

\[
L_{fs}(dB) = 20 \log_{10}(d) + 20 \log_{10}(f) - 147.55
\]

But in this program, we use the power-based form:

\[
P_r = P_t \cdot G_t \cdot G_r \cdot \left(\frac{\lambda}{4\pi d}\right)^2
\]

Where:
- \( P_r \): Received power (W)
- \( P_t \): Transmit power (W)
- \( G_t, G_r \): Antenna gains (unitless)
- \( \lambda = \frac{c}{f} \): Wavelength (m)
- \( d \): Distance between transmitter and receiver (m)

---

### 2. Two-Ray Ground Reflection Model

This model considers **both direct path** and **reflected path** off the ground, more accurately modeling real-world propagation, especially over longer distances.

#### **Formula:**

\[
P_r = \frac{P_t \cdot G_t \cdot G_r \cdot h_t^2 \cdot h_r^2}{d^4}
\]

Where:
- \( h_t, h_r \): Transmit and receive antenna heights (m)

This model is more accurate beyond a certain **breakpoint distance**.

---

### 3. Breakpoint Distance

This is the distance where FSPL transitions to the two-ray model.

\[
d_{break} = \frac{4 \cdot h_t \cdot h_r}{\lambda}
\]

After \( d_{break} \), the received power decreases much faster (∝ \(1/d^4\)) compared to FSPL (∝ \(1/d^2\)).

---

## 🧮 Simulation Parameters

| Parameter        | Value      |
|------------------|------------|
| Frequency        | 2.4 GHz    |
| Transmit Power   | 1 W        |
| Antenna Gains    | 1 (unitless) |
| Transmit Height  | 50 m       |
| Receive Height   | 2 m        |
| Distance Range   | 1 m – 5000 m |

---

## 📊 Output

The program plots:
- **FSPL** curve (blue, dashed)
- **Two-Ray** curve (red, solid)
- **Breakpoint distance** (green dotted line)

All on a **logarithmic scale** for clarity.

---

## 📂 How to Run

1. Ensure you have Python and the following libraries:
   - `numpy`
   - `matplotlib`

2. Run the script in any Python IDE or notebook.

---

## 🔍 Applications

- Wireless communication systems
- Signal coverage estimation
- Antenna design and placement
- Network simulation and planning (e.g., WiFi, 5G, IoT)

---

## 📈 Sample Output

![FSPL vs Two-Ray Model](fspl.png)


## 🤝 Contributing

Feel free to fork, improve the logic (e.g., include terrain/obstacle loss), or extend it for other propagation models.

