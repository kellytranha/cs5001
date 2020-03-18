from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output
    sp = StringProcessor()
    assert sp.process_string("ab") == ""
    assert sp.process_string("ab*") == "b"
    assert sp.process_string("ab^") == "ba"
    assert sp.process_string("^") == ""
    assert sp.process_string("a^") == "a"
    assert sp.process_string("b-5es^m9c*u?er^xl0t*a") == "secret"
    assert sp.process_string("na0s*9-o*veXul^z-2it^,no^pr8") == "solution"
    assert sp.process_string(
        "zeM^un-e*0 t^a*l t^75*4a1:^s35*A,P ^2NM* ,^Mc.+GcO^"
        " t^3*,0^2 ^5m0*x81^"
        ) == "Meet at 5:15 PM, Oct 30, 2018"
