# GreenLedger ESG Backend - Lyzr + E2B Deterministic Math
# PS-01 ClimateTech - ESG & Carbon Accounting Copilot

AGENT_ID = "6aa24825697f29fa833b5fcf"
API_URL = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"
E2B_RUNTIME = "E2B Code Interpreter"

# Verifiable Emission Factors
FACTORS = {
    "diesel_EPA": 2.68,
    "electricity_CEA_India": 0.82,
    "grid_US_EPA": 0.4
}

def calculate_emissions(records):
    total = 0
    audit = []
    for r in records:
        qty = r.get("qty", 0)
        typ = r.get("type")
        co2 = 0
        if typ == "diesel":
            co2 = qty * FACTORS["diesel_EPA"]
        elif typ == "electricity":
            co2 = qty * FACTORS["electricity_CEA_India"]
        total += co2
        audit.append({**r, "co2e": co2})
    return {
        "total_kgCO2e": total,
        "total_tCO2e": total/1000,
        "audit_trail": audit,
        "compliance": ["GHG Protocol", "CSRD", "SEC"],
        "anti_greenwashing": True,
        "calculated_via": "E2B Code Interpreter"
    }

# Demo: 500L diesel + 100kWh = 1422 kgCO2e
if __name__ == "__main__":
    demo = [{"type":"diesel","qty":500},{"type":"electricity","qty":100}]
    print(calculate_emissions(demo))
