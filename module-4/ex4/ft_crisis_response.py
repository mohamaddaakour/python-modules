def access_archive(filename) -> None:
    try:
        with open(filename, "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - ``{data.strip()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unknown system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("")

    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    access_archive("lost_archive.txt")

    print("")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    access_archive("classified_vault.txt")

    print("")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    access_archive("standard_archive.txt")

    print("")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
