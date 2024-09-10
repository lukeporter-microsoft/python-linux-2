import bottle
from bottle import Bottle, run, template
import json
import image

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/call')
def call_service():
    directoryName = 'photos'
    image.process(directoryName)

@app.route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    call_service()
    return template('index.tpl',data="Request completed!", title=title)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)


