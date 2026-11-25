# Evidence Acquisition and Hash Validation

## Acquisition record

- **Evidence ID:** E-001
- **Item:** `simulated_server_image.bin`
- **Source:** Synthetic training artefact generated for this assignment
- **Acquisition status:** No physical or virtual hospital server was imaged.
- **Tool:** Python standard library used to generate a 32 KiB placeholder file
- **Acquisition date:** 17 November 2026
- **Examiner:** Student examiner (replace with your name)
- **Limitation:** This file is deliberately **not** a forensic disk image and must not be represented as one.

## Hash validation

- **Algorithm:** SHA-256
- **Digest:** `8d4ae2d9bef2ade722b88d7116610eb797eccb3ad0d0880defd1988a84287b07`
- **Procedure:** Calculate the digest of the file at acquisition, then calculate it again after copying or transfer. Matching values support that the bytes compared have not changed between those calculations.
- **Re-check (Linux/macOS):** `sha256sum simulated_server_image.bin`
- **Re-check (Windows PowerShell):** `Get-FileHash .\simulated_server_image.bin -Algorithm SHA256`
- **Result in this generated package:** `8d4ae2d9bef2ade722b88d7116610eb797eccb3ad0d0880defd1988a84287b07`

A matching hash does not establish who created the file, whether the source was trustworthy, or whether the file represents a complete disk. For a real case, use a validated forensic imager such as FTK Imager or `dd` under an approved procedure, document write-blocking, device identifiers, errors and examiner details, and hash both source acquisition and resulting image where feasible.
