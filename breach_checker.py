import hashlib
import requests


def check_password_breach(password):
    sha1_hash = hashlib.sha1(
        password.encode("utf-8")
    ).hexdigest().upper()

    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return {
            "breached": False,
            "breach_count": 0,
            "error": "Unable to contact HIBP API."
        }

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return {
                "breached": True,
                "breach_count": int(count),
                "error": None
            }

    return {
        "breached": False,
        "breach_count": 0,
        "error": None
    }