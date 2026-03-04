# Architecture

## Goal

Produce debrief drafts that stay inside strict bounds.
Every claim traces to input.

## Inputs

Mission log events with timestamps
Transcript segments with timestamps

## Outputs

Fixed debrief template
Claims with explicit source references
Unknowns stated as unknown

## Components

Ingestion
Validate JSON inputs using schemas

Alignment
Link transcript segments to mission events using time windows

Draft generator
Fill a fixed template
Only use facts present in inputs

Validation
Validate output against schema
Validate that all source references exist

Scoring
Compare output to expected debrief for regression checks

## Boundaries

No freeform narrative outside schema fields
No new numbers that do not exist in inputs
No claims without sources
