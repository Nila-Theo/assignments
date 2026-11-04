# Day 3 Assignment: Powder X-Ray Diffraction (p-XRD) Bragg Peak Calculator

## Overview
This script computes the theoretical interplanar spacings ($d$-spacings) and Bragg diffraction angles ($2\theta$) for a cubic crystal lattice and compares them against experimental diffraction data loaded from a CSV file.

## Files Included
* **`Bragg.py`**: The core Python script containing functions to parse the dataset, compute crystallographic parameters via Bragg's Law, and output a formatted comparison table.
* **`diffraction_data.csv`**: A structured comma-separated data file containing Miller indices ($h, k, l$) and experimental $2\theta$ diffraction angles.

## Scientific Computations Performed
1. **Interplanar Spacing ($d$):** Calculates the $d$-spacing for a cubic crystal system given lattice parameter $a$:
   $$d = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

22. **Bragg's Law & Detector Angles ($2\theta$):** Computes the theoretical diffraction peak positions using copper $K\alpha$ radiation wavelength ($\lambda = 1.5406$ Å): 
   $$\sin\theta = \frac{\lambda}{2d}$$
   $$2\theta_{\text{calc}} = 2 \times \arcsin(\sin\theta)$$

3. **Error Analysis:** Computes the residual difference ($\Delta 2\theta = 2\theta_{\text{calc}} - 2\theta_{\text{exp}}$) to evaluate the match between theoretical model predictions and experimental observations.

## How to Run
Navigate to the `day03` folder in your terminal and execute:
```bash
python3 Bragg.py