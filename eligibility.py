def is_eligible(user):
    """Refactor: renamed variable, restructured the conditional.

    Seeded false positive for the demo: Suspect Finder flags this as "logic
    may have changed" purely from the diff shape. The Prosecutor tests it
    across every user state (verified/unverified x under/at/over 18) and
    behavior is identical to the base branch on all of them — demoted,
    never posted. This is the case that proves verification matters, not
    just hypothesis generation.
    """
    if user.age >= 18 and user.verified:
        return True
    return False
