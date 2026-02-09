def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    try:
        with open(filename, "r") as file:
            print("Connection established...")

            print("")

            print("RECOVERED DATA:")
            for i, line in enumerate(file):
                print(f"[FRAGMENT {i:03}] {line.strip()}")

        print("")

        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
