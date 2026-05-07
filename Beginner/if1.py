#1. Write a program to determine the BMI Category based on user input. 

print("----BMI category determination-----")

height=float(input("Enter the height in meters: "))
weight=float(input("Enter the weight kilograms: "))

BMI = weight / (height)**2

if BMI>=30:
    print("Obesity")
elif BMI>=25:
    print("Overweight")
elif BMI>=18.5:
    print("Normal")
elif BMI<18.5:
    print("Underweight")


