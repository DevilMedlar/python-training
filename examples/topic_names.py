"""Small review exercise adapted from the supplied GitHub practical reference.

Contract: input is str; lowercase it and join whitespace-separated words with
hyphens. Punctuation remains; empty/whitespace-only input returns an empty string.
This is not a URL, filename, identifier, or security sanitizer.
"""


def normalize_topic(topic: str) -> str:
    return "-".join(topic.lower().split())
