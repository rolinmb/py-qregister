from qudit import qudit
from qregister import qregister
from math import sqrt

N_ITERS = 10000

if __name__ == '__main__':
    qudit1 = qudit(0.5, sqrt(3)/2) # 25% chance to collapse to {0}; 75% chance to collapse to '1'
    qudit2 = qudit(0.5, 0.5, sqrt(2)/2) # 25% chance to collapse0 to {0} or {1}, 50% chance to collapse to {2}
    qr = qregister(qudit1, qudit2)
    nqd1Zeros = nqd1Ones = 0
    nqd2Zeros = nqd2Ones = nqd2Twos = 0
    for n in range(0, N_ITERS):
        measurement = qr.measure()
        #print(f"src/main.py :: Iteration {n} qr.measure() = {measurement}")
        if measurement[0] == 0:
            nqd1Zeros += 1
        elif measurement[0] == 1:
            nqd1Ones += 1
        if measurement[1] == 0:
            nqd2Zeros += 1
        elif measurement[1] == 1:
            nqd2Ones += 1
        elif measurement[1] == 2:
            nqd2Twos += 1
    print(f"src/main.py :: Quantum Register Measurement Test Results after {N_ITERS} Iterations:")
    print(f"\tqudit1 -> {nqd1Zeros} Zeros observed; {nqd1Ones} Ones observed.")
    print(f"\tqudit2 -> {nqd2Zeros} Zeros oberved; {nqd2Ones} Ones observed; {nqd2Twos} Twos observed.")
