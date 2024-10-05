import math

class RobotSpeed:
    def __init__(self, motor_rpm, gear_ratio, weight_pounds, radius, friction_coefficient=0.7):
        self.gear_ratio = gear_ratio
        self.weight = weight_pounds * 0.453592  # Convert pounds to kilograms
        self.radius = radius  
        self.friction_coefficient = friction_coefficient
        self.rpm = motor_rpm / gear_ratio  # Effective RPM at the wheels
    
    def LinearSpeed(self):
        circumference = 2 * math.pi * self.radius
        linear_speed = self.rpm * (circumference / 60)  # convert RPM to m/s
        return linear_speed

    def FrictionForce(self):
        return 0

    def CalculateSpeed(self):
        speed = self.LinearSpeed()
        friction_force = self.FrictionForce()
        speed_adjusted = speed - friction_force  # adjust speed for friction
        return speed_adjusted

weight_pounds = 119.5  
motor_rpm = 6000  
gear_ratio = 6.12  
wheel_radius = 0.10


robot = RobotSpeed(motor_rpm, gear_ratio, weight_pounds, wheel_radius)

linear_speed = robot.LinearSpeed()
friction_force = robot.FrictionForce()
adjusted_speed = robot.CalculateSpeed()

print(f"Initial Linear Speed: {linear_speed:.2f} m/s")
print(f"Friction Force: {friction_force:.2f} N")
print(f"Adjusted Speed: {adjusted_speed:.2f} m/s")
print(f"Adjusted Speed: {adjusted_speed*3.28:.2f} f/s")
