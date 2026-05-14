import argparse

from password_checker import check_password_strength
from entropy_calculator import calculate_entropy
from breach_checker import check_password_breach
from report_generator import save_report


def load_common_passwords():
    try:
        with open(
            "sample/common_passwords.txt",
            "r",
            encoding="utf-8"
        ) as file:
            return {
                line.strip().lower()
                for line in file
                if line.strip()
            }
    except FileNotFoundError:
        return set()


def analyze_password(password, common_passwords):
    strength_result = check_password_strength(password)
    entropy_result = calculate_entropy(password)
    breach_result = check_password_breach(password)

    dictionary_match = (
        password.lower() in common_passwords
    )

    result = {
        "password": password,
        "score": strength_result["score"],
        "strength": strength_result["strength"],
        "checks": strength_result["checks"],
        "recommendations": strength_result["recommendations"],
        "entropy": entropy_result["entropy"],
        "entropy_rating": entropy_result["rating"],
        "dictionary_match": dictionary_match,
        "breached": breach_result["breached"],
        "breach_count": breach_result["breach_count"],
        "error": breach_result["error"],
    }

    return result


def print_result(result):
    print(f"Password: {result['password']}")
    print(f"Strength: {result['strength']}")
    print(
        f"Entropy: {result['entropy']} bits "
        f"({result['entropy_rating']})"
    )
    print(
        "Dictionary Match:",
        "Yes" if result["dictionary_match"] else "No"
    )

    if result["error"]:
        print(f"Breach Check Error: {result['error']}")
    else:
        if result["breached"]:
            print(
                f"Breached: Yes "
                f"({result['breach_count']} times)"
            )
        else:
            print("Breached: No")

    if result["recommendations"]:
        print("Recommendations:")
        for item in result["recommendations"]:
            print(f"- {item}")

    print("-" * 50)


def process_file(file_path, common_passwords):
    with open(file_path, "r", encoding="utf-8") as file:
        passwords = [
            line.strip()
            for line in file
            if line.strip()
        ]

    for password in passwords:
        result = analyze_password(
            password,
            common_passwords
        )
        print_result(result)


def main():
    parser = argparse.ArgumentParser(
        description="Password Security Auditor Pro"
    )

    parser.add_argument(
        "password",
        nargs="?",
        help="Password to analyze"
    )

    parser.add_argument(
        "--file",
        help="Path to a file containing passwords"
    )

    parser.add_argument(
        "--json",
        help="Save output to a JSON file"
    )

    args = parser.parse_args()

    common_passwords = load_common_passwords()

    if args.file:
        process_file(
            args.file,
            common_passwords
        )
        return

    if not args.password:
        parser.print_help()
        return

    result = analyze_password(
        args.password,
        common_passwords
    )

    print_result(result)

    if args.json:
        save_report(result, args.json)
        print(f"Report saved to {args.json}")


if __name__ == "__main__":
    main()