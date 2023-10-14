import telebot
import requests

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
        temp = round(data['main']['temp'] - 273.15, 2)
        desc = data['weather'][0]['description']
        hum = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(data)

        #Providing data
        bot.send_message(message.chat.id, f'Temperature: {temp} C \
                                            \nDescription: {desc} \
                                            \nHumidity: {hum}% \
                                            \nWind Speed: {wind_speed} m/s')
    else:
        #Error if data is not fetched
        bot.reply_to(message, "Error fetching weather data")

#Continious polling
bot.infinity_polling()