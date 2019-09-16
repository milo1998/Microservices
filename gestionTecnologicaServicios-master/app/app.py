# compose_flask/app.py
# https://runnable.com/docker/python/docker-compose-with-flask-apps
# https://stackoverflow.com/questions/42316511/communication-between-two-flask-services-in-docker
# https://github.com/eelkevdbos/microservices-flask/blob/master/concat/concat.py
from flask import Flask
from flask import render_template,request,make_response
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST', 'GET'])
def send():
	if request.form['action'] == '+':
	    #COMUNICARSE CON SUMA.PY
		num1 = request.form["num1"]
		num2 = request.form["num2"]
		suma=requests.get('http://suma:5000/'+num1+'/'+num2).text
		#suma=requests.get('http://suma:5000/5/8').text
		return render_template('/show_all.html', string_variable=suma)
	elif request.form['action'] == '-':
        #COMUNICARSE CON RESTA.PY
		num1 = request.form["num1"]
		num2 = request.form["num2"]
		resta=requests.get('http://resta:5000/'+num1+'/'+num2).text
		#suma=requests.get('http://suma:5000/5/8').text
		return render_template('/show_all.html', string_variable=resta)
	    #COMUNICARSE CON MULTIPLICACION.PY
	elif request.form['action'] == '*':
		num1 = request.form["num1"]
		num2 = request.form["num2"]
		multiplicacion=requests.get('http://multiplicacion:5000/'+num1+'/'+num2).text
		#suma=requests.get('http://suma:5000/5/8').text
		return render_template('/show_all.html', string_variable=multiplicacion)
	   	#COMUNICARSE CON MULTIPLICACION.PY
	elif request.form['action'] == '/':
	    #COMUNICARSE CON DIVISION.PY
		num1 = request.form["num1"]
		num2 = request.form["num2"]
		division=requests.get('http://division:5000/'+num1+'/'+num2).text
		#suma=requests.get('http://suma:5000/5/8').text
		return render_template('/show_all.html', string_variable=division)

@app.route('/show_all')
def show_all():
	return render_template('show_all.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)


