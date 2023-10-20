file = open("activity_logger.txt")

data = file.read()

number_of_start = data.count("start")
number_of_now = data.count("now")
number_of_tomorrow = data.count("tomorrow")
number_of_threedays = data.count("threedays")
number_of_help = data.count("help")

print("Number of starts: ", number_of_start)
print("Number of nows: ", number_of_now)
print("Number of tomorrows: ", number_of_tomorrow)
print("Number of threedays: ", number_of_threedays)
print("Number of helps: ", number_of_help)

file.close()