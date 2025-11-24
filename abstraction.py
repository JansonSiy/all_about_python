# Why this is Abstraction?
# The user doesn’t need to know the internal process.
# They just call one method: make_coffee().
# Internal complexity is hidden and encapsulated within the class methods.

from abc import ABC, abstractmethod

# Abstract class
class CoffeeMachine(ABC):
    @abstractmethod
    def make_coffee(self):
        pass

# Subclass for Espresso
class EspressoMachine(CoffeeMachine):
    def make_coffee(self):
        # Internal processing hidden from the user
        self._grind_beans()
        self._heat_water()
        self._brew()
        return "Espresso is ready!"

    # These are private internal methods
    def _grind_beans(self):
        print("Grinding coffee beans...")

    def _heat_water(self):
        print("Heating water...")

    def _brew(self):
        print("Brewing the coffee...")

# Subclass for Latte
class LatteMachine(CoffeeMachine):
    def make_coffee(self):
        self._grind_beans()
        self._heat_water()
        self._brew()
        self._add_milk()
        return "Latte is ready!"

    def _grind_beans(self):
        print("Grinding coffee beans...")

    def _heat_water(self):
        print("Heating water...")

    def _brew(self):
        print("Brewing the coffee...")

    def _add_milk(self):
        print("Adding milk to coffee...")

# Using abstraction: user only interacts with make_coffee()
def order_coffee(machine: CoffeeMachine):
    print(machine.make_coffee())

# Example usage
order_coffee(EspressoMachine())
order_coffee(LatteMachine())    
