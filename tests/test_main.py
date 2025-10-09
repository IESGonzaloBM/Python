import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import suma

# Agregar el directorio raíz del proyecto (practica6) al sys.path

def test_sum():
    assert suma(10, 2) == 12
    assert suma(13, 43) == 56
    assert suma(3, -6) == -3