import json
import sys

def loadJson(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def normalizeClaims(items):
    out = []
    for item in items:
        text = item.get("text", "").strip().lower()
        sources = item.get("sources", [])
        sources = [str(s).strip() for s in sources]
        sources.sort()
        out.append((text, tuple(sources)))
    out.sort()
    return out

def computeF1(expectedList, actualList):
    expectedSet = set(expectedList)
    actualSet = set(actualList)

    tp = len(expectedSet & actualSet)
    fp = len(actualSet - expectedSet)
    fn = len(expectedSet - actualSet)

    precision = tp / (tp + fp) if (tp + fp) else 1.0
    recall = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) else 0.0

    return tp, fp, fn, precision, recall, f1

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python scoreOutput.py expected.json actual.json")

    expected = loadJson(sys.argv[1])
    actual = loadJson(sys.argv[2])

    expectedAll = normalizeClaims(expected["debrief"]["highlights"]) + normalizeClaims(expected["debrief"]["issues"])
    actualAll = normalizeClaims(actual["debrief"]["highlights"]) + normalizeClaims(actual["debrief"]["issues"])

    tp, fp, fn, precision, recall, f1 = computeF1(expectedAll, actualAll)

    print("Scoring")
    print("TP " + str(tp))
    print("FP " + str(fp))
    print("FN " + str(fn))
    print("Precision " + f"{precision:.3f}")
    print("Recall " + f"{recall:.3f}")
    print("F1 " + f"{f1:.3f}")

main()
