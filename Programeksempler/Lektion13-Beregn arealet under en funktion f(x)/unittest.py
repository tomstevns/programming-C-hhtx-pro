import unittest

from integration import AreaCalculationUnderCurve

integrator = AreaCalculationUnderCurve()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(15, integrator.integration(1,1,5,1,1))
        self.assertEqual(13.75, integrator(1, 2, 5, 1, 1))


if __name__ == '__main__':
    unittest.main()
