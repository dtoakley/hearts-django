from .common import *

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',] + MIDDLEWARE

# Pytest Test runner
TEST_RUNNER = 'hearts.test_runner.PytestTestRunner'
