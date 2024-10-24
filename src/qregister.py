from util import true_pyrand

class qregister:
    def __init__(self, *qudits):
        self.qudits = list(qudits)
    """ self._validate() # Don't need to validate register if all qudits are entangled and validated too
    
    def _validate(self):
        for qudit in self.qudits:
            total_prob = sum(abs(c)**2 for c in qudit.amplitudes)
            if round(total_prob, 6) != 1.0:
                raise ValueError(f"src/qregister.py Qudit {qudit} outcome probabilities do not sum to 1: {total_prob}")
    """
    def measure(self):
        result = []
        obs = true_pyrand()
        for qudit in self.qudits:
            measured_value = qudit.measure(obs)
            result.append(measured_value)
        return result