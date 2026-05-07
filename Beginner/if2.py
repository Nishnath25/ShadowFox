'''2. Write a program to determine which country a city belongs to. Given
list of cities per country: 
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 
Ask the user to enter a city name and print the corresponding country'''

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 

city=input("Enter a city name to check whiich country it belongs to: ")

if city in Australia:
    print(f"{city} belongs to Australia")
elif city in UAE:
    print(f"{city} belongs to UAE")
elif city in India:
    print(f"{city} belongs to India")
else:
    print(" Not found ")