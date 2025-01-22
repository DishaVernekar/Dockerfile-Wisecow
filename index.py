from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\"https://github.com/nyrahul/wisecow/assets/9133227/8d6bfde3-4a5a-480e-8d55-3fef60300d98:\"\"}"

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("8080"), debug=True)
