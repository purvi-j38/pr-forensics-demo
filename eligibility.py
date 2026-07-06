def is_eligible(user):
    is_adult = user.age >= 18
    is_verified = user.verified
    if not is_adult:
        return False
    if not is_verified:
        return False
    return True
