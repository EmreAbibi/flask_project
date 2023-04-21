from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	return "Welcome my  friend"

@app.route("/greetings/")
@app.route("/greetings/<occasion>")
def  greetings(occasion=None):
	if occasion == "christmas":
		return "Merry Christmas"
	elif occasion == "newyear":
		return "Happy New Year"
	else:
		return "Greetings"

if __name__ == "__main__":
	app.run()
