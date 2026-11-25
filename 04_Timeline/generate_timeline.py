import csv
from datetime import datetime
from pathlib import Path
folder = Path(__file__).parent
source = folder / "attack_timeline.csv"
output = folder / "generated_timeline.md"
with source.open("r", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    required = {"timestamp_utc", "source", "evidence_id", "event", "confidence"}
    if not required.issubset(reader.fieldnames or []):
        raise SystemExit("ERROR: Required CSV columns are missing.")
    events = list(reader)
for event in events:
    datetime.strptime(event["timestamp_utc"], "%Y-%m-%dT%H:%M:%SZ")
events.sort(key=lambda item: item["timestamp_utc"])
lines = [
    "# Generated Incident Timeline",
    "",
    "**Date:** 17 November 2026  ",
    "**Timezone:** UTC  ",
    f"**Events recorded:** {len(events)}",
    "",
    "| Timestamp (UTC) | Evidence | Source | Event | Confidence |",
    "|---|---|---|---|---|",
]
for e in events:
    lines.append(
        f"| {e['timestamp_utc']} | {e['evidence_id']} | "
        f"{e['source']} | {e['event']} | {e['confidence']} |"
    )
lines += [
    "",
    "## Limitations",
    "",
    "This timeline is generated from the supplied synthetic CSV records. "
    "It does not independently authenticate the logs or establish that a "
    "real cyberattack occurred. Event confidence reflects the supplied "
    "record's confidence label, not proof of the underlying activity.",
    "",
]
output.write_text("\n".join(lines), encoding="utf-8")
print(f"SUCCESS: Created {output}")
print(f"Events processed: {len(events)}")
