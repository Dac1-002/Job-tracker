from enum import StrEnum


class ApplicationStatus(StrEnum):
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    OFFERED = "offered"
    REJECTED = "rejected"
    HIRED = "hired"