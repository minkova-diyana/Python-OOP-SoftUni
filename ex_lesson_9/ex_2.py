def even_parameters(function):
    def wrapper(*args, **kwargs):
        for el in args:
            if isinstance(el, int) and el % 2 == 0:
                continue
            else:
                return 'Please use only even numbers!'

        result = function(*args, **kwargs)
        return result
    return wrapper




import unittest


class EvenParametersTests(unittest.TestCase):
    def test_even(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 4, 4)
        self.assertEqual(result, 12)

    def test_odd(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, 5, 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_non_integer_params(self):
        @even_parameters
        def func(*args):
            return sum(args)

        result = func(4, "4", 4)
        self.assertEqual(result, "Please use only even numbers!")

    def test_with_no_params(self):
        @even_parameters
        def func():
            return "hi"

        result = func()
        self.assertEqual(result, "hi")


if __name__ == '__main__':
    unittest.main()
