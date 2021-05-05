from two_column_text_read_int import two_column_text_read
from quadratic_fit_int import quadratic_fit
from fit_curve_array import fit_curve_array

array = two_column_text_read("volumes_energies.dat")

print(fit_curve_array(quadratic_fit(array), 0, 10))
