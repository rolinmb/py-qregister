class qudit:
    def __init__(self, *amplitudes):
        self.amplitudes = list(amplitudes)
        self._validate()

    def _validate(self):
        total_prob = sum(abs(c)**2 for c in self.amplitudes) # every qudit must be valid
        if round(total_prob, 10) != 1.0:
            raise ValueError(f"src/main.py Qudit outcome probabilities do not sum to 1: {total_prob}")

    def measure(self, obs):
        cumulative_prob = 0
        for i, amplitude in enumerate(self.amplitudes):
            prob = abs(amplitude)**2
            cumulative_prob += prob
            if obs < cumulative_prob:
                return i

    def resetAmplitudes(self, *amplitudes):
        self.amplitudes = list(amplitudes)        

    def resetRegister(self):
        self.amplitudes = list()