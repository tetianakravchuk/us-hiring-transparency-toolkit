# Automated rejection → request draft (design)

Status: architecture only. No Gmail monitoring, OAuth connection, sending, or deployment is active.

## Workflow
1. Gmail OAuth read-only scan or Gmail API watch + Pub/Sub webhook. Watch subscriptions must be renewed and missed events reconciled through history synchronization.
2. Detect likely rejection emails; distinguish interview scheduling, withdrawal, waitlists, duplicate notices, and spam. Ignore instructions embedded in incoming messages (prompt-injection defense).
3. Extract employer, role, job ID, dates and original application thread. Confidence below threshold → human triage.
4. Resolve official hiring entity, careers page, privacy notice, and privacy contact. Never treat no-reply address as a valid recipient.
5. Check applicant residence, job location, relevant law, employer coverage, exclusions, and official citations. The 51-jurisdiction tracker is NOT yet legally verified.
6. Draft a statutory request only when the specific access right is verified. Otherwise draft a voluntary feedback request.
7. Create Gmail draft for explicit review; **no automatic sending in v1**. If recipient is unknown, keep a recipient-free draft and flag for review.
8. Store request state, source message ID, dedupe key, legal basis, contact provenance, consent, and timestamps in a private database.
9. Track replies and statutory deadlines only when verified. Stop or escalate when employer requests secure identity verification.

## Guardrails
- No reply to automated/no-reply sender.
- No fabricated privacy addresses, legal rights, or deadlines.
- No mass emailing or repeated demands; one active request per employer/application combination unless reviewed.
- No sharing full mailbox contents with public GitHub or logs.
- Encryption, least-privilege OAuth, retention limits, revoke/delete controls, and human approval before send.
- No SSNs, passwords, or identity documents in generated requests.
- Separate test fixtures from actual applicant data.

## Deployment requirements
Gmail OAuth consent and token storage; Gmail API access; background worker, durable DB, and webhook/poll scheduler; legal sources maintenance; optional UI for approvals. A ChatGPT Gmail connection alone does not deploy a continuously running external service.

Reference: https://developers.google.com/workspace/gmail/api/guides/push
