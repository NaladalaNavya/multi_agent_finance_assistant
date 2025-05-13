from orchestrator.router import Router

def test_router_returns_response():
    router = Router()
    response, confidence = router.handle_text_query("What is today's exposure?")
    assert isinstance(response, str)
    assert confidence >= 0.0
