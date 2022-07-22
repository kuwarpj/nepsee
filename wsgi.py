

from whitenoise import WhiteNoise
import whitenoise


from index import app

application = whitenoise(app)