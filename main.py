import rake
import operator
import sys
from flask import Flask

rake_object = rake.Rake("stopwords_pt.txt", 4, 3, 0)

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'
  
@app.route('/oi')
def hello_world():
  return 'Hello, World!'

@app.route('/texto')
@app.route("/texto/<text>".decode('utf-8'))
def home(text=""):
	text = text.decode('base64')
	keywords = rake_object.run(text)
	#print "Keywords:", keywords
	#print text
	kw = []
	for name in keywords:
		if  name[1]>1:
			kw.append(name[0])

	myList = ','.join(map(str, kw))

	#print myList
	return myList
	
if __name__ == '__main__':
    app.run()
    # http://localhost:5000/
    # {"lista": ["python", "eh", "lindo"]}