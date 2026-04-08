from enum import Enum

class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    OFFERED = "offered"
    REJECTED = "rejected"
    HIRED = "hired"