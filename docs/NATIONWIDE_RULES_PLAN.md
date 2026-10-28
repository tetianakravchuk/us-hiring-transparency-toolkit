# Nationwide hiring-rights rules engine — implementation plan

Status: research and design; NOT a completed legal audit of all states.
Research baseline: 2026-10-28.

## Inputs
Applicant residence at application and request dates; job location and remote scope; employer legal entity and relevant establishments; application/rejection dates; type of processing (ATS, AI assessment, consumer report); desired data and outcome.

## Rules model
Each rule must have jurisdiction, statute, section, official_source_url, last_verified, effective_from, effective_until, covered_persons, covered_entities, geographic_scope, employment_exclusion, thresholds, exemptions, available_rights, response_deadline, verification_method, and confidence.

## Evaluation
1. Resolve employer identity from official corporate site, job posting, and privacy policy; keep headquarters, legal entity, worksite, and processing location separate.
2. Evaluate all plausibly applicable jurisdictions, not just headquarters.
3. Check effective date on relevant conduct and current request.
4. Check residence, coverage, employment exemptions, and processing type.
5. Return VERIFIED_APPLIES, VERIFIED_EXCLUDED, or NEEDS_REVIEW with statute and sources.
6. Only verified applicable rights may produce statutory demands; otherwise produce voluntary feedback requests.
7. Keep a human review step for ambiguous cases.

## Research acceptance criteria
- 50 states plus DC each have a reviewed record, with official statute and regulator URLs, verification date, and explicit employment-applicant analysis.
- Separate local laws, AI hiring, FCRA/background checks, salary transparency, discrimination complaint processes, and retention rules.
- Test cross-state remote hiring, subsidiaries, relocation, conflicting jurisdictions, and prospective laws.
- No invented legal rights, legal deadlines, employer contacts, or AI scores.
- Never commit applicant PII to public GitHub.

## Initial authoritative references
- Colorado AG employment exclusion: https://coag.gov/resources/colorado-privacy-act/
- NYC AEDT rules: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
- California CPPA: https://cppa.ca.gov/
- EEOC: https://www.eeoc.gov/job-applicants
- FTC background checks: https://www.ftc.gov/business-guidance/resources/background-checks-what-employers-need-know

This is a research roadmap, not legal advice.
