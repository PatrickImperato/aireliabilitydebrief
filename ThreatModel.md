# Threat model

## Data risks

Sensitive inputs copied into outputs
Unauthorized access to logs

Mitigations
Keep raw inputs immutable
Separate storage for generated outputs
Access control and audit logs

## Behavior risks

Hallucinated facts
Overconfident language

Mitigations
Require sources for every claim
Use fixed template fields
Force unknown when evidence missing

## Process risks

Model changes break behavior
Silent regressions

Mitigations
Version outputs
Regression scoring against expected debriefs
Gates before each rollout stage
