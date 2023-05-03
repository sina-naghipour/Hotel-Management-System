from flask import Flask
from api.routes import api


SECRET_KEY = '5655c052-96d9-4576-b804-cbc235338939'
app = Flask(__name__)

app.register_blueprint(api)

app.config.update(SECRET_KEY=SECRET_KEY)

@app.route('/', methods=['GET'])
def index():
    return 'hey'