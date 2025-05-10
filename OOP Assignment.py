# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")

    def display_power(self):
        print(f"My superpower is: {self.power}")

# Inherited class
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def display_power(self):  # Polymorphism
        print(f"I can fly at {self.flight_speed} km/h with power: {self.power}")

# Another inherited class
class StrengthHero(Superhero):
    def __init__(self, name, power, city, lifting_capacity):
        super().__init__(name, power, city)
        self.lifting_capacity = lifting_capacity

    def display_power(self):  # Polymorphism
        print(f"I can lift {self.lifting_capacity} tons using my strength!")

# Instantiate objects
hero1 = FlyingHero("SkyFlash", "Flight", "Skyline City", 700)
hero2 = StrengthHero("IronBoulder", "Super Strength", "Rockville", 100)

# Demonstrate functionality
hero1.introduce()
hero1.display_power()
print()
hero2.introduce()
hero2.display_power()
