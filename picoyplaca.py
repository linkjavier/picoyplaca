from car import Car

""" Pico y Placa predictor """


if __name__ == "__main__":

    plate = input("Enter plate number: ")
    date = input("Enter date in this format(Day-Month-Year): ")
    hour = input("Enter hour in this format(Hour:Minute): ")
    car = Car(plate)
    car.canDrive(date, hour)
