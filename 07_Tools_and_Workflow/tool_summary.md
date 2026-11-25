# Tool Summary and Workflow

| Tool | Purpose in a real investigation | Use in this package |
| --- | --- | --- |
| FTK Imager | Acquire and verify forensic disk images | Described only; no physical image acquired |
| `dd` | Bit-stream acquisition on Unix-like systems | Described only |
| SHA-256 (`sha256sum`, `Get-FileHash`) | Integrity comparison | Used to hash synthetic placeholder |
| Python 3 | Generate and correlate synthetic artefacts | Used for safe simulator and package generation |
| Timeline tools (`log2timeline`/Plaso) | Parse and normalise forensic artefacts | Workflow described; CSV timeline supplied |
| GitHub Actions | Validate repository layout and Markdown hygiene | Workflow included |

## Workflow

1. Establish authority, patient-safety priorities and incident scope.
2. Document scene and system state.
3. Identify, label, preserve and acquire evidence.
4. Hash and verify acquisition outputs.
5. Analyse copies in a controlled environment.
6. Correlate events and state uncertainty.
7. Prepare legal-technical report and recommendations.
8. Review chain of custody, repository completeness and disclosure limitations.
