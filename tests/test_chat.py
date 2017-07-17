from context import idiomatic

def test_chat_nocrash():
	result = idiomatic.fullparse("examples/chat/client.bl")

	result = idiomatic.fullparse("examples/chat/server.bl")

	assert True