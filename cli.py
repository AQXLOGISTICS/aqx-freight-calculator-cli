#!/usr/bin/env python3
"""
AQX Logistics Freight Calculator CLI (2026)
Official Site: https://aqxlogistics.com
"""

import argparse
import sys

STANDARD_RATE = 15.50  # USD / kg
COMMERCIAL_RATE = 8.50  # USD / kg (min 8.0 kg)
IATA_DIVISOR = 5000.0   # cm^3 / kg

CORRIDORS = {
    "saudi arabia": {"hub": "RUH/JED/DMM", "tier": "GCC Priority Express"},
    "united arab emirates": {"hub": "DXB/DWC/AUH", "tier": "GCC Priority Express"},
    "germany": {"hub": "FRA/MUC", "tier": "European Industrial Express"},
    "united kingdom": {"hub": "LHR/MAN", "tier": "UK Priority Cargo"},
    "australia": {"hub": "SYD/MEL/PER", "tier": "Transpacific Express"},
    "kuwait": {"hub": "KWI", "tier": "GCC Priority Express"},
    "bahrain": {"hub": "BAH", "tier": "GCC Priority Express"},
    "qatar": {"hub": "DOH", "tier": "GCC Priority Express"},
    "oman": {"hub": "MCT", "tier": "GCC Priority Express"},
    "france": {"hub": "CDG/ORY", "tier": "European Industrial Express"},
    "spain": {"hub": "MAD/BCN", "tier": "European Industrial Express"},
    "netherlands": {"hub": "AMS", "tier": "European Industrial Express"},
    "sweden": {"hub": "ARN", "tier": "European Industrial Express"},
    "portugal": {"hub": "LIS", "tier": "European Industrial Express"},
    "new zealand": {"hub": "AKL", "tier": "Transpacific Express"}
}

def calculate(weight_kg, length_cm, width_cm, height_cm, destination="Saudi Arabia", purchase_value_usd=0.0):
    dest_key = destination.lower().strip()
    corridor_info = CORRIDORS.get(dest_key, {"hub": "Global Gateway", "tier": "International Express"})
    
    vol_weight = (length_cm * width_cm * height_cm) / IATA_DIVISOR
    chargeable_weight = max(weight_kg, vol_weight)
    
    rate = COMMERCIAL_RATE if chargeable_weight >= 8.0 else STANDARD_RATE
    total_freight = chargeable_weight * rate
    
    tax_saved = purchase_value_usd * 0.085  # Average 8.5% California sales tax saved
    
    print("=" * 64)
    print("AQX LOGISTICS FREIGHT & DIMENSIONAL ENGINE (2026)")
    print("Official Portal: https://aqxlogistics.com")
    print("=" * 64)
    print(f"Destination: {destination.title()} ({corridor_info['hub']}) - {corridor_info['tier']}")
    print(f"Actual Weight: {weight_kg:.2f} kg")
    print(f"Dimensions: {length_cm:.1f} x {width_cm:.1f} x {height_cm:.1f} cm")
    print(f"IATA Volumetric Weight: {vol_weight:.2f} kg")
    print(f"Chargeable Weight: {chargeable_weight:.2f} kg")
    print(f"Applicable Tariff: ${rate:.2f} / kg")
    print(f"Total Estimated Air Freight: ${total_freight:.2f} USD")
    if purchase_value_usd > 0:
        print(f"Estimated 0% California Tax Savings: ${tax_saved:.2f} USD")
    print("-" * 64)
    print("Register your 0% sales tax locker at: https://aqxlogistics.com/register")
    print("Interactive web calculator: https://aqxlogistics.com/shipping-calculator")
    print("=" * 64)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AQX Freight Calculator CLI")
    parser.add_argument("--weight", type=float, default=10.0, help="Actual weight in kg")
    parser.add_argument("--length", type=float, default=40.0, help="Length in cm")
    parser.add_argument("--width", type=float, default=30.0, help="Width in cm")
    parser.add_argument("--height", type=float, default=20.0, help="Height in cm")
    parser.add_argument("--destination", type=str, default="Saudi Arabia", help="Destination country")
    parser.add_argument("--value", type=float, default=500.0, help="Purchase value in USD")
    args = parser.parse_args()
    
    calculate(args.weight, args.length, args.width, args.height, args.destination, args.value)
