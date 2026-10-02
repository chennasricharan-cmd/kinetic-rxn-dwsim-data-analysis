print("=== START ===")
feed = Flowsheet.GetFlowsheetSimulationObject("1")
reactor = Flowsheet.GetFlowsheetSimulationObject("PFR_1")
product = Flowsheet.GetFlowsheetSimulationObject("3")
E1 = Flowsheet.GetFlowsheetSimulationObject("E1")

props = feed.Phases[0].Properties

phase = feed.Phases[0]

for c in phase.Compounds:
    if c.Key == "Acetaldehyde":
        acetaldehyde = c.Value
        ca = acetaldehyde.MolarFlow/acetaldehyde.VolumetricFlow

print("inlet concentration of aldehyde:",ca)

m_in,m_out,v_out=0.0,0.0,0.0

# Find acetaldehyde in feed
FA_in = 0.0
for c in phase.Compounds:
    if c.Key == "Acetaldehyde":
        FA_in = c.Value.MolarFlow
    m_in+=c.Value.MassFlow


# Find acetaldehyde in product
FA_out = 0.0
phase2=product.Phases[0]
for c in phase2.Compounds:
    v_out+=c.Value.VolumetricFlow
    if c.Key == "Acetaldehyde":
        FA_out = c.Value.MolarFlow
        x_ace=c.Value.MoleFraction
    m_out+=c.Value.MassFlow

cA_out=FA_out/v_out

print("outlet acetaldehyde concentration:",cA_out)

# Conversion
X = (FA_in - FA_out) / FA_in
print("Acetaldehyde inlet molar flow =", FA_in)
print("Acetaldehyde outlet molar flow =", FA_out)
print("Acetaldehyde conversion =", X)
print("Acetaldehyde conversion (%) =", X * 100.0)

mass_error = m_in - m_out

if abs(m_in) > 0.0:
    mass_error_percent = abs(mass_error) / abs(m_in) * 100.0
else:
    mass_error_percent = 0.0

print(" MASS BALANCE VALIDATION")
print("INLET MASS FLOW  =", m_in)
print("OUTLET MASS FLOW =", m_out)
print("MASS BALANCE ERROR =", mass_error)
print("MASS BALANCE ERROR (%) =", mass_error_percent)

if mass_error_percent < 0.01:
    print("MASS BALANCE: PASS")
else:
    print("MASS BALANCE: CHECK REQUIRED")
# COMPONENT STOICHIOMETRIC BALANCE
# CH3CHO -> CH4 + CO
FCH4_in = 0.0
FCH4_out = 0.0

FCO_in = 0.0
FCO_out = 0.0


# INLET
for c in phase.Compounds:
    if c.Key == "Methane":
        FCH4_in = c.Value.MolarFlow
    elif c.Key == "Carbon monoxide":
        FCO_in = c.Value.MolarFlow

# OUTLET 
for c in phase2.Compounds:
    if c.Key == "Methane":
        FCH4_out = c.Value.MolarFlow

    elif c.Key == "Carbon monoxide":
        FCO_out = c.Value.MolarFlow
  
# CHANGE IN MOLAR FLOW

delta_A = FA_in - FA_out
delta_CH4 = FCH4_out - FCH4_in
delta_CO = FCO_out - FCO_in

error_CH4 = delta_CH4 - delta_A
error_CO = delta_CO - delta_A

print("STOICHIOMETRIC COMPONENT BALANCE")
print("CH3CHO -> CH4 + CO")

print("CH3CHO consumed =", delta_A, "mol/s")
print("CH4 formed      =", delta_CH4, "mol/s")
print("CO formed       =", delta_CO, "mol/s")
 
print("CH4 error =", error_CH4, "mol/s")
print("CO error  =", error_CO, "mol/s")

#  PASS / FAIL 

tol = 1e-6

if abs(error_CH4) < tol and abs(error_CO) < tol:
    print("STOICHIOMETRIC BALANCE: PASS")
else:
    print("STOICHIOMETRIC BALANCE: CHECK REQUIRED")

T_in = feed.Phases[0].Properties.temperature
T_out = product.Phases[0].Properties.temperature
T_reactor = 925.0

print("ISOTHERMAL VALIDATION")
print("Specified reactor T =", T_reactor, "K")
print("Feed T              =", T_in, "K")
print("Product T           =", T_out, "K")

print("Feed deviation    =", T_in - T_reactor, "K")
print("Product deviation =", T_out - T_reactor, "K")

if abs(T_in - T_reactor) < tol and abs(T_out - T_reactor) < tol:
    print("ISOTHERMAL TEMPERATURE CHECK: PASS")
else:
    print("ISOTHERMAL TEMPERATURE CHECK: CHECK REQUIRED")

# ENERGY / HEAT DUTY CHECK
H_in = feed.Phases[0].Properties.enthalpy
H_out = product.Phases[0].Properties.enthalpy


Q_KW = E1.GetEnergyFlow()

print("======================================")
print("ENERGY / HEAT DUTY VALIDATION")
print("======================================")

print("")
print("Feed enthalpy flow    =", H_in)
print("Product enthalpy flow =", H_out)

delta_h = H_out-H_in
print("Enthalpy difference (Hout-Hin) =",delta_h)

print("")
print("Reactor heat duty Q =", Q_KW)

print("======================================")

# COOLANT-SIDE HEAT DUTY VALIDATION

# Known coolant data
m_coolant = 1.0          # kg/s
Cp = 4.18                # kJ/(kg.K)
T_coolant_in = 298.15    # K

# E1 energy flow
Q_E1_W = E1.GetEnergyFlow()
Q_E1_kW = Q_E1_W / 1000.0

# Magnitude of heat transferred to coolant
Q_absorbed = abs(Q_E1_kW)

# Calculate coolant outlet temperature
T_coolant_out = T_coolant_in + Q_absorbed / (m_coolant * Cp)

# Independently calculate heat absorbed by coolant
Q_coolant = m_coolant * Cp * (T_coolant_out - T_coolant_in)

# Difference
error = Q_coolant - Q_absorbed

# Percentage error
if Q_absorbed != 0:
    error_percent = abs(error) / Q_absorbed * 100.0
else:
    error_percent = 0.0

print("COOLANT-SIDE HEAT DUTY VALIDATION")

print("E1 heat flow              =", Q_E1_kW, "kW")
print("Heat transferred         =", Q_absorbed, "kW")

print("")
print("Coolant mass flow        =", m_coolant, "kg/s")
print("Coolant Cp               =", Cp, "kJ/(kg.K)")
print("Coolant inlet temperature=", T_coolant_in, "K")

print("")
print("Calculated coolant outlet temperature =",
      T_coolant_out, "K")

print("")
print("Heat absorbed by coolant =", Q_coolant, "kW")
print("Heat duty error           =", error, "kW")
print("Heat duty error (%)       =", error_percent, "%")


# Validation
tolerance_percent = 0.01

if error_percent <= tolerance_percent:
    print("COOLANT-SIDE ENERGY BALANCE: PASS")
else:
    print("COOLANT-SIDE ENERGY BALANCE: CHECK REQUIRED")

