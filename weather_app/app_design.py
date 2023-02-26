from tkinter import *
import sys
sys.path.append("..")
from weather import retrieve_recent_data, return_forecast
from PIL import Image, ImageTk
import requests
from io import BytesIO

''' This is UI part'''

def get_data():
    '''
    get data from apis
    '''
    city_name = entry_enter_city.get()
    recent_data = retrieve_recent_data(city_name)
    forecast_data = return_forecast(city_name)
    update_entries_text(recent_data, forecast_data)

def get_image(icon):
    '''get icons'''
    url = 'http://openweathermap.org/img/wn/' + icon + '@2x.png'
    response = requests.get(url, 'icon.png')
    image_bytes = BytesIO(response.content)
    image = Image.open(image_bytes)
    image = ImageTk.PhotoImage(image)
    print(image)
    return image

def update_entries_text(recent_data, forecast_data):
    '''Clean entry fields before receiving new data.
    Getting needed fields of data from recent data and forecast data, received from the function above.
    Updating entries  with needed data and updating icons.
    '''
    entry_temperature.delete(0, END)
    entry_feels_like_now.delete(0, END)
    entry_temperature_day.delete(0, END)
    entry_temperature_night.delete(0, END)
    entry_feels_like.delete(0, END)
    entry_description.delete(0, END)    
    temperature = recent_data['temperature']
    feels_like_now = recent_data['feels_like']
    icon = recent_data['icon']
    description_current = recent_data['description']    
    icon_image = get_image(icon)
    label_icon.configure(image = icon_image)
    label_icon.image = icon_image

    temperature_day = forecast_data['temperature_day']
    temperature_night = forecast_data['temperature_night']
    feels_like = forecast_data['feels_like']
    description = forecast_data['description']
    forecast_icon = forecast_data['icon']
    forecast_icon_image = get_image(forecast_icon)
    label_icon_forecast.configure(image = forecast_icon_image)
    label_icon_forecast.image = forecast_icon_image

    entry_temperature.insert(END, temperature)
    entry_feels_like_now.insert(END, feels_like_now)
    entry_description_current.insert(END, description_current)
    entry_temperature_day.insert(END, temperature_day)
    entry_temperature_night.insert(END, temperature_night)
    entry_feels_like.insert(END, feels_like)
    entry_description.insert(END, description)

'''Creating instance of tkinter with and all needed labels and entries'''
master = Tk()
master.geometry("700x250")
master.title("Weather App")
master['background']='#d7e58c'


spacer_top = Label(master, height=1, pady=10)
spacer_bottom = Label(master, height=1, pady=10)

label_enter_city= Label(master, text="Enter city You are in", font=('Helvetica 13'))
label_temperature = Label(master, text="Temperature now: ", font=('Helvetica 13'))
label_feels_like_now = Label(master, text="Feels like: ", font=('Helvetica 13'))
label_description_current = Label(master, text="Description: ", font=('Helvetica 13'))

label_temperature_day = Label(master, text="Temperature tomorrow (day): ", font=('Helvetica 13'))
label_temperature_night = Label(master, text="Temperature tomorrow (night): ", font=('Helvetica 13'))
label_feels_like = Label(master, text="Feels like: ", font=('Helvetica 13'))
label_description = Label(master, text="Description: ", font=('Helvetica 13'))
label_icon = Label(master, bg='white')
label_icon_forecast = Label(master, bg='white')

entry_enter_city = Entry(master)
entry_temperature = Entry(master)
entry_feels_like_now = Entry(master)
entry_description_current = Entry(master)
entry_temperature_day = Entry(master)
entry_temperature_night = Entry(master)
entry_feels_like = Entry(master)
entry_description = Entry(master)

btn = Button(master, text ="Get forecasts!", command = get_data)

label_enter_city.grid(row=0, column=0, padx=10, pady=10)
label_temperature.grid(row=1, column=0, padx=10, pady=10)
label_feels_like_now.grid(row=2, column=0, padx=10, pady=10)
label_description_current.grid(row=3, column=0, padx=10, pady=10)
label_temperature_day.grid(row=4, column=0, padx=10, pady=10)
label_temperature_night.grid(row=5, column=0, padx=10, pady=10)
label_feels_like.grid(row=6, column=0, padx=10, pady=10)
label_description.grid(row=7, column=0, padx=10, pady=10)


entry_enter_city.grid(row=0, column=1, padx=10, pady=10)
entry_temperature.grid(row=1, column=1, sticky="e", padx=10, pady=10)
entry_feels_like_now.grid(row=2, column=1, sticky="e", padx=10, pady=10)
entry_description_current.grid(row=3, column=1, sticky="e", padx=10, pady=10)
entry_temperature_day.grid(row=4, column=1, sticky="e", padx=10, pady=10)
entry_temperature_night.grid(row=5, column=1, sticky="e", padx=10, pady=10)
entry_feels_like.grid(row=6, column=1, sticky="e", padx=10, pady=10)
entry_description.grid(row=7, column=1, sticky="e", padx=10, pady=10)

btn.grid(row=0, column=3, padx=10, pady=10)

label_icon.grid(row=3, column=3, padx=10, pady=10)
label_icon_forecast.grid(row=6, column=3, padx=10, pady=10)

mainloop()