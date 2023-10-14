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
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'

#Handler for /start command
@bot.message_handler(commands=['start'])
def start(message):
    #Adding keyboard button
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/request')
    keyboard.row('/help')
    
    #Perform the button
    bot.send_message(message.chat.id, "Current choosen city is Almaty", reply_markup=keyboard)

#Handler for /request command
@bot.message_handler(commands = ['request'])
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
        hum = data['main']['humidity']
        wind_speed = data['wind']['speed']

        #Uncomment this for debugging
        #print(data)

        #Providing data
        bot.send_message(message.chat.id, f'{time.strftime("%d/%m/%Y %H:%M:%S")} \n\
                                            \nTemperature: {temp} C \
                                            \nDescription: {desc} \
                                            \nHumidity: {hum}% \
                                            \nWind Speed: {wind_speed} m/s')
    else:
        #Error if data is not fetched
        bot.reply_to(message, "Error fetching weather data")

@bot.message_handler(commands=['help'])
def help(message):
    #Perform the button
    bot.send_message(message.chat.id, "In order to use this bot please press start and request button")

#Continious polling
bot.infinity_polling()