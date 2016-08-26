###################################################################################################################################	
###################################################################################################################################	
########################        Code to generate fake weather data for a toy simulation environment      ##########################	
########################                          Code written by : Nisarg Shah                          ##########################	
########################							    Rev 1 : 24/8/2016								 ##########################	
###################################################################################################################################	
###################################################################################################################################	


import random
import datetime
import time
import msvcrt
g_words = []		# List for storing the countries and their latitude, longitude and altitude


# Open the file for reading.
c_fname = 'list.txt'	

try:
	c_fhand = open(c_fname)
except:
	print 'File cannot be opened:', c_fname
	exit()
for line in c_fhand:						# Read each line from the input file
	line = line.rstrip()
	for word in line.split(','):			# separate each token of the line
		g_words.append(word)				# flaten the file and store each token in a single list - l_word

#Number of cities in the list		
l_num_of_city = len(g_words)/4				

#constants for weather conditions
c_weather = ['Rain','Snow','Sunny']

#initialising date to current time plus some delta between 5 mins to 24 hours.
dt = datetime.datetime.now() + datetime.timedelta(seconds=random.randint(300,86400))

###################################################################################################################################
#function to predict weather depending on the Temperature, Pressure and Relative Humidity. More constraints can be added
def weather_condition (rel_humidity,temperature,pressure,city):
	
	l_month = dt.strftime('%m')
	#If month is between March and September and the city is in the Southern Hemisphere and temperature is less than 20 degree C, 
	#and relative humidity is less than 60%, then it cannot be rainy 
	if (l_month>3 and l_month < 9 and g_words[city*4+1] < 0 and temperature > 20 and rel_humidity<60):	
		l_weather = 'Sunny'
	elif (l_month>3 and l_month < 9 and g_words[city*4+1] < 0 and temperature > 20 and rel_humidity>=60):
		l_weather = 'Rain'
	elif (rel_humidity<60): 	
		l_weather = random.choice(['Snow','Sunny'])
	elif (temperature > 10):
		l_weather = random.choice(['Rain','Sunny'])
	elif (l_month>3 and l_month < 9 and g_words[city*4+1] > 0):
		l_weather = random.choice(['Rain','Sunny'])
	else:
		l_weather = random.choice (c_weather)
		
	return (l_weather) 	
###################################################################################################################################

	
###################################################################################################################################	
#Function to format the output for each city
def cityloc (l_city):
	l_city_name = g_words[l_city*4]
	l_city_latitute = g_words[l_city*4+1]
	l_city_longitude = g_words[l_city*4+2]
	l_city_altitude = g_words[l_city*4+3]
	l_clla = l_city_name+"|"+l_city_latitute+","+l_city_longitude+","+l_city_altitude
	return (l_clla)
###################################################################################################################################


###################################################################################################################################	
#Function to randomly generate values for temperature, pressure and relative humidity within a fixed range	
def generate_random_tpr(l_city):
	l_month = dt.strftime('%m')
	if (l_month>3 and l_month < 9 and g_words[l_city*4+1] < 0 ):
		l_temperature = random.choice(-15,30)
	else:	
		l_temperature = random.uniform (-15.0,50.0)		# Temperature range defined between -15 to 50 degrees C - Source Wikipedia
	l_pressure = random.uniform (950.00,1100.00)		# Atmospheric pressure defined between 950 to 1100 hPa - Source Wikipedia
	l_rel_humidity = random.randint (10,99)				# Relative humidity defined between 10 to 99% - Source Wikipedia
	
	return (l_temperature,l_pressure,l_rel_humidity)
###################################################################################################################################	
	
	
#while True: 	#this will provide continuous outputs, till the user presses any key. This is more for the real game testing scenario
for i in range(50):	# For loop introduced for test purposes. The loop can run for values higher than 50
	if msvcrt.kbhit():	# waiting for a key press to exit the program
		print "End of Program"
		break
	else:	
				
		city = random.randint(0,l_num_of_city-1)							# Get a random city from the list of cities in the input file
		temperature,pressure,rel_humidity = generate_random_tpr(city)		# Generate random values for temperature, pressure and Relative Humidity depending on city and time
		weather = weather_condition(rel_humidity,temperature,pressure,city)	# Function call to determine the weather condition
		clla = cityloc(city)												# Function call to get output format for city
		
		# Print statement to get the location and the other parameters including the date in the ISO8601Z format
		print (clla+"|"+(dt.strftime('%Y-%m-%dT%H:%M:%SZ'))+"|%s|%+2.2f|%4.2f|%2d"%(weather,temperature,pressure,rel_humidity)) 
		
		#increment time value by a random number of seconds between 5 mins to 5 days	
		dt = dt + datetime.timedelta(seconds=random.randint(300,86400*5))
		
		
	
	

	
