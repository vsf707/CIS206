# BMI calculator Program
# Conversion constants are written in uppercase as recommended by PEP 8
# BMI category ranges sourced from Wikipedia: Body Mass Index

POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

weight_pounds = float(input("Enter your weight in pounds: "))

height_feet = int(input("Enter your height in feet: "))
height_inches = int(input("Enter you height in inches: "))

total_height_inches = (height_feet * 12) + height_inches

weight_kg = weight_pounds * POUNDS_TO_KG
height_meters = total_height_inches * INCHES_TO_METERS

bmi = weight_kg / (height_meters ** 2)

print(f"\nYour BMI is: {bmi:.1f}")

print("\nBMI Categories:")
print("Underweight: Less than 18.5")
print("Normal weight is 18.5 - 24.9")
print("Overweight: 25.0 and above")
print("Source: https://en.wikipedia.org/wiki/Body_mass_index")
