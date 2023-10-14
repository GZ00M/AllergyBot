 import telebot
import requests

weather_token = 'ddd0af3053f9e38df2bd318431751176'
bot_token = "6531175645:AAHTJRNrd09ae8YGPUljZ_IFcvdx4btPs7k"

bot = telebot.TeleBot(bot_token)

city = "Almaty"

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

@bot.message_handler(commands = ['request'])
def request(message):
    url = get_url()
    bot.send_photo(message.chat.id, url)


bot.infinity_polling()