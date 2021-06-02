from carrier import *
from plane import *


def main():
    cargo = Cargo()
    passenger = Passenger()

    # Bridging Military and Cargo classes
    military1 = Military(cargo, 100)
    military1.display_description()
    military1.add_objects(25)
    military1.display_description()

    cargo = Cargo()
    passenger = Passenger()

    # Bridging Military and Passenger classes
    military2 = Military(passenger, 250)
    military2.display_description()
    military2.add_objects(10)
    military2.display_description()

    # Bridging Commercial and Passenger
    commercial1 = Commercial(passenger, 400)
    commercial1.display_description()
    commercial1.add_objects(50)
    commercial1.display_description()

    # Bridging Commercial and Cargo
    commercial2 = Commercial(cargo, 150)
    commercial2.display_description()
    commercial2.add_objects(15)
    commercial2.display_description()


if __name__ == "__main__":
    main()
