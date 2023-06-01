from flask import Flask
import requests
import json
import pickle

app = Flask(__name__)

@app.route('/')
def myapp():
	data_url = 'http://rocky-retreat-74526.herokuapp.com/sensor'
	response = requests.get(data_url).text
	json_data = json.loads(response)
	data_cross_val = []
	for i in json_data:
		if len(i)==8:		
			try:
				a, b, c = i["A"].split(',')
				data_cross_val.append(i)
			except:
				pass

	for i in data_cross_val:
		A1, A2, A3 = i["A"].split(',')
		G1, G2, G3 = i["G"].split(',')
		l1, l2 = i["l"].split(',')

		i['A1'] = float(A1)
		i['A2'] = float(A2)
		i['A3'] = float(A3)

		i['G1'] = float(G1)
		i['G2'] = float(G2)
		i['G3'] = float(G3)

		i['l1'] = float(A1)
		i['l2'] = float(A2)

		del i["_id"]
		del i["A"]
		del i["G"]
		del i["l"]

	with open ('model_pickle', 'rb') as f:
		model = pickle.load(f)

	return data_cross_val

if __name__=="__main__":
	app.run(debug=True, port=7000)
