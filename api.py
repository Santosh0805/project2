import requests 

api_key="452d535373fafc310a6eda80c4befc0d"   

city_name=input("Enter your city name:- ")   

url="https://api.openweathermap.org/data/2.5/weather?units=metric&appid="
complete_url = url + api_key + "&q=" +city_name

response=requests.get(complete_url).json()

print(f"Weather Temperature = {response['main']['temp']}°C")
