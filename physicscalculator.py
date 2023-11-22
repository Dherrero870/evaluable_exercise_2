import math

class PhysicsCalculator:
    def __init__(self):
        self.unit_system = None

    def set_unit_system(self):
        while True:
            system = input("Choose unit system (SI or US): ").upper()
            if system in ["SI", "US"]:
                self.unit_system = system
                break
            else:
                print("Invalid input. Please enter SI or US.")

    def get_input(self, prompt, unit=""):
        while True:
            try:
                value = float(input(prompt))
                return value if self.unit_system == "SI" else self.convert_units(value, unit)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def convert_units(self, value, unit):
        # Add unit conversion logic here
        # For simplicity, this example assumes SI and US units are the same
        return value

    def kinematic_equation(self):
        print("\nKinematic Equation: v = u + at")
        u = self.get_input("Enter initial velocity (m/s or ft/s): ", "m/s")
        a = self.get_input("Enter acceleration (m/s^2 or ft/s^2): ", "m/s^2")
        t = self.get_input("Enter time (s): ")
        v = u + a * t
        print(f"Final velocity: {v:.2f} {'' if self.unit_system == 'SI' else 'ft/s'}")

    def gravitational_force(self):
        print("\nGravitational Force: F = G * (m1 * m2) / r^2")
        G = 6.67430e-11  # gravitational constant
        m1 = self.get_input("Enter mass of object 1 (kg or lb): ", "kg")
        m2 = self.get_input("Enter mass of object 2 (kg or lb): ", "kg")
        r = self.get_input("Enter separation distance (m or ft): ", "m")
        force = G * (m1 * m2) / r ** 2
        print(f"Gravitational force: {force:.2e} N {'' if self.unit_system == 'SI' else 'lb'}")

def main():
    calculator = PhysicsCalculator()

    while True:
        calculator.set_unit_system()

        print("\nChoose a physics calculation:")
        print("1. Kinematic Equation")
        print("2. Gravitational Force")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            calculator.kinematic_equation()
        elif choice == "2":
            calculator.gravitational_force()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()