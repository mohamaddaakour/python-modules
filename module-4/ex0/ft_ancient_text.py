def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    print("")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    try:
        file = open(filename, "r")
        print("Connection established...")
        print("RECOVERED DATA:")
        content = file.read()
        print(content.strip())
        file.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
