import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from practicum_1 import print_five_table

def test_print_five_table(capsys):
    print_five_table()
    captured = capsys.readouterr()
    expected = "\n".join([f"5 * {i} = {5 * i}" for i in range(1, 11)]) + "\n"
    assert captured.out == expected
