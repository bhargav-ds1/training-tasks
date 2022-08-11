from flask import Flask
from flask_restful import Resource, Api
import numpy as np
from random_words import RandomWords

app = Flask(__name__)
api = Api(app)

class RandomWordGenerator(Resource):
    def get(self):
        rw = RandomWords()
        n=np.random.randint(5,11)
        words=rw.random_words(count=n)
        return " ".join(words)

api.add_resource(RandomWordGenerator, '/')

if __name__ == '__main__':
    app.run(debug=True)
