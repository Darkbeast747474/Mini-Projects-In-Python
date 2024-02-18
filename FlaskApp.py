from flask import Flask, jsonify, request , Response
from flask_restful import Resource, Api  #using flask_restful 

# creating the flask app 
app = Flask(__name__) 

# creating an API object 
api = Api(app) 
    
# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 

class Hello(Resource): 
	# corresponds to the GET request. 
	# this function is called whenever there 
	# is a GET request for this resource 
	def get(self): 

		return jsonify({'message': 'hello MFS'}) 

	# Corresponds to POST request 
	def post(self): 
            data = request.get_json()
            response = jsonify(data)
            response.status_code = 200
            return response
        
        
# another resource to calculate the square of a number 
class Square(Resource): 

	def get(self, num): 
	#Corresponds to Get request and an Integer is sent with The Request of this resource
	#and this function is called
		return jsonify({'square': num**2}) 


class RQ(Resource):
    #Corresponds to Get request and this function where a text file 'requirements.txt' contents 
    #are returned in dictionary or Json format
    def get(self):
        rq = {}
        with open('*Your File URL here*', 'r') as f: 
          for i, r in enumerate(f.readlines()):
            rq[f'{i}'] = f'{r.replace('\n', '')}'  
        return jsonify(rq)
    
    #Corresponds to Post request where this Function append The Data Sent by Request Into the Same File
    def post(self):
        data = request.get_json()['Name']
        rq={}
        with open('*Your File URL here*','+a') as f:
            f.write(f'\n{data}')
            for i, r in enumerate(f.readlines()):
              rq[f'{i}'] = f'{r.replace('\n', '')}'
        response = jsonify(rq)
        response.status_code = 200
        return response  
        
		

# Add the resources with their respective endpoints
api.add_resource(Hello, '/hello', methods=['GET','POST'])
api.add_resource(Square, '/square/<int:num>')
api.add_resource(RQ, '/rq', methods=['GET', 'POST']) #describing the request methods for this endpoint of a resource

if __name__ == '__main__': #Main Function
    
 	app.run(debug = True)  #Runs the flask app
