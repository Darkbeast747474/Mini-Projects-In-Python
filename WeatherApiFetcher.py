import requests

def Scrape_Weather_Api(api_key):
    
    url = "https://weatherapi-com.p.rapidapi.com/current.json"  # URL for API requests
    querystring = {"q": f"{input('Enter The Name Of Your City: ')}"}   # Sending Desired Location in querystring format parameters
    headers = {
		"X-RapidAPI-Key": api_key, # API key 
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com" #API host 
        }
    response = requests.get(url, headers=headers, params=querystring).json() #Using get method to retrieve Data In Json format
    
    if 'error' not in response: #Checking if any error in response data
        print(f"Location: {response['location']['name']},{response['location']['region']},{response['location']['country']}")
        print(f"Temperature: {response['current']['temp_c']}℃ ,{response['current']['temp_f']}℉")
        print(f"Last Updated: {response['current']['last_updated']}")
    else:
        print("Unable to retrieve latest Weather forecast!!")   #In case Of Bad Request Print the message
    return response #Returning The Json Content which contains the The unaccessed Data As well

if __name__ == "__main__": #Main function
    Scrape_Weather_Api() #Pass Your API Key In Function Parameters
    
#For Further Information Visit https://www.weatherapi.com/    