import subprocess


def test_motion_print():
    result = subprocess.run(["python", "practicum_1.py"], capture_output=True, text=True)
    assert "motion test" in result.stdout
