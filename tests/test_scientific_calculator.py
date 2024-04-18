import unittest,math
from typing import NoReturn

from src.scientific_calculator import Calculator
from src.custom_ex import IncorrectInputError, DivisionError


class CalculatorAddTestCase(unittest.TestCase):  # Test Case

    def test_add_3_corrrect_input(self) -> None | NoReturn:  # Unit
        # Arrange
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 8

        # Act
        result = calculator.add(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_no_args(self) -> None | NoReturn:
        # Arrange
        calculator = Calculator()
        expected_result = 0

        # Act
        result = calculator.add()

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_incorrect_input(self) -> NoReturn:
        # Arrange
        calculator = Calculator()
        x = "6"
        y = [4, 5]

        # Act/Assert
        with self.assertRaises(TypeError):
            calculator.add(x, y)

    def test_add_with_negative_numbers(self):
        calculator = Calculator()
        x = -4
        y = 3
        z = -1
        expected_result = -2

        result = calculator.add(x, y, z)

        self.assertEqual(result, expected_result)

    def test_add_with_float_numbers(self):
        calculator = Calculator()
        x = 1.5
        y = 2.5
        z = 3.5
        expected_result = 7.5

        result = calculator.add(x, y, z)

        self.assertAlmostEqual(result, expected_result, places=7)

    def test_add_with_mixed_types(self):
        calculator = Calculator()
        x = 4
        y = 3.5
        z = 1
        expected_result = 8.5

        # Act
        result = calculator.add(x, y, z)

        # Assert
        self.assertAlmostEqual(result, expected_result, places=7)


class CalculatorSubtractTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_subtract_with_correct_input(self):
        x = 10
        y = 3
        z = 2
        expected_result = 5

        result = self.calculator.subtract(x, y, z)

        self.assertEqual(result, expected_result)

    def test_subtract_with_incorrect_input(self):
        x = "10"
        y = [3, 2]

        with self.assertRaises(IncorrectInputError):
            self.calculator.subtract(x, y)

    def test_subtract_with_negative_numbers(self):
        x = -5
        y = -3
        z = -2
        expected_result = 0

        result = self.calculator.subtract(x, y, z)

        self.assertEqual(result, expected_result)

    def test_subtract_with_mixed_sign_numbers(self):
        x = 10
        y = -3
        z = 2
        expected_result = 11

        result = self.calculator.subtract(x, y, z)

        self.assertEqual(result, expected_result)

    def test_subtract_with_float_numbers(self):
        x = 10.5
        y = 3.5
        z = 2.5
        expected_result = 4.5

        result = self.calculator.subtract(x, y, z)

        self.assertAlmostEqual(result, expected_result, places=7)

    def tearDown(self):
        pass


class CalculatorMultTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_mult_with_correct_input(self):
        x = 1
        y = 2
        z = 3
        expected_result = 6

        result = self.calculator.multiply(x, y, z)

        self.assertEqual(result, expected_result)

    def test_mult_with_incorrect_input(self):
        x = []
        y = (1, 2)
        z = "4"

        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x, y, z)

    def test_mult_with_negative_numbers(self):
        x = -1
        y = 2
        z = -3
        expected_result = 6

        result = self.calculator.multiply(x, y, z)

        self.assertEqual(result, expected_result)

    def test_mult_with_float_numbers(self):
        x = 1.5
        y = 2.5
        z = 3.5
        expected_result = 13.125

        result = self.calculator.multiply(x, y, z)

        self.assertAlmostEqual(result, expected_result, places=7)

    def test_mult_with_mixed_types(self):
        x = 4
        y = 3.5
        z = 2
        expected_result = 28

        result = self.calculator.multiply(x, y, z)

        self.assertAlmostEqual(result, expected_result, places=7)


    def tearDown(self):
        pass


class CalculatorDivTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_div_with_correct_input(self):
        x = 4
        y = 2
        expected_result = 2
        result = self.calculator.divide(x,y)
        self.assertEqual(result, expected_result)

    def test_div_with_division_by_zero(self):
        x = 4
        y = 0

        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(x, y)

    def test_div_with_negative_numbers(self):
        x = -6
        y = 2
        expected_result = -3
        result = self.calculator.divide(x, y)
        self.assertEqual(result, expected_result)

    def test_div_with_float_numbers(self):
        x = 5.5
        y = 2.0
        expected_result = 2.75
        result = self.calculator.divide(x, y)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_div_with_mixed_types(self):
        x = 10
        y = 2.5
        expected_result = 4
        result = self.calculator.divide(x, y)
        self.assertEqual(result, expected_result)

    def test_div_with_incorrect_input(self):
        x = "10"
        y = [3, 2]

        with self.assertRaises(IncorrectInputError):
            self.calculator.divide(x, y)

    def tearDown(self):
        pass


class CalculatorSquareTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_square_with_positive_number(self):
        x = 5
        expected_result = 25
        result = self.calculator.square(x)
        self.assertEqual(result, expected_result)

    def test_square_with_negative_number(self):
        x = -5
        expected_result = 25
        result = self.calculator.square(x)
        self.assertEqual(result, expected_result)

    def test_square_with_zero(self):
        x = 0
        expected_result = 0
        result = self.calculator.square(x)
        self.assertEqual(result, expected_result)

    def tearDown(self):
        pass


class CalculatorCubeTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_cube_with_positive_number(self):
        x = 3
        expected_result = 27
        result = self.calculator.cube(x)
        self.assertEqual(result, expected_result)


    def test_cube_with_negative_number(self):
        x = -3
        expected_result = -27
        result = self.calculator.cube(x)
        self.assertEqual(result, expected_result)

    def test_cube_with_zero(self):
        x = 0
        expected_result = 0
        result = self.calculator.cube(x)
        self.assertEqual(result, expected_result)

    def tearDown(self):
        pass


class CalculatorSquareRootTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_square_root_with_positive_number(self):
        x = 25
        expected_result = 5
        result = self.calculator.square_root(x)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_square_root_with_zero(self):
        x = 0
        expected_result = 0
        result = self.calculator.square_root(x)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_square_root_with_decimal_number(self):
        x = 2.5
        expected_result = 1.5811388300841898
        result = self.calculator.square_root(x)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_square_root_with_negative_number(self):
        x = -25
        with self.assertRaises(ValueError):
            self.calculator.square_root(x)

    def tearDown(self):
        pass


class CalculatorNaturalLogarithmTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_natural_logarithm_with_positive_number(self):
        x = 10
        expected_result = 2.302585092994046
        result = self.calculator.natural_logarithm(x)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_natural_logarithm_with_decimal_number(self):
        x = 2.5
        expected_result = 0.9162907318741551
        result = self.calculator.natural_logarithm(x)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_natural_logarithm_with_zero(self):
        x = 0
        with self.assertRaises(ValueError):
            self.calculator.natural_logarithm(x)

    def test_natural_logarithm_with_negative_number(self):
        x = -10
        with self.assertRaises(ValueError):
            self.calculator.natural_logarithm(x)

    def tearDown(self):
        pass


class CalculatorSineTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_sine_with_degree(self):
        angle_degrees = 30
        expected_result = 0.5
        result = self.calculator.sine(angle_degrees)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_sine_with_radian(self):
        angle_radians = math.pi / 6
        expected_result = 0.5
        result = self.calculator.sine(math.degrees(angle_radians))
        self.assertAlmostEqual(result, expected_result, places=7)

    def tearDown(self):
        pass


class CalculatorCosineTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_cosine_with_degree(self):
        angle_degrees = 60
        expected_result = 0.5
        result = self.calculator.cosine(angle_degrees)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_cosine_with_radian(self):
        angle_radians = math.pi / 3
        expected_result = 0.5
        result = self.calculator.cosine(math.degrees(angle_radians))
        self.assertAlmostEqual(result, expected_result, places=7)

    def tearDown(self):
        pass


class CalculatorTangentTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_tangent_with_degree(self):
        angle_degrees = 45
        expected_result = 1.0
        result = self.calculator.tangent(angle_degrees)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_tangent_with_radian(self):
        angle_radians = math.pi / 4
        expected_result = 1.0
        result = self.calculator.tangent(math.degrees(angle_radians))
        self.assertAlmostEqual(result, expected_result, places=7)

    def tearDown(self):
        pass