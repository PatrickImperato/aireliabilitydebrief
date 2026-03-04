# AI Is Not The Hard Part Reliability Is

A reliability first architecture for AI assisted training debrief generation in secure simulator environments.

Author  
Patrick Imperato

Technical product leader focused on reliable AI systems in secure environments.

LinkedIn  
https://www.linkedin.com/in/patrickimperato/

Original article  
[LinkedIn Article](https://www.linkedin.com/pulse/ai-hard-partreliability-patrick-imperato-8idwc/)

---

## Overview

This repository demonstrates a reliability first architecture for AI assisted training debrief generation inside secure simulator environments.

The purpose is not to build a large model system. The purpose is to show how AI outputs can be made traceable, constrained, and auditable in environments where correctness matters.

The repository includes

1. Architecture documentation  
2. A working demo pipeline  
3. Schema constrained outputs  
4. Output validation  
5. Evaluation metrics  

Full article text is located in

docs/Article.md

---

## System Overview

The system demonstrates a reliability first pipeline for AI assisted debrief generation.

Pipeline flow

Mission Data  
→ Structured Event Mapping  
→ Transcript Processing  
→ Objective Detection  
→ Constrained Debrief Generation  
→ Schema Validation  
→ Evaluation and Scoring  

Each layer isolates model behavior so every output can be traced to its source data.

Architecture description

[System Architecture](assets/systemArchitecture.md)

---

## Repository Structure

```
assets/
    systemArchitecture.md

demo/
    data/
        expectedDebrief.json
        sampleMissionLog.json
        sampleTranscript.json
        outputDebrief.json

    schemas/
        debrief.schema.json
        missionLog.schema.json
        transcript.schema.json

    src/
        generateDebrief.py
        validateJson.py
        scoreOutput.py

docs/
    Article.md
    Architecture.md
    EvaluationPlan.md
    Glossary.md
    References.md
    ThreatModel.md

LICENSE
README.md
requirements.txt
```

---

## Run the Demo

### Download the repository

Option 1  
Download ZIP from the green Code button on GitHub.

Option 2  
Clone using git

```bash
git clone https://github.com/PatrickImperato/aireliabilitydebrief.git
cd aireliabilitydebrief
```

---

### Create a Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

When activated your terminal should show

```
(.venv)
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

The demo only requires the jsonschema package.

---

### Generate a debrief

Run the generator script.

```bash
python3 demo/src/generateDebrief.py demo/data/sampleMissionLog.json demo/data/sampleTranscript.json demo/data/outputDebrief.json
```

The generated output file will appear at

```
demo/data/outputDebrief.json
```

---

### Validate the output

Validate the generated JSON using the schema.

```bash
python3 demo/src/validateJson.py demo/schemas/debrief.schema.json demo/data/outputDebrief.json
```

Expected result

```
Validation passed
```

---

### Score the output

Compare the generated output with the expected reference output.

```bash
python3 demo/src/scoreOutput.py demo/data/expectedDebrief.json demo/data/outputDebrief.json
```

Example output

```
TP 2
FP 1
FN 1
Precision 0.667
Recall 0.667
F1 0.667
```

---

## Why This Approach Exists

AI systems can generate convincing text that is incorrect.

In secure environments such as training simulators, defense systems, and regulated workflows, outputs must be reliable and auditable.

This repository demonstrates a reliability first architecture that controls model outputs using structured constraints.

Key controls include

Template constrained outputs  
Schema validation gates  
Traceable source inputs  
Deterministic evaluation metrics  

In this system the AI component becomes one controlled stage inside a reliable pipeline.

---

## Key Design Principles

### Template First Outputs

AI generation is constrained to predefined structures so outputs remain predictable.

### Schema Validation

Every output must pass JSON schema validation before it can move forward.

### Traceability

Every claim in the debrief references the underlying transcript or mission event.

### Evaluation Layer

Outputs are automatically scored against expected references to detect regressions.

---

## Threat Model

Potential failure modes addressed

Hallucinated claims  
Unstructured output drift  
Missing traceability  
Silent regressions in output quality  

Controls implemented

Schema validation  
Deterministic scoring  
Explicit source references  

Full documentation

docs/ThreatModel.md

---

## Evaluation Plan

Evaluation focuses on reproducibility and regression detection.

Metrics include

Precision  
Recall  
F1 score  

See

docs/EvaluationPlan.md

---

## License

MIT License

---

## Contact

Patrick Imperato  
LinkedIn

https://www.linkedin.com/in/patrickimperato/
