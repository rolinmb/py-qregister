from util import true_pyrand
from collections import Counter
#import matplotlib.pyplot as plt

class qregister:
    def __init__(self, *qudits):
        self.qudits = list(qudits) # Don't need to re-validate
    
    def measure(self):
        result = []
        obs = true_pyrand()
        for qudit in self.qudits:
                measured_value = qudit.measure(obs)
                result.append(measured_value)
            #self.visualize_measurement(result)
        return result

""" def visualize_measurement(self, result):
        counts = Counter(result)
        states, freqs = zip(*counts.items())
        total_measurements = sum(freqs)
        probabilities = [freq / total_measurements for freq in freqs]
        fig, ax = plt.subplots()
        ax.bar(states, probabilities, color='skyblue')
        ax.set_xlabel('Measured States')
        ax.set_ylabel('Probability')
        ax.set_title('Measurement Probabilities of Quantum Register')
        ax.set_ylim(0, 1)
        for i, prob in enumerate(probabilities):
            ax.text(states[i], prob + 0.02, f"{prob:.2f}", ha='center', va='bottom')
        plt.show()
"""
    