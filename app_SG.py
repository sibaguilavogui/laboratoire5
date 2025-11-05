from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from BE - 192.168.x.x'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
