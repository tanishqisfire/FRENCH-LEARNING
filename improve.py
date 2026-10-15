SIMILAR_GROUPS = [
    {"e", "ɛ"},
    {"o", "ɔ"},
    {"ø", "œ"},
]

def same_group(a, b):
    if a == b:
        return True
    for group in SIMILAR_GROUPS:
        if a in group and b in group:
            return True

    return False


LIAISON_SOUNDS = {"z", "t"}