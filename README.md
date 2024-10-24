Referencing my py-qubits repo to try and recreate the functionality of a quantum register.

Some thoughs/TODO:
    -> IDK if I am validating a quantum register correctly. I couldn't find an exact equation like the method used to validate an inidividual qudit; the implementation I have is a result of working with ChatGPT. I am assuming a valid qubit/qutrit/qudit must have its individual measurement state probabilities sum to 1 (i.e. the sum of complex modulus for each complex number describing a qudit/qlu must sum to 1). This still allows for encoded states that may not ever be observable (i.e. have complex modulus/probability of 0).
    
    This way you can mimic "entanglement" of qudits/qlus as one observation should hold true for all qudits entangled in the register; this is why I generate the observation for the register when you call it; you could also pass in the observation and then measure the individual qudits that way; but the result would be the same cause of how true_pyrand() re-seeds on every call before generating the observation.