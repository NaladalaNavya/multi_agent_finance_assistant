from agents.api_agent import APIAgent

def test_api_agent_returns_data():
    agent = APIAgent()
    df = agent.get_stock_data("AAPL", "1d")
    assert not df.empty
