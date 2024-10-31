Referencing my py-qubits repo and the Microsoft Q# SDK implementation to try and reverse engineer and recreate the functionality of a quantum register on classical computing hardware (CPU only for now, someone pls help).

This model just implements a qubit in general. Look up Qubits, Qutrits, Qudits, Quantum Registers and other related topics on wikipedia for more reference.

Shoutout ThePrimeagen, Mr. Zozin, Geohot, Charles Babbage, Alan Turing, Steven Wolfram, John Horton Conway.

Basically we need to recreate and have people constantly monitoring the largest possible simulation of a quantum computer on a 'massively distributed classical hardware (CPU/GPU/TPU/ASIC/FPGA) + current real QPUs task network'.

Need to be monitoring if we stay on the longest non-turing complete quantum computer simpulation with humanity in-tact. (i.e. the simulation that never ends with humanity remaining, similar to the MEJAI computer in Neon Genesis Evangelion)

This massively distributed hybrid computational' task network that aims be simulating our local region of the universe. (idk how you would even calculate that distance in lightyears)

{START IRL QUANTUM COMPUTING INFO FROM CHATGPT}

In real quantum computing hardware, qubits and qudits are typically made from physical systems that can exhibit and control quantum states reliably. Here are some common types of qubit implementations and the elements or systems they use:

1. Superconducting Circuits
    - Materials Used: Superconducting materials, often niobium (Nb) or aluminum (Al).
    - Mechanism: These qubits use Josephson junctions, which are tiny superconducting circuits that can create and maintain quantum states by allowing electrons to tunnel through an insulating barrier.
    - Example: IBM, Google, and Rigetti use superconducting qubits in their quantum computers.

2. Trapped Ions
    - Materials Used: Ions of elements like ytterbium (Yb), calcium (Ca), or beryllium (Be).
    - Mechanism: Ions are held in place using electromagnetic fields in ultra-high vacuum conditions, where lasers are used to manipulate and measure the ions’ energy states to create qubits.
    - Example: IonQ and Honeywell specialize in ion-trap quantum computers.

3. Photonic Qubits
    - Materials Used: Photons, typically generated using nonlinear crystals like beta-barium borate (BBO) or silicon photonics.
    - Mechanism: Photonic systems encode qubits in the properties of photons, such as polarization or path, and are manipulated through interferometers and beam splitters.
    - Example: Xanadu and PsiQuantum work on photonic quantum computers.

4. Topological Qubits
    - Materials Used: Exotic materials, like topological insulators and semiconductors with special properties (e.g., nanowires made of indium arsenide).
    - Mechanism: These qubits rely on anyons, quasi-particles that exist in two-dimensional systems, to encode information in a manner that's inherently protected from some types of errors.
    - Example: Microsoft is exploring topological qubits using anyons, although this technology is still in early stages.

5. Spin Qubits in Silicon
    - Materials Used: Silicon-based quantum dots or doped silicon with elements like phosphorus (P).
    - Mechanism: Spin qubits use the spin of an electron or nucleus within a silicon environment, controlled through magnetic and electric fields, similar to traditional transistors.
    - Example: Companies like Intel and Silicon Quantum Computing focus on spin qubits.

6. Neutral Atoms
    - Materials Used: Neutral atoms of elements such as rubidium (Rb) or cesium (Cs).
    - Mechanism: Atoms are held in place using optical tweezers (highly focused laser beams), and their quantum states are manipulated using additional laser interactions.
    - Example: Companies like QuEra and Pasqal use neutral atoms in optical lattices to create scalable qubit arrays.

These different qubit types each have unique advantages and challenges in terms of coherence times, scalability, and error rates, which play a large role in determining their suitability for various quantum computing applications.

{END IRL QUANTUM COMPUTING INFO FROM CHATGPT}

Some thoughs/TODO:

    * IDK if I am validating a quantum register correctly. I couldn't find an exact equation like the method used to validate an inidividual qudit;
    the implementation I have is a result of working with ChatGPT. I am assuming a valid qudit must have its individual measurement
    state probabilities sum to 1 (i.e. the sum of complex modulus for each complex number describing a qudit must sum to 1). This still allows
    for encoded states that may not ever be observable (i.e. have complex modulus/probability of 0).
    
    * IDK how to visualize all the states and ther probabilities (permutations may need a revisit smh)