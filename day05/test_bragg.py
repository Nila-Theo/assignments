import math
import pytest
from Bragg import calculate_single_peak


def test_calculate_single_peak_standard():
    # For a = 4.0 Å, (h, k, l) = (1, 0, 0) -> d = 4.0 Å
    # With wavelength = 1.5406 Å -> 2theta ≈ 22.21°
    result = calculate_single_peak(h=1, k=0, l=0, exp_2theta=22.00)

    assert result is not None
    assert result["hkl"] == "(100)"
    assert result["d_spacing"] == 4.0
    assert result["calc_2theta"] == 22.21
    assert result["exp_2theta"] == 22.0
    assert result["diff"] == 0.21


def test_calculate_single_peak_111():
    # For a = 4.0 Å, (h, k, l) = (1, 1, 1) -> d = 4.0 / sqrt(3) ≈ 2.3094 Å
    # With wavelength = 1.5406 Å -> 2theta ≈ 38.97°
    result = calculate_single_peak(h=1, k=1, l=1, exp_2theta=39.00)

    assert result["hkl"] == "(111)"
    assert result["d_spacing"] == 2.3094
    assert result["calc_2theta"] == 38.97
    assert result["diff"] == -0.03


def test_second_order_reflection_200():
    # Higher-order periodicity: n = 2 on (100) is equivalent to n = 1 on (200)
    # For a = 4.0 Å, (h, k, l) = (2, 0, 0) -> d = 2.0 Å, 2theta ≈ 45.31°
    result = calculate_single_peak(h=2, k=0, l=0, exp_2theta=45.30)

    assert result is not None
    assert result["hkl"] == "(200)"
    assert result["d_spacing"] == 2.0
    assert result["calc_2theta"] == 45.31
    assert result["diff"] == 0.01


def test_zero_miller_indices_returns_none():
    # (0, 0, 0) should return None to avoid division by zero
    result = calculate_single_peak(h=0, k=0, l=0, exp_2theta=20.0)
    assert result is None


def test_unphysical_reflection_returns_nan():
    # When wavelength > 2 * d_spacing (sin_theta > 1), calc_2theta should be NaN
    result = calculate_single_peak(
        h=1, k=0, l=0, exp_2theta=10.0, lattice_parameter_a=1.0, wavelength_angstrom=3.0
    )

    assert result is not None
    assert math.isnan(result["calc_2theta"])
    assert math.isnan(result["diff"])