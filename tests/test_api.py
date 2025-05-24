import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from app.main import app
from app.model import SimpleLinearRegression
import numpy as np

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    """Test prediction with valid input"""
    response = client.post('/predict', 
                         json={'x': 10},
                         headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    assert response.json['prediction'] == 21.0  

def test_invalid_input(client):
    """Test missing required field"""
    response = client.post('/predict', 
                         json={'wrong_field': 5},
                         headers={'Content-Type': 'application/json'})
    assert response.status_code == 400

def test_model_logic():
    """Test model directly"""
    model = SimpleLinearRegression()
    assert np.isclose(model.predict(5), 11.0)