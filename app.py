from tkinter import *
import requests
import json

root = Tk()
root.title("Weath box")
root.geometry("400x40")

try:
    api_req = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=F033E0BC-B84D-4531-85E3-FDADCF359CCF")
    api = json.loads(api_req.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api="Error"
    print(api)

api_label = Label(root, text=city + "'s Air quality = " + str(quality) + " -> " + category, font=(20))
api_label.pack()


root.mainloop()