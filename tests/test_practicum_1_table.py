import subprocess

def test_practicum_1_table():
    result = subprocess.run(["python", "practicum_1.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "5" in result.stdout
    assert "50" in result.stdout
