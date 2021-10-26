import unittest

import Afleveringsopgave2




class TestTheExercisesForAfleveringsopgave1(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_gangTalMed7(self):
        #tester om 7*10 = 70
        self.assertEqual(Afleveringsopgave2.gangTalMed7(10),70)
        #Tester randværdier
        self.assertEqual(Afleveringsopgave2.gangTalMed7(1),7)
        self.assertEqual(Afleveringsopgave2.gangTalMed7(-1),-7)
        #Tester reelle tal
        self.assertEqual(Afleveringsopgave2.gangTalMed7(2.25),15.75)
        #Tester at strenge ikke kan håndteres
        self.assertNotEqual(Afleveringsopgave2.gangTalMed7("10"),70)



if __name__ == '__main__':
    unittest.main()
