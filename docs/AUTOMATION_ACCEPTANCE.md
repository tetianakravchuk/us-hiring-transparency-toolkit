# Acceptance tests for automated hiring requests

- Recognizes an ordinary rejection and a rejection following an interview.
- Does not classify an interview invitation, offer, waitlist, or marketing email as rejection.
- Extracts company and role without inventing missing fields.
- Ignores malicious instructions contained in email bodies.
- Flags sender `no-reply@` or `donotreply@` and searches official employer privacy routes instead.
- Rejects unverifiable privacy contacts.
- Creates a voluntary request when jurisdiction or coverage is uncertain.
- Uses a statutory request only when verified evidence covers applicant, employer, time, and requested data.
- Dedupe prevents repeated drafts from repeated rejection notifications.
- Gmail draft is created without sending; user must explicitly approve.
- Can disable monitoring and erase retained personal information.
- Does not expose application records in public GitHub, CI logs, or analytics.
