import os
import sys
from dotenv import load_dotenv


REQUIRED = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def main() -> None:
    load_dotenv()

    missing = [v for v in REQUIRED if not os.getenv(v)]
    if missing:
        print("Missing:", ", ".join(missing))
        sys.exit(1)

    print("ORACLE STATUS: Reading the Matrix...")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print("Configuration loaded successfully")


if __name__ == "__main__":
    main()