class warShipsInSea:

    def __init__(self, battleShip = None):
         self._age = battleShip

    # getter method
    def get_battleShip(self):
        return self._battleShip

    # setter method
    def set_battleShip(self, x):
        self._battleShip = x


slagskib = [(1,0),(2,0),(3,0),(4,0),(5,0)]
"""ubåd =[(,),(,),(,),(,)]
destroyer1 =[(,),(,),(,)]
destroyer2 =[(),(),()]
torpedoBåd1[()]
torpedoBåd2[()]"""
northSea = warShipsInSea()

northSea.set_battleShip(slagskib)

print(northSea.get_battleShip())
