from unittest import TestCase

import app


class Test(TestCase):
    def test_hello_world(self):
        assert app.hello_world() == 'Hello World!'
