# ============================================================
# DWSIM PFR AUTOMATION
# 3000 CASES

# Reaction:
# CH3CHO -> CH4 + CO
#
# Variables:
# Temperature
# Pressure
# Reactor Volume

# Results:
# Feed CH3CHO
# Product CH3CHO
# Conversion
# PFR Heat Load
# PFR Residence Time

# 1.GET DWSIM OBJECTS:


feed = Flowsheet.GetFlowsheetSimulationObject("1")
reactor = Flowsheet.GetFlowsheetSimulationObject("PFR_1")
product = Flowsheet.GetFlowsheetSimulationObject("3")

ws = Spreadsheet.Worksheets[0]

# 2.SPREADSHEET HEADERS:

ws.Cells["A1"].Data = "Case"
ws.Cells["B1"].Data = "Temperature (K)"
ws.Cells["C1"].Data = "Pressure (Pa)"
ws.Cells["D1"].Data = "Volume (m3)"
ws.Cells["E1"].Data = "Feed CH3CHO (mol/s)"
ws.Cells["F1"].Data = "Product CH3CHO (mol/s)"
ws.Cells["G1"].Data = "Conversion (%)"
ws.Cells["H1"].Data = "Heat Load (kW)"
ws.Cells["I1"].Data = "Residence Time (s)"
ws.Cells["J1"].Data = "Status"

# 3.AUTOMATION SETTINGS:

# Temperature range(K)
T_start = 940.0
T_end = 960.0
T_step = 0.2

# Pressure range (PA)
P_start = 31330.0
P_end = 33330.0
P_step = 100.0

# Reactor volume range(M3)
V_start = 0.90
V_end = 1.10
V_step = 0.02

# Maximum number of simulations
max_cases = 3000
case_no = 0

# 4.TEMPERATURE>PRESSURE>REACTOR VOLUME LOOP:

T = T_start

while T <= T_end and case_no < max_cases:

    # RESET PRESSURE FOR NEW TEMPERATURE

    P = P_start

    while P <= P_end and case_no < max_cases:

        # RESET VOLUME FOR NEW PRESSURE

        V = V_start

        while V <= V_end and case_no < max_cases:

            case_no += 1
            row = case_no + 1

            try:

                
                feed.SetTemperature(T)
                feed.SetPressure(P)
                reactor.Volume = V

                # SOLVE FLOWSHEET

                Flowsheet.SolveFlowsheet2()

                # FEED CH3CHO

                feed_phase = feed.Phases[0]

                feed_total = feed_phase.Properties.molarflow

                feed_A = None

                for comp in feed_phase.Compounds.Values:

                    if comp.Name == "Acetaldehyde":

                        feed_A = (comp.MoleFraction* feed_total)
                        break

                # PRODUCT CH3CHO

                product_phase = product.Phases[0]

                product_total = (product_phase.Properties.molarflow)

                product_A = None

                for comp in product_phase.Compounds.Values:

                    if comp.Name == "Acetaldehyde":
                        product_A = ( comp.MoleFraction* product_total)
                        break

                # CHECK ACETALDEHYDE VALUES

                if feed_A is None:

                    raise Exception(
                        "Feed Acetaldehyde not found"
                    )

                if product_A is None:

                    raise Exception(
                        "Product Acetaldehyde not found"
                    )

                if feed_A <= 0:

                    raise Exception(
                        "Invalid feed CH3CHO flow"
                    )

                # CALCULATE CONVERSION

                conversion = ((feed_A - product_A)/ feed_A) * 100.0

                # GET HEAT LOAD DIRECTLY FROM PFR
                heat_load = reactor.DeltaQ

                # GET RESIDENCE TIME DIRECTLY FROM PFR
                residence_time = reactor.ResidenceTime

                # CHECK CONVERSION

                if conversion < 0.0 or conversion > 100.0:

                 # INVALID RESULT

                    ws.Cells[
                        "A" + str(row)
                    ].Data = case_no

                    ws.Cells[
                        "B" + str(row)
                    ].Data = T

                    ws.Cells[
                        "C" + str(row)
                    ].Data = P

                    ws.Cells[
                        "D" + str(row)
                    ].Data = V

                    ws.Cells[
                        "E" + str(row)
                    ].Data = None

                    ws.Cells[
                        "F" + str(row)
                    ].Data = None

                    ws.Cells[
                        "G" + str(row)
                    ].Data = None

                    ws.Cells[
                        "H" + str(row)
                    ].Data = None

                    ws.Cells[
                        "I" + str(row)
                    ].Data = None

                    ws.Cells[
                        "J" + str(row)
                    ].Data = "NULL"


                else:

                    # VALID RESULT

                    ws.Cells[
                        "A" + str(row)
                    ].Data = case_no

                    ws.Cells[
                        "B" + str(row)
                    ].Data = T

                    ws.Cells[
                        "C" + str(row)
                    ].Data = P

                    ws.Cells[
                        "D" + str(row)
                    ].Data = V

                    ws.Cells[
                        "E" + str(row)
                    ].Data = feed_A

                    ws.Cells[
                        "F" + str(row)
                    ].Data = product_A

                    ws.Cells[
                        "G" + str(row)
                    ].Data = conversion

                    ws.Cells[
                        "H" + str(row)
                    ].Data = heat_load

                    ws.Cells[
                        "I" + str(row)
                    ].Data = residence_time

                    ws.Cells[
                        "J" + str(row)
                    ].Data = "OK"

            # IF DWSIM SOLVE FAILS

            except:

                ws.Cells[
                    "A" + str(row)
                ].Data = case_no

                ws.Cells[
                    "B" + str(row)
                ].Data = T

                ws.Cells[
                    "C" + str(row)
                ].Data = P

                ws.Cells[
                    "D" + str(row)
                ].Data = V

                ws.Cells[
                    "E" + str(row)
                ].Data = None

                ws.Cells[
                    "F" + str(row)
                ].Data = None

                ws.Cells[
                    "G" + str(row)
                ].Data = None

                ws.Cells[
                    "H" + str(row)
                ].Data = None

                ws.Cells[
                    "I" + str(row)
                ].Data = None

                ws.Cells[
                    "J" + str(row)
                ].Data = "NULL"


            # INCREASE VOLUME
            V += V_step

        # INCREASE PRESSURE
        P += P_step

    # INCREASE TEMPERATURE

    T += T_step

# AUTOMATION SUMMARY

ws.Cells["L1"].Data = "Automation Summary"
ws.Cells["L2"].Data = "Total Cases"
ws.Cells["M2"].Data = case_no
ws.Cells["L3"].Data = "Temperature Range"
ws.Cells["M3"].Data = (
    str(T_start)
    + " - "
    + str(T_end)
    + " K")

ws.Cells["L4"].Data = "Pressure Range"
ws.Cells["M4"].Data = (
    str(P_start)
    + " - "
    + str(P_end)
    + " Pa"
)
ws.Cells["L5"].Data = "Volume Range"
ws.Cells["M5"].Data = (
    str(V_start)
    + " - "
    + str(V_end)
    + " m3"
)

ws.Cells["L6"].Data = "Message"

ws.Cells["M6"].Data = ("3000-case automation completed")