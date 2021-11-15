from tkinter import *
import requests
import json

root = Tk()
root.title("Weath box")
root.geometry("355x19")

try:
    api_req = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=96122&distance=25&API_KEY=F033E0BC-B84D-4531-85E3-FDADCF359CCF")
    api = json.loads(api_req.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_colour = "green"
    elif category == "Moderate":
        weather_colour="Yellow"
    elif category == "Unhealthy for sensitive groups":
        weather_colour="Orange"
    elif category == "Unhealthy":
        weather_colour="Red"
    elif category == "Hazardous":
        weather_colour="Maroon"
    
    root.configure(bg="Purple")

    api_label = Label(root, text=city + "'s Air quality = " + str(quality) + " -> " + category, font=(20),bg=weather_colour)  
    api_label.pack()

except Exception as e:
    api="Error"
    print(api)


root.mainloop()