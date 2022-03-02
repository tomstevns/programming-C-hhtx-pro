import unittest
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

import eksamensopgave



class TestsForEksamensopgave(unittest.TestCase):

    aFile = "100records.csv"
    stdDevFile = "stdDevFile.txt"
    nostdDevFile = "no_stdDevFile.txt"

    def test_gangTalMed7(self):
        #tester om 7*10 = 70
        self.assertNotEqual(eksamensopgave.gangTalMed7(10),71)
        #Tester randværdier
        self.assertEqual(eksamensopgave.gangTalMed7(1),7)
        self.assertEqual(eksamensopgave.gangTalMed7(-1),-7)
        #Tester reelle tal
        self.assertEqual(eksamensopgave.gangTalMed7(2.25),15.75)
        #Tester at strenge ikke kan håndteres
        self.assertNotEqual(eksamensopgave.gangTalMed7("10"),70)

    def test_stddev(self):
        A = np.array([170,175,175,180,180,180,180,185,185,190])

        self.assertEqual(eksamensopgave.stddev(A),5.477225575051661)
        self.assertNotEqual(eksamensopgave.stddev(A),5.477225575051662)

    def test_getIdFromRecords(self):
        self.__class__(FileNotFoundError,eksamensopgave.getIdFromRecords("noexistfile"))


if __name__ == '__main__':
    unittest.main()

