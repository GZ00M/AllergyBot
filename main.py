import telebot
import requests
import datetime

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