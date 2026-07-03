# SANS 10142 Voltage Drop Checker

Python tool that calculates voltage drop for single-phase and 3-phase cable runs and checks compliance with SANS 10142-1 Section 6.2.7.

## What is voltage drop?
Voltage drop is the reduction in voltage from the supply to the load. It occurs due to conductor length, resistivity of the material, and current drawn by the load.

A significant voltage drop results in under-voltage at the load. To deliver the same power `P = V × I`, the load then draws more current. This increased current can overheat conductors, damage equipment, and cause protection devices to fail.

It also hits efficiency: if 8% of voltage is lost in the cable, the load only uses 92% of the supplied voltage — but the consumer pays for 100%.

## What this script does
This tool automates SANS 10142 compliance checks:

- Calculates voltage drop using: 
    - Single-phase: `Vd = 2 × I × R × L`
    - Three-phase: `Vd = √3 × I × R × L`
- Compares results against the SANS 10142 limit of ≤5% of supply voltage
- Flags each cable run as `Acceptable` or `Adjust cable size` in the output report
- Exports a full report to `voltage_drop_results.csv` for documentation/COC
- Identifies runs where cable size should be increased to meet code

## How to run
```bash
python sans10142_voltage_drop_checker.py
