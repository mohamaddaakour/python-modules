import sys
import os
import site

# this are attributes we find them when we are using virtual environement
def is_in_virtualenv():
    return (hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix))

def get_venv_name():
    if "VIRTUAL_ENV" in os.environ:
        venv_path = os.environ["VIRTUAL_ENV"]
        return os.path.basename(venv_path)

    return None

def get_site_packages_path():
    paths = site.getsitepackages()

    if paths:
        return paths[0]
    return site.getusersitepackages()

# display it when we are outside a virtual environment
def display_outside_matrix():
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")

	# if we are working on a windows OS
    if os.name == 'nt':
        print("  matrix_env\\Scripts\\activate # On Windows")
    else:
        print("  source matrix_env/bin/activate  # On Unix")

    print("")

    print("Then run this program again.")

# display this if we are working inside a virtual machine
def display_inside_matrix():
    venv_name = get_venv_name()
    venv_path = os.environ.get('VIRTUAL_ENV', 'Unknown')
    site_packages = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name if venv_name else 'Active'}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    print(f"Package installation path: {site_packages}")


def main():
    if is_in_virtualenv():
        display_inside_matrix()
    else:
        display_outside_matrix()


if __name__ == "__main__":
    main()

# create a virtual environment: python3 -m venv <venv_name>
# get into the virtual environment: source <venv_name>/bin/activate
# get out: deactivate
