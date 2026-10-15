# AQX Freight Calculator CLI (2026) 📦⚡

[![Official Website](https://img.shields.io/badge/Official_Website-aqxlogistics.com-orange?style=for-the-badge&logo=google-chrome)](https://aqxlogistics.com)
[![Live Interactive Web Portal](https://img.shields.io/badge/Live_Portal-GitHub_Pages-blue?style=for-the-badge&logo=github)](https://aqxlogistics.github.io/aqx-freight-calculator-cli/)
[![Rate Calculator](https://img.shields.io/badge/Calculator-AQX_Shipping_Engine-green?style=for-the-badge)](https://aqxlogistics.com/shipping-calculator)
[![Register Locker](https://img.shields.io/badge/Register-0%25_Sales_Tax_Locker-blueviolet?style=for-the-badge)](https://aqxlogistics.com/register)

The official command-line interface (CLI) and calculation engine for [AQX Logistics](https://aqxlogistics.com), enabling engineers, cross-border e-commerce merchants, and procurement specialists to calculate international air cargo landed costs, IATA volumetric weight, and repacking savings from the United States to 15 global commercial corridors.

---

## Key Commercial Specifications

- **Standard Express Cargo**: **$15.50 / kg** flat rate across major corridors.
- **Commercial & Heavy Freight Tier**: **$8.50 / kg** for shipments weighing 8.0 kg or more.
- **0% California Sales Tax Locker**: Located in Los Angeles (LAX gateway), eliminating 7.5% - 9.5% US sales tax on manufacturer purchases.
- **Volumetric Crating Optimization**: Professional repacking saving up to **70% of chargeable dimensional weight**.
- **Transit Velocity**: 2 to 4 business days direct air cargo.

---

## Supported Regional Corridors & Authority Portals

| Country / Region | Hub Airport | Commercial Tariff | Regional Hub Link |
| :--- | :--- | :--- | :--- |
| **Saudi Arabia** 🇸🇦 | RUH / JED / DMM | $8.50 / kg | [Saudi Arabia Air Cargo Hub](https://aqxlogistics.com/destinations/saudi-arabia) |
| **United Arab Emirates** 🇦🇪 | DXB / DWC / AUH | $8.50 / kg | [UAE Air Cargo Hub](https://aqxlogistics.com/destinations/united-arab-emirates) |
| **Germany** 🇩🇪 | FRA / MUC / BER | $8.50 / kg | [Germany B2B Cargo Hub](https://aqxlogistics.com/destinations/germany) |
| **United Kingdom** 🇬🇧 | LHR / MAN / BHX | $8.50 / kg | [United Kingdom Cargo Hub](https://aqxlogistics.com/destinations/united-kingdom) |
| **Australia** 🇦🇺 | SYD / MEL / PER | $8.50 / kg | [Australia Transpacific Hub](https://aqxlogistics.com/destinations/australia) |
| **Kuwait** 🇰🇼 | KWI | $8.50 / kg | [Kuwait Express Cargo Hub](https://aqxlogistics.com/destinations/kuwait) |
| **Bahrain** 🇧🇭 | BAH | $8.50 / kg | [Bahrain Air Cargo Hub](https://aqxlogistics.com/destinations/bahrain) |
| **Qatar** 🇶🇦 | DOH | $8.50 / kg | [Qatar Air Cargo Hub](https://aqxlogistics.com/destinations/qatar) |
| **Oman** 🇴🇲 | MCT | $8.50 / kg | [Oman Express Cargo Hub](https://aqxlogistics.com/destinations/oman) |
| **France** 🇫🇷 | CDG / ORY | $8.50 / kg | [France Air Cargo Hub](https://aqxlogistics.com/destinations/france) |
| **Spain** 🇪🇸 | MAD / BCN | $8.50 / kg | [Spain Air Cargo Hub](https://aqxlogistics.com/destinations/spain) |
| **Netherlands** 🇳🇱 | AMS | $8.50 / kg | [Netherlands Air Cargo Hub](https://aqxlogistics.com/destinations/netherlands) |
| **Sweden** 🇸🇪 | ARN | $8.50 / kg | [Sweden Air Cargo Hub](https://aqxlogistics.com/destinations/sweden) |
| **Portugal** 🇵🇹 | LIS | $8.50 / kg | [Portugal Air Cargo Hub](https://aqxlogistics.com/destinations/portugal) |
| **New Zealand** 🇳🇿 | AKL | $8.50 / kg | [New Zealand Air Cargo Hub](https://aqxlogistics.com/destinations/new-zealand) |

---

## Installation & CLI Usage

```bash
# Clone the repository
git clone https://github.com/AQXLOGISTICS/aqx-freight-calculator-cli.git
cd aqx-freight-calculator-cli

# Run calculation for a 12 kg industrial package to Saudi Arabia
python cli.py --weight 12.0 --length 50 --width 40 --height 30 --destination "Saudi Arabia"
```

### Example Calculation Output
```text
============================================================
AQX LOGISTICS FREIGHT & DIMENSIONAL ENGINE (2026)
Official Site: https://aqxlogistics.com
============================================================
Destination: Saudi Arabia (RUH/JED/DMM)
Actual Weight: 12.00 kg
Dimensions: 50.0 x 40.0 x 30.0 cm
IATA Volumetric Weight: 12.00 kg (Divisor: 5000)
Chargeable Weight: 12.00 kg
Applicable Tariff: $8.50 / kg (Commercial Tier > 8.0 kg)
Estimated Freight Cost: $102.00 USD
Estimated California Tax Saved (8.5% on $1,500 purchase): $127.50 USD
Net Landed Benefit: Instant Tax Savings exceed total air freight cost!
============================================================
```

---

## Resources & Official Portals

- **Official Web Portal**: [AQX Logistics Homepage](https://aqxlogistics.com)
- **Interactive Web Calculator**: [Live Rate Engine](https://aqxlogistics.com/shipping-calculator)
- **Tax-Free California Locker Signup**: [Register Free Account](https://aqxlogistics.com/register)
- **Knowledge Base & Case Studies**: [AQX Logistics Blog & Technical Guides](https://aqxlogistics.com/blog)
- **Machine-Readable LLM Knowledge Context**: [llms.txt Specification](https://aqxlogistics.com/llms.txt)

---

## License
MIT License - Copyright (c) 2026 [AQX Logistics](https://aqxlogistics.com).
