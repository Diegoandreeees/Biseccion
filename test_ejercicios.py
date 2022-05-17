import math
from unittest import TestCase

# INCLUIR ABAJO SU IMPORT

from diego_diaz_biseccion import biseccion as diego_diaz_biseccion

class TestEjercicios(TestCase):

    def setUpClass(self):
        self.fx = lambda x: (x - 2)**2 - math.log(x)
        self.inter = (1, 2)
        self.er = 0.02
        self.n = 50


if __name__ == "__main__":
    # Testing.
    pass
