from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
# import json to load json data wdata.delete()to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request
from .models import WeatherSearchHistory


def index(request): 
	if request.method == 'POST': 
		city = request.POST['city'] 
		''' api key might be expired use your own api_key 
			place api_key in place of appid ="your_api_key_here " '''
        
		# source contain JSON data from API 
		

		source = urllib.request.urlopen( 
			'http://api.openweathermap.org/data/2.5/weather?q='
					+ city + '&appid=7a7b68e1c322119af55ad469ca4cac84').read() 

		# converting JSON data to a dictionary 
		
		list_of_data = json.loads(source) 

		# data for variable list_of_data 

		wdata = WeatherSearchHistory()
		wdata.city = city
		wdata.country_code = str(list_of_data['sys']['country'])
		wdata.coordinate = str(list_of_data['coord']['lon']) + ' '+ str(list_of_data['coord']['lat'])
		wdata.temperature = str(list_of_data['main']['temp']) + 'k'
		wdata.pressure =  str(list_of_data['main']['pressure'])
		wdata.humidity = str(list_of_data['main']['humidity'])
		wdata.save()
		#WeatherSearchHistory.objects.all().delete()
		bdata = WeatherSearchHistory.objects.order_by("-timestamp")
		data = {    
			"bdata":bdata,
			"city":city,
			"country_code": str(list_of_data['sys']['country']), 
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']), 
			"temp": str(list_of_data['main']['temp']) + 'k', 
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 
		} 

        
		print(data) 
	else: 
		data ={} 
	return render(request, "main/index.html", data) 
