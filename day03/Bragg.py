import math
import os

def calculate_bragg_peaks(csv_filename, lattice_parameter_a, wavelength_angstrom):
    print(f"{'hkl':<8} {'d-spacing (A)':<15} {'Calc 2theta (deg)':<15} {'Exp 2theta (deg)':<15} {'Diff (deg)':<10}")
    print("-" * 65)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, csv_filename)
    
    with open(full_path, mode='r', encoding='utf-8-sig') as file:
        lines = file.readlines()
        
    row_count = 0
    for idx, line in enumerate(lines):
        line_clean = line.strip()
        
        # Skip truly empty lines
        if not line_clean:
            continue
            
        # Skip the header row explicitly by checking if it starts with 'h'
        if idx == 0 or line_clean.lower().startswith('h'):
            print(f"Skipping header line: {line_clean}")
            continue
            
        parts = [p.strip() for p in line_clean.split(',')]
        if len(parts) < 4:
            print(f"Skipping line {idx+1} (not enough parts): {parts}")
            continue
            
        try:
            h = int(parts[0])
            k = int(parts[1])
            l = int(parts[2])
            exp_2theta = float(parts[3])
        except ValueError as e:
            print(f"Skipping line {idx+1} (conversion failed for '{line_clean}'): {e}")
            continue
            
        row_count += 1
        hkl_sum = h**2 + k**2 + l**2
        if hkl_sum == 0:
            continue
            
        d_spacing = lattice_parameter_a / math.sqrt(hkl_sum)
        sin_theta = wavelength_angstrom / (2.0 * d_spacing)
        
        if -1.0 <= sin_theta <= 1.0:
            theta_rad = math.asin(sin_theta)
            calc_2theta = math.degrees(2.0 * theta_rad)
        else:
            calc_2theta = float('nan')
            
        diff = calc_2theta - exp_2theta
        print(f"({h}{k}{l})   {d_spacing:<15.4f} {calc_2theta:<15.2f} {exp_2theta:<15.2f} {diff:<+10.2f}")
        
    print(f"\nSuccessfully processed {row_count} data rows.")

if __name__ == "__main__":
    WAVELENGTH = 1.5406  # angstrom
    LATTICE_A = 4.0      # angstrom
    DATA_FILE = "diffraction_data.csv"
    
    print(f"Running PXRD Analysis for Cubic Lattice (a = {LATTICE_A} A, wavelength = {WAVELENGTH} A)\n")
    calculate_bragg_peaks(DATA_FILE, LATTICE_A, WAVELENGTH)