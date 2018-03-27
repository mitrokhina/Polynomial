import unittest

from Polinomial import Polynomial

class TestPolynomial(unittest.TestCase):

    def test_init_correct_int_coeff(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coeffs, [1, 2, 3])
        self.assertEqual(p.degree, 2)

    def test_init_correct_float_coeff(self):
        p = Polynomial([1.0, 2.5, 3.0, 4.0])
        self.assertEqual(p.coeffs, [1.0, 2.5, 3.0, 4.0])
        self.assertEqual(p.degree, 3)

    def test_init_zero_list_coeffs(self):
        p = Polynomial([0, 0, 0])
        self.assertEqual(p.coeffs, [0])
        self.assertEqual(p.degree, 0)

    def test_init_empty_list(self):
        self.assertRaises(TypeError, Polynomial, [])

    def test_init_no_list(self):
        self.assertRaises(TypeError, Polynomial, "0")

    def test_init_incorrect_list(self):
        self.assertRaises(TypeError, Polynomial, ["g", 1])

    def test_init_major_coeffs_is_zero(self):
        p = Polynomial([0, 0, 1, 2])
        self.assertEqual(p.coeffs, [1, 2])
        self.assertEqual(p.degree, 1)

    def test_init_polynomial_with_zero_degree(self):
        p = Polynomial([0, 0, 1])
        self.assertEqual(p.coeffs, [1])
        self.assertEqual(p.degree, 0)

    def test_eq_true(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        self.assertTrue(p1 == p2)

    def test_eq_false(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 3])
        self.assertFalse(p1 == p2)

    def test_eq_constant(self):
        p1 = Polynomial([5])
        p2 = 5
        self.assertTrue(p1 == p2)

    def test_eq_to_string(self):
        p1 = Polynomial([2, 0, 0])
        self.assertRaises(TypeError, p1.__eq__, "2")

    def test_add_same_polyn_size(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [2, 4])
        self.assertEqual(p3.degree, 1)

    def test_add_different_polyn_size(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3, 5])
        self.assertEqual(p3.degree, 2)

    def test_add_negative_coeffs(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([-1, 1])
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_add_zero_values(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([0, 0])
        p3 = p1 + p2
        self.assertEqual(p3, p1)
        self.assertEqual(p3.degree, 2)

    def test_add_positive_constant_float(self):
        p1 = Polynomial([1, 2])
        p2 = 1.7
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 3.7])
        self.assertEqual(p3.degree, 1)

    def test_add_negative_constant_int(self):
        p1 = Polynomial([1, 2])
        p2 = -1
        p3 = p1 + p2
        self.assertEqual(p3.coeffs, [1, 1])
        self.assertEqual(p3.degree, 1)

    def test_mul_same_polyn_size(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 1])
        self.assertEqual(p3.degree, 2)

    def test_mul_different_polynom_size(self):
        p1 = Polynomial([1, 1])
        p2 = Polynomial([1, 1, 1])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1, 2, 2, 1])
        self.assertEqual(p3.degree, 3)

    def test_mul_zero_polynom(self):
        p1 = Polynomial([0, 1, 0])
        p2 = Polynomial([0, 0])
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_mul_zero_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 0
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [0])
        self.assertEqual(p3.degree, 0)

    def test_mul_float_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 1.4
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [1.4, 2.8])
        self.assertEqual(p3.degree, 1)

    def test_mul_int_constant(self):
        p1 = Polynomial([1, 2])
        p2 = 4
        p3 = p1 * p2
        self.assertEqual(p3.coeffs, [4, 8])
        self.assertEqual(p3.degree, 1)

    def test_mul_incorrect_constant(self):
        p1 = Polynomial([1, 2])
        self.assertRaises(TypeError, p1.__mul__, "5")

    def test_string_type_of_coeffs(self):
        self.assertRaises(TypeError, Polynomial, ["aaa", "bb"])

    def test_str_one_coeff(self):
        p1 = Polynomial([5])
        self.assertEqual(str(p1), '5')

    def test_str_one_coeff_begin_with_zero(self):
        p1 = Polynomial([0, -3])
        self.assertEqual(str(p1), '-3')

    def test_str_zero_coeffs_int(self):
        p1 = Polynomial([0, 0, 0])
        self.assertEqual(str(p1), '0')

    def test_str_zero_coeffs_float(self):
        p1 = Polynomial([0.0, 0.0, 0.0])
        self.assertEqual(str(p1), '0.0')

    def test_str_first_coeff_is_zero(self):
        p1 = Polynomial([0, 2, 3, 1])
        self.assertEqual(str(p1), '2x2+3x+1')

    def test_str_each_coeff_is_one(self):
        p1 = Polynomial([-1, 1, 1])
        self.assertEqual(str(p1), '-x2+x+1')

    def test_str_second_coef_is_minus_one(self):
        p1 = Polynomial([0, -1, 0])
        self.assertEqual(str(p1), '-x')

if __name__ == "__main__":
    unittest.main()