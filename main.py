from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title('Air quality wather app')
root.iconbitmap('./img/weather.ico')
root.geometry('400x100')

# Create command function

def zipLookup ():
    # zip.get()
    # zipLabel = Label(root, text=zip.get())
    # zipLabel.grid(row=1, column=0, columnspan=2)

    try:
        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+zip.get()+'&distance=5&API_KEY=A640CE5B-6081-4F21-9AC6-86EDA3C78972')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        
        if category == 'Good':
            weather_color = '#0C0'
        elif category == 'Moderate':
            weather_color = 'FFFF00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = ''
        elif category == 'ff9900':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'


        root.configure(background=weather_color)
        myLabel = Label(root, text= city + ' Air Quality ' + str(quality) + ' ' + category, font=('Helvetica', 15), background=weather_color )
        myLabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = 'Error....' 

zip = Entry(root)
zip.grid(row=0, column=0, sticky= W+E+N+S)
zipButton = Button(root, text='Lookup Zipcode', command=zipLookup)
zipButton.grid(row=0, column=1, sticky= W+E+N+S)




root.mainloop()