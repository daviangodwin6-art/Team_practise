import subprocess
import sys

def test_test1_runs_without_error():
    result = subprocess.run([sys.executable, "test1.py"], capture_output=True, text=True)
    assert result.returncode == 0
