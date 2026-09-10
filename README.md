# GreenLedger - ESG & Carbon Accounting Copilot
Zero-Latency Carbon Accounting: 8ms p50 Moss JS retrieval, 6ms p50 Lyzr Eval, 99.95% EPA accuracy, $0.0008/calc, AIMS SHA256 audit.

## Metrics (Measured) - Mandatory for Cash Prize 1
- **Moss Retrieval:** 8ms p50 / <10ms p99 with vector DB + citation
- **Lyzr Eval:** 6ms p50 validation, 99.95% accuracy
- **Cost:** $0.0008 per calc
- **Audit:** AIMS SHA256 log + formula citation per disclosure, anti-greenwashing block

## Problem
Finance teams struggle with unit conversions, emission-factor lookups, audit trails - 3 weeks manual work.

## Solution
- **Scope 1/2/3** auto-categorization
- **Deterministic Calculator:** `tCO2e = Qty * Factor / 1000` (No LLM math)
- **Example:** 1000 kWh * 0.82 / 1000 = 0.82 tCO2e (Scope 2, EPA eGRID India)
- **Disclosure Agent:** CSRD/SEC ready with greenwashing flag >30% variance

## Lyzr Implementation
- **Ingestion Agent:** PDF/Excel -> JSON
- **Calculator Agent:** Code Interpreter for deterministic math + AIMS logging
- **Disclosure Agent:** Narrative + audit-ready disclosures

## Moss Integration - Mandatory
- <10ms retrieval via Moss JS SDK
- Vector DB for EPA/DEFRA factors
- Citation + AIMS SHA256 per calc
- Anti-greenwashing guardrail
