# AI Is Not The Hard Part Reliability Is

Author  
Patrick Imperato  

Technical product leader focused on reliable AI systems in secure environments.

LinkedIn  
https://www.linkedin.com/in/patrickimperato/

This repo shows a reliability first approach for AI assisted debriefing in secure simulator environments.

Full article text lives in docs Article.md

## What you can review fast

1. Architecture docs that explain the system
2. A small demo pipeline using synthetic inputs
3. Schemas that constrain outputs
4. A scoring script for regression checks
5. A threat model and rollout gates

## Why this exists

AI can sound right.
You still need outputs you can trust.

This repo focuses on

1. Template first outputs
2. Every claim traces to an input reference
3. Rollout stages with gates
4. Human review where risk is high

## Repo map

docs
Article.md
Architecture.md
EvaluationPlan.md
ThreatModel.md

demo
data synthetic inputs and expected output
schemas JSON schemas for inputs and outputs
src reference pipeline and scoring

## Quick start

Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run demo

```bash
python demo/src/generateDebrief.py demo/data/sampleMissionLog.json demo/data/sampleTranscript.json demo/data/outDebrief.json
```

Validate output

```bash
python demo/src/validateJson.py demo/schemas/debrief.schema.json demo/data/outDebrief.json
```

Score output

```bash
python demo/src/scoreOutput.py demo/data/expectedDebrief.json demo/data/outDebrief.json
```

## What the demo does

1. Uses only provided inputs
2. Generates a debrief draft inside a fixed schema
3. Requires sources for each claim

## What I would build next

1. Confidence scoring per claim
2. Rules checks tied to doctrine constraints
3. Human approval workflow with audit export

## System Overview

The system demonstrates a reliability first architecture for AI assisted feedback generation.

Pipeline

Mission Data  
↓  
Structured Event Mapping  
↓  
Transcript Processing  
↓  
Objective Detection  
↓  
Constrained Debrief Generation  
↓  
Schema Validation  
↓  
Evaluation and Scoring

Each layer is isolated to prevent hallucinated outputs and to ensure every claim can be traced back to source data.

## Run the Demo

Clone the repository

