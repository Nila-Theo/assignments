import math
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_single_peak(h, k, l, exp_2theta, lattice_parameter_a=4.0, wavelength_angstrom=1.5406):
    """Calculates Bragg peak values for a single custom input row."""
    hkl_sum = h**2 + k**2 + l**2
    if hkl_sum == 0:
        return None
        
    d_spacing = lattice_parameter_a / math.sqrt(hkl_sum)
    sin_theta = wavelength_angstrom / (2.0 * d_spacing)
    
    if -1.0 <= sin_theta <= 1.0:
        theta_rad = math.asin(sin_theta)
        calc_2theta = math.degrees(2.0 * theta_rad)
    else:
        calc_2theta = float('nan')
        
    diff = calc_2theta - exp_2theta
    
    return {
        "hkl": f"({h}{k}{l})",
        "d_spacing": round(d_spacing, 4),
        "calc_2theta": round(calc_2theta, 2),
        "exp_2theta": round(exp_2theta, 2),
        "diff": round(diff, 2)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    wavelength = 1.5406
    lattice_a = 4.0
    results = []
    
    if request.method == 'POST':
        # Get custom values submitted from the web form
        try:
            h = int(request.form.get('h'))
            k = int(request.form.get('k'))
            l = int(request.form.get('l'))
            exp_2theta = float(request.form.get('exp_2theta'))
            
            # Compute the peak data
            res = calculate_single_peak(h, k, l, exp_2theta, lattice_a, wavelength)
            if res:
                results.append(res)
        except ValueError:
            results = [{"error": "Invalid input. Please enter valid numbers for h, k, l, and 2theta."}]
            
    return render_template('index.html', results=results, lattice_a=lattice_a, wavelength=wavelength)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)