import pytest

from backend.config import TestConfig
from backend.main import create_app


@pytest.fixture(scope='session')
def app(request):
    app = create_app(TestConfig)

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
