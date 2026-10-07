import subprocess

def test_practicum_1():
    result = subprocess.run(["python", "practicum_1.py"], capture_output=True, text=True)
    assert "Practicum 1" in result.stdout
    assert "5 * 1 = 5" in result.stdout
    assert "5 * 10 = 50" in result.stdout
