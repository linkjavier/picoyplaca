from validators import Validator

class Car:
    """ Car object """

    def __init__(self, plate):
        self.plate = plate

    def canDrive(self, date, hour):
        """ Method to return if a car with a certain license plate is on a restricted day and time to circulate. """

        if Validator.DateValidator(date, self.plate) and Validator.HourValidator(hour):
            print(f"The car cannot travel")
            return False
        else:
            print(f"The car can travel")
            return True