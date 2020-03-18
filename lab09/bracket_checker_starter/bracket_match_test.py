from bracket_match import BracketMatch


def test_brackets_match():
    """Test brackets_match method"""
    # Include the following cases in your test:
    # "()" should succeed
    # "a(a[a])a({a})" should succeed
    # "(" should not succeed
    # "(}" should not succeed
    # "a(a(a)a(a)" should not succeed
    # "aa(a))a(a)" should not succeed
    bm = BracketMatch()
    assert bm.brackets_match("()")
    assert bm.brackets_match("a(a[a])a({a})")
    assert not bm.brackets_match("(")
    assert not bm.brackets_match("(}")
    assert not bm.brackets_match("a(a(a)a(a)")
    assert not bm.brackets_match("aa(a))a(a)")
