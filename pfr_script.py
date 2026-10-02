print("=== START ===")
feed = Flowsheet.GetFlowsheetSimulationObject("1")
reactor = Flowsheet.GetFlowsheetSimulationObject("PFR_1")
product = Flowsheet.GetFlowsheetSimulationObject("3")
# Constants
A = 19e6
E = 182000.0
R = 8.314462618
T = feed.Phases[0].Properties.temperature 
phase = feed.Phases[0]
k = A * 2.7**(-E / (R * T))
print(k)

for c in phase.Compounds:
    if c.Key == "Acetaldehyde":
        acetaldehyde = c.Value
        ca = acetaldehyde.MolarFlow/acetaldehyde.VolumetricFlow

r = k * ca**1.5
print("rate:",r)
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

