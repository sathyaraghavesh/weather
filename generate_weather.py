def getPosition():
	#get the current position using some data source or APIs
	position = []
	position.append(getLatitude())
	position.append(getLongitude())
	position.append(getElevation())
	
	return ','.join(map(str, position)

def getTime():
	#...
	return time #time in a string

def getCondition():
	....

#rest of the functions ...
	
def getWeather()
	weatherInfo = []
	weatherInfo.append(getLocation)
	weatherInfo.append(getPosition)
	weatherInfo.append(getTime)
	weatherInfo.append(getCondition)
	weatherInfo.append(getTemperature)
	weatherInfo.append(getPressure)
	weatherInfo.append(getHumidity)

	return '|'.join(map(str, weatherInfo))
	
	
