from qudit import qudit
from qregister import qregister
from util import true_pyrand
from math import sqrt

if __name__ == '__main__':
    qudit1 = qudit(0.5, sqrt(3)/2)
    qudit2 = qudit(0.5, 0.5, sqrt(2)/2)
    register = qregister(qudit1, qudit2)
    print(f"src/main.py :: register.measure() = {register.measure(true_pyrand())}")