import math
import re


def calculate_entropy(password):
    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"\d", password):
        charset_size += 10

    if re.search(r"[^A-Za-z0-9]", password):
        charset_size += 32

    if charset_size == 0:
        entropy = 0.0
    else:
        entropy = len(password) * math.log2(charset_size)

    entropy = round(entropy, 2)

    if entropy < 40:
        rating = "Weak"
    elif entropy < 60:
        rating = "Moderate"
    elif entropy < 80:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return {
        "entropy": entropy,
        "rating": rating,
        "charset_size": charset_size,
    }