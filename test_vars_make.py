def test_var_make(capsys, monkeypatch):
    inputs = ["2", "2", "2", "2"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop())
    import vars_make

    captured = capsys.readouterr()

    assert "he circle has an area of 12.566370614359172 and a perimeter of 12.566370614359172" in captured.out
    assert "The rectangle has an area of 4 and a perimeter of 8" in captured.out
    assert "The octagon has an area of 19.31370849898476 and a perimeter of 16" in captured.out