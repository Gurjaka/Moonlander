import matplotlib.pyplot as plt

class Lander:
    def __init__(self, gravity, thrust, fuel_consumption, delta_time):
        self.gravity = gravity
        self.thrust = thrust
        self.fuel_consumption = fuel_consumption
        self.delta_time = delta_time

        # Initial state
        self.altitude = 1000.0  # Starting altitude
        self.velocity = 0.0      # Initial velocity
        self.fuel = 100          # Initial fuel
        self.is_landed = False    # Status flag
        self.time_elapsed = 0.0   # Total time elapsed

    def apply_gravity(self):
        """Apply gravity to the lander's velocity."""
        self.velocity += self.gravity * self.delta_time

    def apply_thrust(self):
        """Apply thrust to the lander's velocity if there is fuel."""
        if self.fuel > 0:
            self.velocity -= self.thrust * self.delta_time
            self.fuel -= self.fuel_consumption * self.delta_time

    def update_position(self):
        """Update the lander's altitude based on its velocity."""
        self.altitude += self.velocity * self.delta_time
        if self.altitude <= 0:
            self.altitude = 0
            self.is_landed = True  # Mark as landed if altitude is 0

    def update(self, thrusting):
        """Update the lander's state based on thrusting status."""
        self.apply_gravity()
        if thrusting:
            self.apply_thrust()
        self.update_position()
        self.time_elapsed += self.delta_time


class Trajectory:
    def __init__(self):
        # Store the trajectory of altitude and velocity over time
        self.time = []
        self.altitudes = []
        self.velocities = []

    def record(self, time, altitude, velocity):
        """Record the current state of the lander."""
        self.time.append(time)
        self.altitudes.append(altitude)
        self.velocities.append(velocity)


class Simulation:
    def __init__(self, gravity, thrust, fuel_consumption, delta_time):
        self.lander = Lander(gravity, thrust, fuel_consumption, delta_time)
        self.trajectory = Trajectory()

    def run(self):
        """Run the simulation until the lander has landed."""
        while not self.lander.is_landed:
            thrusting = self.lander.fuel > 0 and self.lander.altitude > 100
            self.lander.update(thrusting)
            self.trajectory.record(self.lander.time_elapsed, self.lander.altitude, self.lander.velocity)

    def plot_results(self):
        """Plot the results of the simulation."""
        fig, axs = plt.subplots(2, 1, figsize=(8, 10))

        # Plot altitude vs. time
        axs[0].plot(self.trajectory.time, self.trajectory.altitudes, label="Altitude (m)")
        axs[0].set_title("Lander Altitude Over Time")
        axs[0].set_xlabel("Time (s)")
        axs[0].set_ylabel("Altitude (m)")
        axs[0].legend()

        # Plot velocity vs. time
        axs[1].plot(self.trajectory.time, self.trajectory.velocities, label="Velocity (m/s)", color="orange")
        axs[1].set_title("Lander Velocity Over Time")
        axs[1].set_xlabel("Time (s)")
        axs[1].set_ylabel("Velocity (m/s)")
        axs[1].legend()

        plt.tight_layout()
        plt.show()

    def print_results(self):
        """Print the total time taken for the landing."""
        print(f"Total time to land: {self.lander.time_elapsed:.2f} seconds")


def get_float_input(prompt):
    """Helper function to get a float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Get user inputs for simulation parameters
    gravity = get_float_input("Enter gravity (m/s^2 (1.62 for the Moon): ")
    thrust = get_float_input("Enter thrust (N): ")
    fuel_consumption = get_float_input("Enter fuel consumption rate (units/time): ")
    delta_time = 0.1

    # Initialize and run the simulation
    simulation = Simulation(gravity, thrust, fuel_consumption, delta_time)
    simulation.run()
    simulation.plot_results()
    simulation.print_results()

if __name__ == "__main__":
    main()
