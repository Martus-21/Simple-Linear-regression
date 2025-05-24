import numpy as np
import pytest

def test_model_prediction(model):
    """Test model predicts y = 2x + 1"""
    assert np.isclose(model.predict(5), 11.0)
    assert np.isclose(model.predict(0), 1.0)
    assert np.isclose(model.predict(-2), -3.0)

def test_model_invalid_input(model):
    """Test error handling"""
    with pytest.raises(ValueError):
        model.predict("not_a_number")