import alchemy.elements
import alchemy.__init__

def main():
    print("\n===Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("")

    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.__init__.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.__init__.create_water()}")

    try:
        print(f"alchemy.create_earth(): {alchemy.__init__.create_earth()}")
        print(f"alchemy.create_air(): {alchemy.__init__.create_air()}")
    except:
        print(f"alchemy.create_earth(): AttributeError - not exposed")
        print(f"alchemy.create_air(): AttributeError - not exposed")
    


    print("")

    print("Package metadata: ")
    print(f"Version: {alchemy.__init__.__version__}")
    print(f"Author: {alchemy.__init__.__author__}")


main()