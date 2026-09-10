# GreenLedger - ESG & Carbon Accounting Copilot
PS-01 | AI Quest by Lyzr | ClimateTech

Ingest invoices and ERP logs, classify Scope 1/2/3 emissions with official factors, block greenwashing, and emit audit-ready CSRD/SEC disclosures.

## CONTEXT
CSRD, CSDDD, and SEC climate rules raise penalties for greenwashing and bad GHG accounting. LLMs struggle with unit conversions, emission-factor lookups, audit lineage, and supplier PII.

## ARCHITECTURE
01 Document Ingestion: Ingest utility bills, invoices, freight logs, and tabular ERP data.
02 Scope Categorization: Classify line items into GHG Protocol Scope 1 / 2 / 3.
03 Emission Factor Matching: Bind activities to official EPA eGRID / DEFRA factor tables.
04 Deterministic Math + Safe AI: Arithmetic via verified calculation tools—not LLM token math—with PII protection.
05 Disclosure Report: CSRD/SEC-ready dossier with formula citations and AIMS governance log.

## Lyzr Implementation
- Ingestion Agent: Uses Lyzr Data Analysis Agent to parse CSV/Excel/PDF
- Calculator Agent: Uses Code Interpreter for tCO2e = Qty * Factor / 1000. No LLM math.
- Disclosure Agent: Generates audit trail and flags greenwashing if reduction >30%

Sample: 1000 kWh * 0.82 / 1000 = 0.82 tCO2e (Scope 2, EPA eGRID India)
Sample: 500 L Diesel * 2.68 / 1000 = 1.34 tCO2e (Scope 1, DEFRA 2024)

## Lyzr Stack
Lyzr Data Analysis Agent, Lyzr Safe AI, Lyzr Agent Studio, Lyzr Agent API

## Judging Rubric
30% Lyzr Architecture & Tool Calling, 30% Accuracy, 20% Auditability, 20% Dashboard UX
