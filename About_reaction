## ⚗️ Reaction and Kinetic Basis

The reactor model considers the gas-phase thermal decomposition of acetaldehyde:

CH₃CHO(g) → CH₄(g) + CO(g)

Acetaldehyde decomposition is a temperature-dependent gas-phase reaction. 
The reaction rate increases strongly with temperature because the rate constant 
follows the Arrhenius relationship:

k = A exp(-Ea / RT)

where:

- k = reaction rate constant
- A = pre-exponential (frequency) factor
- Ea = activation energy
- R = universal gas constant
- T = absolute temperature

For the DWSIM reactor simulations, the following kinetic parameters were adopted:

| Parameter | Value |
|---|---:|
| Activation energy, Ea | 182,000 J/mol |
| Pre-exponential factor, A | 19 × 10⁶ |
| Temperature | Varied across the simulation range |
| Reaction | CH₃CHO → CH₄ + CO |

The selected kinetic parameters were used consistently across the DWSIM
simulation cases so that the generated dataset represents changes in reactor
performance caused by changes in operating conditions rather than changes in
the underlying reaction kinetics.

## 🌡️ Temperature Selection

Temperature was treated as one of the major operating variables because the
Arrhenius equation predicts a strong dependence of the reaction rate on
temperature.

The simulation temperature range was selected to provide a meaningful change
in reaction rate and conversion while remaining within the intended operating
range of the reactor model.

Using multiple temperature levels allows the ML dataset to capture the
relationship between temperature, reaction kinetics, residence time, and
conversion.

The temperature range was therefore not selected as a single arbitrary
operating point. Multiple values were generated to provide sufficient
variation for process analysis and machine-learning model development.

### Arrhenius Parameter Selection

The DWSIM model uses Ea = 182 kJ/mol and A = 19 × 10⁶
as the adopted kinetic parameters for the simulation study.

These parameters were kept fixed throughout the automated simulation
campaign. The purpose of the study was to investigate how reactor operating
variables influence conversion under a consistent kinetic model.

The values should therefore be interpreted as model inputs rather than
independently re-estimated kinetic parameters in this project.

## 📚 References

1. Chemical Kinetics and PFR Reactor Basics.
   Project reference material covering Arrhenius kinetics, reaction-rate
   determination, experimental planning, temperature selection, and PFR
   fundamentals.

2. DWSIM User Guide, Version 10.2.1 (August 2026).
   Used as the reference for DWSIM process simulation and reactor modelling.

3. Eusuf, M. & Laidler, K. J. (1964).
   "Kinetics and Mechanisms of the Thermal Decomposition of Acetaldehyde:
   I. The Uninhibited Reaction."
   Canadian Journal of Chemistry.
   DOI: 10.1139/v64-276.

4. Trenwith, A. B. (1963).
   "The thermal decomposition of acetaldehyde: the formation of hydrogen."
   Journal of the Chemical Society, pages 4426–4430.
   NIST Chemical Kinetics Database record.

5. Standard chemical kinetics references describing the Arrhenius equation
   and the thermal decomposition of acetaldehyde.
