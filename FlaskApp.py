# from flask import Flask, jsonify, request
# from flask_restful import Resource, Api  # using flask_restful

# # creating the flask app
# app = Flask(__name__)

# # creating an API object
# api = Api(app)

# # Welcome message for the home page
# @app.route('/', methods=['GET'])
# def home():
#     return jsonify({'message': 'Welcome to the API!'})

# # making a class for a particular resource
# # the get, post methods correspond to get and post requests
# # they are automatically mapped by flask_restful.
# # other methods include put, delete, etc.
# class Hello(Resource):
#     # corresponds to the GET request.
#     # this function is called whenever there
#     # is a GET request for this resource
#     def get(self):
#         return jsonify({'message': 'hello MFS'})

#     # Corresponds to POST request
#     def post(self):
#         data = request.get_json()
#         response = jsonify(data)
#         response.status_code = 200
#         return response


# # another resource to calculate the square of a number
# class Square(Resource):

#     def get(self, num):
#         # Corresponds to Get request and an Integer is sent with The Request of this resource
#         # and this function is called
#         return jsonify({'square': num**2})


# class RQ(Resource):
#     # Corresponds to Get request and this function where a text file 'requirements.txt' contents
#     # are returned in dictionary or Json format
#     def get(self):
#         rq = {}
#         with open('*Your File URL here*', 'r') as f:
#             for i, r in enumerate(f.readlines()):
#                 rq[f'{i}'] = r.strip()
#         return jsonify(rq)

#     # Corresponds to Post request where this Function append The Data Sent by Request Into the Same File
#     def post(self):
#         data = request.get_json()['Name']
#         rq = {}
#         with open('*Your File URL here*', '+a') as f:
#             f.write(f'\n{data}')
#             f.seek(0)
#             for i, r in enumerate(f.readlines()):
#                 rq[f'{i}'] = r.strip()
#         response = jsonify(rq)
#         response.status_code = 200
#         return response



# # Add the resources with their respective endpoints
# api.add_resource(Hello, '/hello', methods=['GET', 'POST'])
# api.add_resource(Square, '/square/<int:num>')
# api.add_resource(RQ, '/rq', methods=['GET', 'POST'])  # describing the request methods for this endpoint of a resource

# if __name__ == '__main__':  # Main Function
#     app.run(debug=True)  # Runs the flask app
import requests
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Fetch data from a given URL
def fetch_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data'}

# Welcome message for the home page
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API!'})

# Endpoint to get recent releases
@app.route('/recent-release', methods=['GET'])
def recent_release():
    url = 'https://webdis-7ies.onrender.com/recent-release'
    data = fetch_data_from_url(url)
    return jsonify(data)

# Endpoint to get popular data
@app.route('/anime-details', methods=['GET'])
def get_popular():
    url = 'https://webdis-7ies.onrender.com/anime-details/'
    data = fetch_data_from_url(url)
    return jsonify(data)

# Endpoint to get top airing data
@app.route('/top-airing', methods=['GET'])
def top_airing():
    url = 'https://webdis-7ies.onrender.com/top-airing'
    data = fetch_data_from_url(url)
    return jsonify(data)

# Class-based resource for Hello
class Hello(Resource):
    def get(self):
        return jsonify({'message': 'Hello World'})

    def post(self):
        data = request.get_json()
        response = jsonify(data)
        response.status_code = 200
        return response

# Class-based resource for calculating square
class Square(Resource):
    def get(self, num):
        return jsonify({'square': num**2})

# Class-based resource for managing requirements file
class RQ(Resource):
    def get(self):
        rq = {}
        with open('requirements.txt', 'r') as f:
            for i, r in enumerate(f.readlines()):
                rq[f'{i}'] = r.strip()
        return jsonify(rq)

    def post(self):
        data = request.get_json()['Name']
        rq = {}
        with open('requirements.txt', '+a') as f:
            f.write(f'\n{data}')
            f.seek(0)
            for i, r in enumerate(f.readlines()):
                rq[f'{i}'] = r.strip()
        response = jsonify(rq)
        response.status_code = 200
        return response

# Adding resources to endpoints
api.add_resource(Hello, '/hello', methods=['GET', 'POST'])
api.add_resource(Square, '/square/<int:num>')
api.add_resource(RQ, '/rq', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)

# Running the Flask App:
# Run the script.
# Open your browser or use an API testing tool like Postman.
# Make requests to the following URLs:
# http://192.168.1.45:5000/ (Home page with welcome message)
# http://192.168.1.45:5000/popular
# http://192.168.1.45:5000/recent-release
# http://192.168.1.45:5000/top-airing
# http://192.168.1.45:5000/anime-details/Anime_name
