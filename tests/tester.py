from unittest import TestCase, main

from car import Car

class TestCar(TestCase):

    def setUp(self):
        self.car = Car("PCX-7521")


    # ==== CAR TESTING =================================

    def test_WeekendDrive(self):
        self.assertTrue(self.car.canDrive("25-06-2022", "8:30"))
        self.assertTrue(self.car.canDrive("25-06-2022", "8:30"))

    def test_canDrive_weekday_morning(self):
        self.assertTrue(self.car.canDrive("25-06-2022", "9:45"))

    def test_canDrive_weekday_afternoon(self):
        self.assertTrue(self.car.canDrive("25-06-2022", "15:00"))

    def test_canDrive_weekday(self):
        self.assertTrue(self.car.canDrive("25-06-2022", "9:45"))

    def test_cannotDrive_weekday_morning(self):
        self.assertFalse(self.car.canDrive("20-06-2022", "08:45"))

    def test_cannotDrive_weekday_afternoon(self):
        self.assertFalse(self.car.canDrive("20-06-2022", "18:00"))

    # ==== END CAR TESTING ======================================

if __name__ == "__main__":
    main()