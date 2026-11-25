# Simulated Evidence Acquisition – Case Omega
## 1. Objective
Demonstrate a simulated evidence acquisition and integrity verification
workflow for the fictional Omega Hospital incident.
## 2. Evidence Details
- Evidence ID: E-001
- Filename: simulated_server_image.bin
- Evidence type: Synthetic binary evidence artifact
- File size: 32,862 bytes
## 3. Acquisition Method
A pre-created synthetic evidence artifact was examined using Windows
PowerShell. SHA-256 was calculated using `Get-FileHash`.
No physical hospital server or production storage device was acquired.
## 4. Integrity Verification
Algorithm: SHA-256
Calculated hash:
`8D4AE2D9BEF2ADE722B88D7116610EB797ECCB3AD0D0880DEFD1988A84287B07`
The calculated hash matched the supplied `SHA256SUMS.txt` manifest.
## 5. Limitations
This was a simulated acquisition exercise.
FTK Imager and physical disk acquisition were not performed.
The supplied binary file is not represented as a verified physical disk image.
## 6. Conclusion
The synthetic evidence artifact was successfully hashed, and its integrity
was verified against the supplied manifest.
