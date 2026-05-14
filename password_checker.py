import re


def check_password_strength(password):
    score = 0
    recommendations = []

    checks = {
        "length": len(password) >= 12,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digits": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    if checks["length"]:
        score += 1
    else:
        recommendations.append(
            "Use at least 12 characters."
        )

    if checks["uppercase"]:
        score += 1
    else:
        recommendations.append(
            "Add at least one uppercase letter."
        )

    if checks["lowercase"]:
        score += 1
    else:
        recommendations.append(
            "Add at least one lowercase letter."
        )

    if checks["digits"]:
        score += 1
    else:
        recommendations.append(
            "Add at least one digit."
        )

    if checks["special"]:
        score += 1
    else:
        recommendations.append(
            "Add at least one special character."
        )

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "checks": checks,
        "recommendations": recommendations,
    }