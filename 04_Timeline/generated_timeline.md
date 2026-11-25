# Generated Incident Timeline

**Date:** 17 November 2026  
**Timezone:** UTC  
**Events recorded:** 9

| Timestamp (UTC) | Evidence | Source | Event | Confidence |
|---|---|---|---|---|
| 2026-11-17T02:02:11Z | E-002 | Windows Security export | Service account successful logon | Medium |
| 2026-11-17T02:07:43Z | E-002 | Windows Security export | Failed logon from 10.20.4.77 | Medium |
| 2026-11-17T02:09:02Z | E-003 | Gateway log | Outbound TLS session to documentation IP | Low |
| 2026-11-17T02:11:09Z | E-002 | Windows Security export | Privileged account successful logon from 10.20.4.77 | Medium |
| 2026-11-17T02:12:44Z | E-003 | Gateway log | Second outbound TLS session | Low |
| 2026-11-17T02:15:31Z | E-002 | Windows Security export | Unusual bulk file access | Medium |
| 2026-11-17T02:19:58Z | E-002 | Windows Security export | Audit log cleared event; verify event source and context | Medium |
| 2026-11-17T02:22:06Z | E-003 | Gateway log | Denied SMB connection attempt | Low |
| 2026-11-17T02:24:20Z | E-002 | Windows Security export | Simulated ransom note creation | Low |

## Limitations

This timeline is generated from the supplied synthetic CSV records. It does not independently authenticate the logs or establish that a real cyberattack occurred. Event confidence reflects the supplied record's confidence label, not proof of the underlying activity.
