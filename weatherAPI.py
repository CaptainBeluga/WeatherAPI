import requests
import webbrowser
import time

activation = False

measure = ""
grades = ""

units = input("Measure Units (Metrics (M) or Imperial (I): ")

units = units.upper()

if(units == "M"):
    measure = "metric"
    grades = "°C"
    activation = True

elif(units == "I"):
    measure = "imperial"
    grades = "°F"
    activation = True

else:
    print("\nMeasure Unit doesn't exits")
    activation = False

print("\n")

if(activation == True):
    
    while True:
        
        city = input("City Name > ")

        APIkey = '540059f9666281dd3654669e964ffc54'    
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}&units={measure}"

        r = requests.get(link)
        r = r.json()

        try:
            
            cityBetterString = city[0].upper() + city[1:].lower()


            temp = r['main']['temp']
            print(f"\n\n------------------------------------------------\n\nTemperature in {cityBetterString} is : {round(temp,0)} {grades}\n\n------------------------------------------------\n\n")
            time.sleep(2)
            webbrowser.open(f"https://www.google.com/search?q={city.lower()}+weather")

        except KeyError:
            print("\nCity doesn't exist!\n\n\n")
