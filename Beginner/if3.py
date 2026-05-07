'''Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not. '''

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 

city1=input("Enter  1st city name : ")
city2=input("Enter 2nd city name : ")

def country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None
country1=country(city1)
country2=country(city2)

if country1 == country2 and country1 is not None:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")
