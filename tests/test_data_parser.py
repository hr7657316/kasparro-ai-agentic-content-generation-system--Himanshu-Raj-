import pytest
from src.agents.data_parser_agent import DataParserAgent

def test_data_parser_valid_input():
    agent = DataParserAgent()
    input_data = {
        "Product Name": "Test Cream",
        "Price": "$50",
        "Benefits": "Moisturizing"
    }
    result = agent.run(input_data)
    assert result["name"] == "Test Cream"
    assert result["price"] == "$50"
    assert result["benefits"] == "Moisturizing"

def test_data_parser_missing_field():
    agent = DataParserAgent()
    input_data = {
        "Product Name": "Test Cream"
    }
    with pytest.raises(ValueError, match="Missing required field: price"):
        agent.run(input_data)
