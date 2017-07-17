from context import idiomatic

def test_sigmod_nocrash():
	result = idiomatic.fullparse("examples/sigmod17/fig1.bl")
	result = idiomatic.fullparse("examples/sigmod17/fig2.bl")
	result = idiomatic.fullparse("examples/sigmod17/fig6.bl")

	assert True