def test_davian():
    import daviantest
    with open('daviantest.py') as f:
        content = f.read()
    assert 'iphone' in content
    assert 'samsung' in content
    assert 'redmi' in content
