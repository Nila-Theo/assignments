import math
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PXRD Bragg Calculator - Day 4</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f8; color: #333; }
        h1 { color: #2c3e50; }
        .meta { margin-bottom: 20px; font-style: italic; color: #555; }
        form { background: #fff; padding: 20px; margin-bottom: 20px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .form-group { display: inline-block; margin-right: 15px; margin-bottom: 10px; }
        label { display: block; font-weight: bold; margin-bottom: 5px; font-size: 14px; }
        input { padding: 8px; width: 80px; border: 1px solid #ddd; border-radius: 4px; }
        button { padding: 10px 20px; background-color: #34495e; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #2c3e50; }
        table { border-collapse: collapse; width: 100%; background: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        th, td { border: 1px solid #ddd; padding: 12px 16px; text-align: center; }
        th { background-color: #34495e; color: white; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .error { color: #c0392b; font-weight: bold; }
    </style>
</head>
<body>
    <h1>p-XRD Bragg Peak Analysis</h1>
    <div class="meta">
        Lattice Parameter a: {{ lattice_a }} Å | X-ray Wavelength: {{ wavelength }} Å
    </div>
    <form method="POST">
        <div class="form-group">
            <label for="h">h:</label>
            <input type="number" id="h" name="h" required value="1">
        </div>
        <div class="form-group">
            <label for="k">k:</label>
            <input type="number" id="k" name="k" required value="0">
        </div>
        <div class="form-group">
            <label for="l">l:</label>
            <input type="number" id="l" name="l" required value="0">
        </div>
        <div class="form-group">
            <label for="exp_2theta">Exp 2&theta;:</label>
            <input type="number" step="any" id="exp_2theta" name="exp_2theta" required value="22.18">
        </div>
        <div style="margin-top: 10px;">
            <button type="submit">Calculate Peak</button>
        </div>
    </form>
    <table>
        <thead>
            <tr>
                <th>hkl</th>
                <th>d-spacing (Å)</th>
                <th>Calc 2&theta; (deg)</th>
                <th>Exp 2&theta; (deg)</th>
                <th>Diff (deg)</th>
            </tr>
        </thead>
        <tbody>
            {% if results %}
                {% for row in results %}
                    {% if row.error %}
                    <tr><td colspan="5" class="error">{{ row.error }}</td></tr>
                    {% else %}
                    <tr>
                        <td><strong>{{ row.hkl }}</strong></td>
                        <td>{{ row.d_spacing }}</td>
                        <td>{{ row.calc_2theta }}</td>
                        <td>{{ row.exp_2theta }}</td>
                        <td>{{ row.diff }}</td>
                    </tr>
                    {% endif %}
                {% endfor %}
            {% else %}
                <tr><td colspan="5">Enter custom parameters above and click "Calculate Peak".</td></tr>
            {% endif %}
        </tbody>
    </table>
</body>
</html>
"""

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
        try:
            h = int(request.form.get('h'))
            k = int(request.form.get('k'))
            l = int(request.form.get('l'))
            exp_2theta = float(request.form.get('exp_2theta'))
            
            res = calculate_single_peak(h, k, l, exp_2theta, lattice_a, wavelength)
            if res:
                results.append(res)
        except ValueError:
            results = [{"error": "Invalid input. Please enter valid numbers."}]
            
    return render_template_string(
        HTML_TEMPLATE,
        results=results,
        lattice_a=lattice_a,
        wavelength=wavelength,
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)