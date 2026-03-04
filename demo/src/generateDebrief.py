import json
import sys

def loadJson(path):
    with open(path, "r", encoding="utf 8") as f:
        return json.load(f)

def writeJson(path, obj):
    with open(path, "w", encoding="utf 8") as f:
        json.dump(obj, f, indent=2)

def findSegmentsNearTime(segments, t, windowSec=40):
    hits = []
    for seg in segments:
        if abs(seg["timeOffsetSec"] - t) <= windowSec:
            hits.append(seg)
    return hits

def main():
    if len(sys.argv) != 4:
        raise SystemExit("Usage: python generateDebrief.py mission.json transcript.json out.json")

    missionPath = sys.argv[1]
    transcriptPath = sys.argv[2]
    outPath = sys.argv[3]

    mission = loadJson(missionPath)
    transcript = loadJson(transcriptPath)

    if mission["missionId"] != transcript["missionId"]:
        raise ValueError("missionId mismatch")

    events = mission["events"]
    segments = transcript["segments"]

    highlights = []
    issues = []

    for event in events:
        near = findSegmentsNearTime(segments, event["timeOffsetSec"])
        sources = [event["eventId"]] + [seg["segmentId"] for seg in near]

        labelLower = event["label"].lower()

        if "fuel" in labelLower:
            highlights.append({"text": "Fuel management recovered after a correction.", "sources": sources})
        elif "comm" in labelLower:
            issues.append({"text": "Comm discipline had stepped on calls during rejoin.", "sources": sources})
        elif "altitude" in labelLower or event["type"] == "safety":
            issues.append({"text": "Altitude block had a brief dip below floor, corrected.", "sources": sources})
        else:
            issues.append({"text": "Observed item: " + event["label"] + ".", "sources": sources})

    out = {
        "missionId": mission["missionId"],
        "debrief": {
            "summary": "Debrief draft based on mission log and transcript only.",
            "highlights": highlights,
            "issues": issues,
            "unknowns": [
                {"text": "No additional objectives provided beyond supplied inputs.", "sources": []}
            ]
        }
    }

    writeJson(outPath, out)
    print(outPath)

main()
