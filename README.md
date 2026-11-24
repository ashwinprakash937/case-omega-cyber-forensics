# Case Omega — Ransomware Incident Forensic Investigation

**Assignment:** Assignment 3 – Unit 3: Investigation of Cyber Crimes  
**Scenario:** Simulated ransomware incident at a fictional healthcare network  
**Status:** Academic simulation — no real hospital, patient, or production system was accessed.

## Repository contents
| Folder | Contents |
|---|---|
| `01_Incident_Response/` | First-responder SOP and incident checklist |
| `02_Evidence/` | Evidence register, chain of custody, acquisition and hash validation records, synthetic logs |
| `03_Malware_Analysis/` | Harmless ransomware-behaviour simulator, analysis, IOCs |
| `04_Timeline/` | Correlated incident timeline and CSV |
| `05_Forensic_Report/` | Final report in DOCX and PDF |
| `06_Scene_Documentation/` | Scene sketch and evidence-tag register |
| `07_Tools_and_Workflow/` | Tool summary, workflow, limitations and authorship declaration |
| `.github/workflows/` | GitHub Actions repository checks |

## Important scope and evidence note
This repository contains **synthetic demonstration evidence**. The disk image is a small generated placeholder evidence file, not a bit-for-bit image of a real server. The event logs, timestamps, IOCs, hash values and incident narrative are fabricated for this classroom exercise. No real ransomware is included. The Python simulator only writes harmless demonstration files under a user-selected output directory; it does not encrypt, delete, spread, persist, or contact a network.

## Quick start
1. Read `05_Forensic_Report/Case_Omega_Forensic_Report.pdf`.
2. Review the first-responder procedure and chain-of-custody form.
3. Run the safe simulator (optional): `python 03_Malware_Analysis/safe_ransomware_simulator.py --output ./demo_output`
4. Validate the included evidence placeholder with `sha256sum 02_Evidence/simulated_server_image.bin` (Windows PowerShell: `Get-FileHash ... -Algorithm SHA256`).
5. Push this folder to a new GitHub repository.

## Reproducibility
The included SHA-256 manifest records hashes of the generated demonstration artefacts. Recompute hashes after any edits; changing a file changes its digest. `02_Evidence/acquisition_record.md` explains why the placeholder is not a forensic acquisition from a live system.

## Academic integrity
Replace the student/institution placeholders, review the scenario and legal discussion, and make sure the submission reflects your own understanding and any practical work actually performed. Do not describe simulated steps as real-world actions.
