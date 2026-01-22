import sys

def main():
    print("=== Command Quest ===")

    program_name = sys.argv[0]
    total_args = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {total_args - 1}")

    index = 1
    while index < total_args:
        print(f"Argument {index}: {sys.argv[index]}")
        index += 1

    print(f"Total arguments: {total_args}")

if __name__ == "__main__":
    main()
