import pytest
from app.main import app  
from app.model import SimpleLinearRegression  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def model():
    return SimpleLinearRegression()
