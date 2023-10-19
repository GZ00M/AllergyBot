import telebot
import requests
import datetime
import sqlite3

class ActivityLogger:
    def __init__(self, file):
        self.filename = file
        try:
            f = open(file, 'r')
            f.close()
        except IOError:
            f = open(file, 'w+')
            f.close()

    def log(self, button):
        f = open(self.filename, "a")
        f.write(f"\n{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} {button}")
        f.close()

logger = ActivityLogger("activity_logger.txt")

con = sqlite3.connect("pollen_db.db", check_same_thread=False)
cur = con.cursor()

'''
cur.execute("CREATE TABLE IF NOT EXISTS Bereza(date INTEGER, value INTEGER)")
cur.execute("INSERT INTO Bereza (date, value) VALUES (1, 0)")
res = cur.execute("SELECT * FROM Bereza")
print(res.fetchone())
'''

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

month_converter = {
                    '01' : 'January', \
                    '02' : 'February', \
                    '03' : 'March', \
                    '04' : 'April', \
                    '05' : 'May', \
                    '06' : 'June', \
                    '07' : 'July', \
                    '08' : 'August', \
                    '09' : 'September', \
                    '10' : 'October', \
                    '11' : 'November', \
                    '12' : 'December'
}

#Handler for /start command
@bot.message_handler(commands=['start', 'back'])
def start(message):
    #Adding keyboard button
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/now')
    keyboard.row('/additional')
    keyboard.row('/help')

    username = message.from_user.username

    #print(username)

    #ABOBA NEXT LEVEL
    #cur.execute(f"CREATE TABLE IF NOT EXISTS {username} (TEXT);")

    logger.log("start")
    
    #Perform the button
    bot.send_message(message.chat.id, "Current choosen city is Almaty", reply_markup=keyboard)

#Handler for /request command
@bot.message_handler(commands = ['now'])
def now(message):
    #Making request to OpenWheather
    response = requests.get(url)

    logger.log("now")

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
        
        #result_from_db = cur.execute("SELECT * FROM April WHERE")
        #cur.execute("SELECT * FROM April;")
        rows = cur.execute(f"SELECT * FROM {month_converter[time.strftime("%m")]};").fetchall()
        max_val = max(rows, key=lambda x: x[1])[1]

        plants_with_max = ", ".join([x[0] for x in rows if x[1] == max_val])

        #print(plants_with_max)
        #print(month_converter[(datetime.datetime.today() + datetime.timedelta(days=43+31+31+29+31+30+31+30+31+31+30)).strftime("%m")])

        b = max_val

        x = round(round(a, 2) * b) if b != 0 else 0

        #Providing data
        bot.send_message(message.chat.id, f'{time.strftime("%d/%m/%Y %H:%M:%S")} \n\
                                            \nTemperature: {temp} C \
                                            \nDescription: {desc} \
                                            \nHumidity: {hum}% \
                                            \nWind Speed: {wind_speed} m/s \
                                            \nDanger lever: {x if x <= 2 else 2} \
                                            \nFlowering plants: {plants_with_max if max_val != 0 else "no plants are blooming now"}')
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

    logger.log("tomorrow")

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

        rows = cur.execute(f"SELECT * FROM {month_converter[time.strftime("%m")]};").fetchall()
        max_val = max(rows, key=lambda x: x[1])[1]

        plants_with_max = ", ".join([x[0] for x in rows if x[1] == max_val])

        a = ((temp * 0.05 if temp > 0 else 0.01) \
            + (2 if weather_id == 800 else koef[int(str(weather_id)[0])]) \
            + (hum * 0.02) \
            + (wind_speed * 1.1)) / 4
        b = max_val

        x = round(round(a, 2) * b) if b != 0 else 0

        #Providing data
        bot.send_message(message.chat.id, f'{time.strftime("%d/%m/%Y")} \n\
                                            \nTemperature: {temp} C \
                                            \nDescription: {desc} \
                                            \nHumidity: {hum}% \
                                            \nWind Speed: {wind_speed} m/s \
                                            \nDanger lever: {x if x <= 2 else 2} \
                                            \nFlowering plants: {plants_with_max if max_val != 0 else "no plants will be blooming"}')

@bot.message_handler(commands=['threedays'])
def threedays(message):
    response = requests.get(url_future)

    logger.log("threedays")

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

            rows = cur.execute(f"SELECT * FROM {month_converter[time.strftime("%m")]};").fetchall()
            max_val = max(rows, key=lambda x: x[1])[1]

            plants_with_max = ", ".join([x[0] for x in rows if x[1] == max_val])

            a = ((temp * 0.05 if temp > 0 else 0.01) \
                + (2 if weather_id == 800 else koef[int(str(weather_id)[0])]) \
                + (hum * 0.02) \
                + (wind_speed * 1.1)) / 4
            b = max_val

            x = round(round(a, 2) * b) if b != 0 else 0

            #Providing data
            bot.send_message(message.chat.id, f'{time.strftime("%d/%m/%Y")} \n\
                                                \nTemperature: {temp} C \
                                                \nDescription: {desc} \
                                                \nHumidity: {hum}% \
                                                \nWind Speed: {wind_speed} m/s\
                                                \nDanger lever: {x if x <= 2 else 2} \
                                                \nFlowering plants: {plants_with_max if max_val != 0 else "no plants will be blooming"}')

@bot.message_handler(commands=['help'])
def help(message):
    #Perform the button
    bot.send_message(message.chat.id, "In order to use this bot please press start and request button \
                                        \n \
                                        \nHere are 3 danger levels to describe the widespread of allergens: 0, 1, 2")

    logger.log("help")

    '''
    response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={weather_token}")

    if response.status_code == 200:
        data = response.json()
        print(data)'''

#Continious pollings
bot.infinity_polling()