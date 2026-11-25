# First Responder SOP — Case Omega
**Scenario time:** 17 November 2026 (fictional exercise)  
**Location:** Omega General Hospital, fictional server room  
**Incident:** Suspected ransomware affecting clinical file services
## 1. Purpose and authority
Preserve people’s safety, protect patient care, prevent avoidable evidence
alteration, and establish a defensible record. The incident commander
authorises containment actions. Follow the organisation's incident-response
plan and applicable law.
## 2. Step-by-step procedure
1. **Safety first:** Check electrical, fire, environmental and physical
   safety. Do not enter an unsafe server room.
2. **Establish control:** Notify the incident commander, hospital
   IT/security lead, privacy/legal contact and law-enforcement liaison as
   required. Start an incident log with local time and time zone.
3. **Protect patient care:** Coordinate with clinical leadership to move
   critical workflows to approved downtime procedures. Do not independently
   shut down clinical equipment.
4. **Restrict access:** Establish an access perimeter and record everyone
   entering or leaving. Do not allow unauthorised staff to handle devices.
5. **Document before touching:** Photograph the room, device fronts/rears,
   cabling, screen messages and connected media. Record make/model, serial
   number, asset tag, power/network state, displayed time and visible
   symptoms. Use evidence tags.
6. **Record volatile context:** If trained and authorised, document
   logged-in users, running processes, network connections and system clock.
   Live response can alter evidence; record every command, operator, time
   and output. Do not improvise commands.
7. **Contain proportionately:** With the incident commander, isolate
   affected network segments using approved procedures. Prefer network
   isolation over powering off when safe and technically appropriate. Do
   not disconnect or power down blindly; volatile evidence and patient
   safety may be affected.
8. **Preserve originals:** Do not browse files, run unknown programs,
   insert USB devices, or attempt decryption on original media. Use write
   blockers and validated forensic tools where applicable.
9. **Acquire evidence:** A qualified examiner creates a forensic image
   using an approved tool, records tool/version/settings, source and
   destination identifiers, start/end times, errors and hash values. Work
   from verified copies.
10. **Maintain chain of custody:** Seal, label and log every collection,
    transfer, opening, examination and return. Record names, signatures,
    dates, times, purpose and seal condition.
11. **Secure storage:** Store originals in access-controlled evidence
    storage; encrypt working copies; restrict access and maintain an audit
    trail.
12. **Handover and reporting:** Brief the incident commander and authorised
    investigators. Record outstanding actions, risks, limitations and
    every departure from this SOP.
## 3. Do not
- Do not pay a ransom or communicate with an actor without authorised
  leadership/legal direction.
- Do not delete suspicious files, run cleanup tools, reboot, or restore
  backups before evidence and business-continuity decisions are made.
- Do not connect evidence media to an ordinary workstation.
- Do not claim a hash proves the contents are authentic; it supports
  integrity comparison of the same data.
- Do not access patient data unless authorised and necessary.
## 4. Documentation checklist
- [ ] Incident ID and authority recorded
- [ ] Scene and device photographs/sketch captured
- [ ] Device state, clock and network connections recorded
- [ ] Evidence IDs and seals assigned
- [ ] Collection method and tool versions documented
- [ ] SHA-256 values calculated and independently verified
- [ ] Chain-of-custody transfers signed
- [ ] Originals secured; analysis performed on working copies
- [ ] Patient-safety and privacy impacts escalated
- [ ] Final handover completed
