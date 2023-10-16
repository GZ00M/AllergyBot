import telebot
import requests
import datetime
import sqlite3

con = sqlite3.connect("pollen_database.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Bereza(date INTEGER, value INTEGER)")
cur.execute("INSERT INTO Bereza (date, value) VALUES (1, 0)")
res = cur.execute("SELECT * FROM Bereza")
print(res.fetchone())

"""
class pollen:
    pollen = {
        'Bereza' : {'Jan' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false, '31' : false}, 
                    'Feb' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false}, 
                    'Mar' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false, '31' : false}, 
                    'Apr' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false}, 
                    'May' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false, '31' : false}, 
                    'Jun' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false}, 
                    'Jul' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false, '31' : false}, 
                    'Aug' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false, '31' : false}, 
                    'Sep' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false}, 
                    'Oct' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false, '31' : false}, 
                    'Nov' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false}, 
                    'Dec' : {'1' : false, '2' : false, '3' : false, '4' : false, '5' : false, '6' : false, '7' : false, '8' : false, '9' : false, '10' : false, '11' : false, '12' : false, '13' : false, '14' : false, '15' : false, '16' : false, '17' : false, '18' : false, '19' : false, '20' : false, '21' : false, '22' : false, '23' : false, '24' : false, '25' : false, '26' : false, '27' : false, '28' : false, '29' : false, '30' : false, '31' : false}
        }
    }
"""

#Tokens
weather_token = 'ddd0af3053f9e38df2bd318431751176'
bot_token = "6531175645:AAHTJRNrd09ae8YGPUljZ_IFcvdx4btPs7k"

#Refernece to bot object
bot = telebot.TeleBot(bot_token)

#City and url template
city = "Almaty"
lat = "43.22"
lon = "76.85"
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'
url_future = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={weather_token}'

#Handler for /start command
@bot.message_handler(commands=['start', 'back'])
def start(message):
    #Adding keyboard button
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/now')
    keyboard.row('/additional')
    keyboard.row('/help')
    
    #Perform the button
    bot.send_message(message.chat.id, "Current choosen city is Almaty", reply_markup=keyboard)

#Handler for /request command
@bot.message_handler(commands = ['now'])
def request(message):
    #Making request to OpenWheather
    response = requests.get(url)

    #Handling and processing response
    if response.status_code == 200:
        #Getting data in JSON format
        data = response.json()

        #Saving data from JSON for easy access
        time = datetime.datetime.now()
        temp = round(data['main']['temp'] - 273.15, 2)
        desc = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']
        hum = data['main']['humidity']
        wind_speed = data['wind']['speed']

        #Uncomment this for debugging
        #print(data)

        koef = {6 : 0.2, 2 : 0.4, 5 : 0.6, 3 : 0.8, 8 : 1, 7 : 1}

        a = ((temp * 0.05 if temp > 0 else 0.01) \
            + (2 if weather_id == 800 else koef[int(str(weather_id)[0])]) \
            + (hum * 0.02) \
            + (wind_speed * 1.1)) / 4
        b = 1

        x = round(round(a, 2) * b) if b != 0 else 0

        #Providing data
        bot.send_message(message.chat.id, f'{time.strftime("%d/%m/%Y %H:%M:%S")} \n\
                                            \nTemperature: {temp} C \
                                            \nDescription: {desc} \
                                            \nHumidity: {hum}% \
                                            \nWind Speed: {wind_speed} m/s \
                                            \nDanger lever: {x}')
    else:
        #Error if data is not fetched
        bot.reply_to(message, "Error fetching weather data")

@bot.message_handler(commands=['additional'])
def additional(message):
    #Adding keyboard button
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/tomorrow')
    keyboard.row('/threedays')
    keyboard.row('/back')
    
    #Perform the button
    bot.send_message(message.chat.id, "Choose prediction date range", reply_markup=keyboard)

@bot.message_handler(commands=['tomorrow'])
def tomorrow(message):
    response = requests.get(url_future)

    time = datetime.datetime.today() + datetime.timedelta(days=1)

    if response.status_code == 200:
        timestamp_tomorrow_12pm = int(datetime.datetime.strptime(str(time.strftime("%d/%m/%Y")), "%d/%m/%Y").timestamp()) + 3600 * 12
        
        #Getting data in JSON format
        for item in response.json()['list']:
            if item['dt'] == timestamp_tomorrow_12pm:
                data = item

        #Tomorrow exactly 12PM
        #print(int(datetime.datetime.strptime(str(time.strftime("%d/%m/%Y")), "%d/%m/%Y").timestamp()) + 3600 * 12)
        #print(data)

        temp = round(data['main']['temp'] - 273.15, 2)
        desc = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']
        hum = data['main']['humidity']
        wind_speed = data['wind']['speed']

        koef = {6 : 0.2, 2 : 0.4, 5 : 0.6, 3 : 0.8, 8 : 1, 7 : 1}

        a = ((temp * 0.05 if temp > 0 else 0.01) \
            + (2 if weather_id == 800 else koef[int(str(weather_id)[0])]) \
            + (hum * 0.02) \
            + (wind_speed * 1.1)) / 4
        b = 1

        x = round(round(a, 2) * b) if b != 0 else 0

        #Providing data
        bot.send_message(message.chat.id, f'{time.strftime("%d/%m/%Y")} \n\
                                            \nTemperature: {temp} C \
                                            \nDescription: {desc} \
                                            \nHumidity: {hum}% \
                                            \nWind Speed: {wind_speed} m/s \
                                            \nDanger lever: {x}')

@bot.message_handler(commands=['threedays'])
def threedays(message):
    response = requests.get(url_future)

    if response.status_code == 200:
        for i in range(3):
            time = datetime.datetime.today() + datetime.timedelta(days=i+1)

            timestamp_tomorrow_12pm = int(datetime.datetime.strptime(str(time.strftime("%d/%m/%Y")), "%d/%m/%Y").timestamp()) + 3600 * 12
            
            #Getting data in JSON format
            for item in response.json()['list']:
                if item['dt'] == timestamp_tomorrow_12pm:
                    data = item
                    break

            #Tomorrow exactly 12PM
            #print(int(datetime.datetime.strptime(str(time.strftime("%d/%m/%Y")), "%d/%m/%Y").timestamp()) + 3600 * 12)
            #print(data)

            temp = round(data['main']['temp'] - 273.15, 2)
            desc = data['weather'][0]['description']
            weather_id = data['weather'][0]['id']
            hum = data['main']['humidity']
            wind_speed = data['wind']['speed']

            koef = {6 : 0.2, 2 : 0.4, 5 : 0.6, 3 : 0.8, 8 : 1, 7 : 1}

            a = ((temp * 0.05 if temp > 0 else 0.01) \
                + (2 if weather_id == 800 else koef[int(str(weather_id)[0])]) \
                + (hum * 0.02) \
                + (wind_speed * 1.1)) / 4
            b = 1

            x = round(round(a, 2) * b) if b != 0 else 0

            #Providing data
            bot.send_message(message.chat.id, f'{time.strftime("%d/%m/%Y")} \n\
                                                \nTemperature: {temp} C \
                                                \nDescription: {desc} \
                                                \nHumidity: {hum}% \
                                                \nWind Speed: {wind_speed} m/s\
                                                \nDanger lever: {x}')

@bot.message_handler(commands=['help'])
def help(message):
    #Perform the button
    bot.send_message(message.chat.id, "In order to use this bot please press start and request button")

#Continious polling
bot.infinity_polling()