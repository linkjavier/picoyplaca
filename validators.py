from datetime import datetime


class Validator:
    
    """
    Validator Class to handle validations of values.
    
    """

    @staticmethod
    def __restrictedHours():
        """
        Method to GET the restricted hours as a Dictionary format. 
        M: Morning [Start , End]
        A: Afternoon [Start , End]
        :return: Dictionary of restricted hours
        """
        restrictedHours = {
            "M": ["7:00", "9:30"],  #Morning
            "A": ["16:00", "19:30"] #Afternoon
            }

        return restrictedHours

    @staticmethod
    def __restrictedPlates():
        """
        Method to GET restricted plates per day
        :return: Dictionary of restricted plates per day
        """
        PlateNumbersByDays = {
            1: [1, 2], #Monday
            2: [3, 4], #Tuesday
            3: [5, 6], #Wednesday
            4: [7, 8], #Thursday
            5: [9, 0], #Friday
            6: [],     #Saturday
            7: []      #Sunday
            }

        return PlateNumbersByDays

    @staticmethod
    def __getRestrictedHours(partOfDay):
        """
        Return the time restriction in time format
        :param partOfDay: Char parameter M: Morning, A: Afternoon
        :return: time interval in which the restriction holds
        """
        restrictedHours = Validator.__restrictedHours()
        startHour = restrictedHours[partOfDay][0]
        finishHour = restrictedHours[partOfDay][1]
        startHour = datetime.strptime(startHour, "%H:%M").time()
        finishHour = datetime.strptime(finishHour, "%H:%M").time()

        return startHour, finishHour

    @staticmethod
    def HourValidator(timeInput):
        """
        This method determines if the entered time is within the restricted time values.
        :param timeInput: time parameter as string
        :return: True or False
        """
        # ValidTime.validateTime(timeInput)
        time = datetime.strptime(timeInput, "%H:%M").time()
        morningStart, morningFinish = Validator.__getRestrictedHours("M")
        if morningStart <= time <= morningFinish:
            return True

        afternoonStart, afternoonFinish = Validator.__getRestrictedHours("A")
        if afternoonStart <= time <= afternoonFinish:
            return True

        return False

    @staticmethod
    def DateValidator(date, plate):
        """
        Method that checks if the plate is restricted by day.
        :param date: Date as string (Correct Format dd-mm-yyy)
        :param plate: plate number (Correct Format SSS-NNNN) S is a character. N is a number
        :return: True or False
        """

        day = datetime.strptime(date, '%d-%m-%Y').isoweekday()

        #If the Saturday(6) or Sunday(7) return False
        if day == 6 or day == 7:
            # Return False when the day is Saturday or Sunday
            return False

        else:
            lastChar = plate[-1]
            lastPlateNumber = int(lastChar)
            restrictedPlates = Validator.__restrictedPlates()
            RestrictedPlateNumbers = restrictedPlates[day]

            if lastPlateNumber == RestrictedPlateNumbers[0] or lastPlateNumber == RestrictedPlateNumbers[1]:
                #Return True when when the last number matches with restricted number
                return True

            else:
                return False
