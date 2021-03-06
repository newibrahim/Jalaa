import pyowm
import datetime
from datetime import date
import calender
owm = pyowm.OWM('0741d86c5a4615231dd18ef3c8e280ed')
location = owm.weather_at_place('New York, US')
weather = location.get_weather()

temp = weather.get_temperature('fahrenheit')
header = "\n\tNEW YORK 3-DAY FORECAST:\n\n\tDay\t\tHigh\tLow\tConditions\n\t---\t\t----\t---\t----------\n"
forecast = "\t" + str(datetime.date.today() + datetime.timedelta(days=0)) + "\t" + str(temp.get('temp_max')) + "F" + "\t" + str(temp.get('temp_min')) + "F" + "\t" + str(datetime.date.today() + datetime.timedelta(days=1)) + "\n\t" + str(datetime.date.today() + datetime.timedelta(days=2))+ "\t\t" + str(temp.get('temp_max')) + "F" + "\t" + str(temp.get('temp_min')) + "F" + "\tSunny\n\tTuesday\t\t" + str(temp.get('temp_max')) + "F" + "\t50F\tCloudy\n"
print(header + forecast)
