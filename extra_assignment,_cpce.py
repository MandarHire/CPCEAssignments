# -*- coding: utf-8 -*-
"""Extra Assignment, CPCE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lyLf2ndX7pwgTo7ub-o5k1MQdtEKSp83
"""

import math

# Input parameters
length = float(input("Enter the length of the column (in meters): "))
diameter = float(input("Enter the diameter of the column (in meters): "))
applied_force = float(input("Enter the applied axial force (in Newtons): "))
material_yield_strength = float(input("Enter the yield strength of the material (in Pascals): "))

# Calculate the column's cross-sectional area
cross_sectional_area = (math.pi / 4) * (diameter ** 2)

# Calculate critical load using Euler's formula
critical_load = (math.pi ** 2) * material_yield_strength * (diameter ** 2) / (4 * (length ** 2))

# Determine if the column is safe or will buckle
if applied_force <= critical_load:
    print("The column is safe. Applied load is below the critical load.")
else:
    print("The column is not safe. Applied load exceeds the critical load.")

class WaterTreatmentPlant:
    def __init__(self, raw_water_source):
        self.raw_water_source = raw_water_source
        self.treated_water = []

    def intake_water(self, volume):
        print(f"Intaking {volume} cubic meters of raw water from {self.raw_water_source}.")
        self.treated_water = [volume]

    def coagulation(self):
        print("Coagulation process: Adding chemicals to aid particle clumping.")

    def sedimentation(self):
        print("Sedimentation process: Allowing particles to settle.")

    def filtration(self):
        print("Filtration process: Removing remaining impurities.")

    def distribute_water(self):
        print(f"Distributing {self.treated_water[0]} cubic meters of treated water.")

def main():
    plant = WaterTreatmentPlant("River XYZ")
    plant.intake_water(1000)  # Intake 1000 cubic meters of raw water
    plant.coagulation()
    plant.sedimentation()
    plant.filtration()
    plant.distribute_water()

if __name__ == "__main__":
    main()