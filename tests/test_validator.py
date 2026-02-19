from src.validator import validate

def test_validate():
    assert validate({"key": "value"}) is True
