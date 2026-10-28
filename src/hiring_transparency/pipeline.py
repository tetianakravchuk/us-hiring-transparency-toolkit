"""Pure classification and draft preparation. Never sends mail."""
from dataclasses import dataclass
from email.utils import parseaddr
import hashlib
import re

REJECTION = re.compile(r"\b(unfortunately|not (?:be )?moving forward|not selected|other candidates|unable to offer|will not be proceeding|not proceeding|position has been filled)\b", re.I)
NEGATIVE = re.compile(r"\b(interview invitation|schedule (?:an|your) interview|offer of employment|congratulations|application received|thank you for applying|withdrawn by you|unsubscribe)\b", re.I)
NO_REPLY = re.compile(r"^(?:no[._-]?reply|do[._-]?not[._-]?reply|notifications?)@", re.I)

@dataclass(frozen=True)
class IncomingMessage:
    message_id: str
    sender: str
    subject: str
    body: str

@dataclass(frozen=True)
class DraftProposal:
    dedupe_key: str
    classification: str
    confidence: str
    recipient: str | None
    subject: str | None
    body: str | None
    requires_review: bool = True

def classify(message: IncomingMessage) -> str:
    content = f"{message.subject}\n{message.body}"
    if NEGATIVE.search(message.subject) or (NEGATIVE.search(content) and not REJECTION.search(content)):
        return "not_rejection"
    return "possible_rejection" if REJECTION.search(content) else "uncertain"

def prepare_draft(message: IncomingMessage, employer: str | None = None,
                  role: str | None = None, verified_contact: str | None = None) -> DraftProposal:
    """Generate voluntary feedback only; statutory requests need verified rules."""
    classification = classify(message)
    key = hashlib.sha256(message.message_id.encode("utf-8")).hexdigest()
    if classification != "possible_rejection":
        return DraftProposal(key, classification, "low", None, None, None)
    address = parseaddr(verified_contact or "")[1]
    recipient = address if address and "@" in address and not NO_REPLY.match(address) and address == (verified_contact or "").strip() else None
    if not employer or not role:
        return DraftProposal(key, classification, "needs_application_match", None, None, None)
    subject = f"Request for application feedback — {role}"
    body = (f"Hello Recruiting or Privacy Team,\n\n"
            f"I applied for the {role} position at {employer} and received an update that I was not selected. "
            "If available under your policies, I would appreciate any feedback or applicant-facing assessment "
            "results you are able to share. Could you also tell me whether automated screening was used "
            "and direct me to the appropriate privacy-request process if one applies?\n\n"
            "I understand that confidential evaluations may not be available.\n\nThank you.")
    return DraftProposal(key, classification, "needs_human_review", recipient, subject, body)
