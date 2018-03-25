from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/<text>".decode('utf-8'))
def home(text=""):
	return "<h1>{0}</h1>".format(text.decode('base64'))
		
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000)
    # http://localhost:5000/
    # {"lista": ["python", "eh", "lindo"]}