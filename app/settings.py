from ._settings import *

# Add your custom settings here


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test-assignment-1',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PASSWORD': '123123',
    }
}
