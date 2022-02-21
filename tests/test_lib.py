from mytestpackage.lib import try_me

def test_tryme(monkeypatch):
    
    monkeypatch.setattr('builtins.input', lambda _:"Marco")
    i = try_me()
    assert "Hello Marco!" in i 