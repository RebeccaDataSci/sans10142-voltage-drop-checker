
# Voltage Drop Calculator per SANS 10142
# Author: Rebecca Mosima
# Date: 2026-07-02
# Purpose: Merge cable data with SABS resistance tables to check Voltage drop compliance
# Input: cable_runs.csv, sabs_resistance.csv
# Output: voltage_drop_results.csv


import pandas as pd
import numpy as np

# import the datasets
data_1 = pd.read_csv("cable_runs.csv")

data_2 = pd.read_csv("sabs_resistance.csv")

# get details of the datsets
print(data_1.info())
print()
print(data_2.info())

# convert length from m to km
data_1["length_km"] = (data_1["length_m"]) / 1000

data_1 = data_1.drop(columns=["length_m"])

# merge the datasets
merged_data = pd.merge(data_1, data_2, on="conductor_size_mm2", how="inner")

print()
print(merged_data.head())

# calculate the voltage drop
merged_data["volt_drop"] = np.where(merged_data["phases"] == 1, 2 * merged_data["load_current_A"] * merged_data["resistance_ohm_per_km"] * merged_data["length_km"], np.sqrt(3)*merged_data["load_current_A"] *
                                    merged_data["resistance_ohm_per_km"]*merged_data["length_km"])


# calculate the voltage drop percentage
merged_data["volt_drop_percentage"] = (
    merged_data["volt_drop"]/merged_data["supply_voltage_V"])*100

# assign result status
merged_data["status"] = np.where(
    merged_data["volt_drop_percentage"] <= 5, "Acceptable", "Adjust cable size")

print()
print(merged_data.head())

# create a final results table
final_results = merged_data[["circuit_id", "phases",
                             "volt_drop", "volt_drop_percentage", "status"]].round(2)

# save the final results in a table
final_results.to_csv("voltage_drop_results.csv", index=False)


# print the results
print()
print("n\Report saved:voltage_drop_results.csv")
print(final_results)
