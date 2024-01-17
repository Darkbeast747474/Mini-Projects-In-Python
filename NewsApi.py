import requests

def scrape_news_api(api_key):    
    
    ''' Function That Fetchs The Information From A News API and Displays It Functions Parameters Are Your API Key'''
    
    url = "https://newsapi.org/v2/top-headlines"    # Url Of API Providor
    
    params = {
        'query': f'{(input("Enter The Topic: "))}',     #Parameters To Send To The Requested Url
        "apiKey": api_key,                              
        "language": 'en'
    }  
  

    data = requests.get(url, params=params).json()  #Getting The Data In the Form of JSON

    if response := requests.get(url, params=params).status_code == 200:   #Checking the Status Code Of The Request To Be Success
        
        for article in data["articles"]:
            print("Title:", article["title"])
            print("Author:", article["author"])                           #Json Are Just Like Python Dictionaries N We Access                           
            print("Description:", article["description"])                   #Necessary Information to Display
            print('Url:', article['url'])
            print("\n------------------------------------------------------------")
            
    else: #If The Request Failed 
        print("Error:", data["Unable To Get The Info Ryt Now!"])
    return data #Function Also returns The Response As Json object

if __name__ == "__main__":
  scrape_news_api()  #Pass Your API Key In Function Parameters

#For Any Information Visit https://newsapi.org/