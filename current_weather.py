import requests
import datetime

owm_api_key = '49d60c155f5a57d4701ef9c096bda088'
url ='http://api.openweathermap.org/data/2.5/weather?'

def get_current_weather_report(city):
    try:
        complete_url = f'{url}appid={owm_api_key}&q={city}'
        response = requests.get(complete_url)
        w_data = response.json()
        # print(w_data)
        
        # Extract Description
        try:
            desc = w_data['weather'][0]['description']
            desc = desc.title()
            
        except:
            desc = "Description isn't found ):"
        
        #Extract temp
        try:
            temp = (float(w_data['main']['temp'])) - 273.15
            temp = round(temp, 2)
        
        except:
            temp = "Temperature is'nt found ):"
            
        #Extract max_temp
        try:
            max_temp = (w_data['main']['temp_max']) - 273.15
            max_temp = round(max_temp, 2)
            
        except:
            max_temp = "Maximum Temperature isn't found ):"
            
        #Extract min_temp
        try:
            min_temp = (w_data['main']['temp_min']) - 273.15
            min_temp = round(min_temp, 2)
            
        except:
            min_temp ="Minimum Tempearture isn't found ):"
        
        #Extract Humidity
        try:
            humidity = w_data['main']['humidity']
            
        except:
            humidity = "Humidity isn't found ):"
        
        #Extract Wind speed
        try:
            wind_speed = w_data['wind']['speed']
            
        except:
            wind_speed = "Wind Speed isn't found ):"
            
        #Wind Direction
        try:
            def get_wind_direction(degrees):
                directions = ["North", "North-Northeast", "Northeast", "East-Northeast",
                            "East", "East-Southeast", "Southeast", "South-Southeast",
                            "South", "South-Southwest", "Southwest", "West-Southwest",
                            "West", "West-Northwest", "Northwest", "North-Northwest"]

                index = int((degrees + 11.25) / 22.5) % 16

                return directions[index]
                        
            win_dir_deg = w_data['wind']['deg']
            win_dir = get_wind_direction(win_dir_deg)
            
        except:
            win_dir = "Wind Direction isn't found ):"
            
        #Wind gust speed
        try:
            gust_speed = w_data['wind']['gust']
        
        except:
            gust_speed = "Gust speed isn't found ):"
        
        #Extract visibility
        try:
            visibility_a = w_data.get('visibility')
            visibility = visibility_a / 1000
            
        except:
            visibility = "Visibility isn't found ):"
            
        #Extract pressure
        try:
            pressure = w_data['main']['pressure']
            
        except:
            pressure = "Pressure isn't found ):"
            
        #Extract Cloudiness
        try:
            cloudiness = w_data['clouds']['all']
            
        except:
            cloudiness = "Cloudiness isn't found"
        
    except:
        print(' : Error fetching weather data ):')
        
    datetime_setup = datetime.datetime.now()
    request_date = datetime_setup.strftime('%d-%m-%Y')
    request_time = datetime_setup.strftime('%I:%M')
        
    report = f''' ⛅ Weather Report of {city.capitalize()} ⛅
    =) {desc}
        ➡️ Requesting Date    : {request_date}
        ➡️ Requesting Time    : {request_time}
        ➡️ Temperature        : {temp} °C
        ➡️ Minimum Temperature: {min_temp} °C
        ➡️ Maximum Temperature: {max_temp} °C
        ➡️ Humidity           : {humidity}%
        ➡️ Wind Speed         : {wind_speed} m/s
        ➡️ Wind Direction     : {win_dir}
        ➡️ Gust Speed         : {gust_speed} m/s
        ➡️ Visibility         : {visibility} km
        ➡️ Pressure           : {pressure} hPa
        ➡️ Cloudiness         : {cloudiness}%'''
        
    all_info = [w_data, report]
    
    return all_info