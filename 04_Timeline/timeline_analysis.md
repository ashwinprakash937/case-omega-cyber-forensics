# Attack Timeline and Correlation

The timeline is ordered in UTC and merges the synthetic Windows event export with the synthetic gateway log. Confidence describes confidence that the **synthetic record says this**, not proof that an actual attack occurred.

## Interpretation
1. The first listed activity is a service-account logon at 02:02 UTC.
2. A failed logon from `10.20.4.77` precedes a privileged successful logon from the same source.
3. Gateway events show two outbound TLS sessions, but the destination addresses are documentation ranges and cannot represent real command-and-control infrastructure.
4. Bulk file access follows the privileged logon. This is consistent with several possibilities, including legitimate administration; corroboration is required.
5. An audit-log-cleared event appears before the simulated ransom-note event. Investigators should validate the event ID, log provenance and host clock before drawing conclusions.

## Limitations
No original EVTX, EDR, DNS, DHCP, VPN, cloud audit or file-system metadata was supplied. The timeline is a classroom correlation exercise, not a validated forensic reconstruction. Confirm time zones, clock drift, log completeness and source authenticity in a real investigation.
