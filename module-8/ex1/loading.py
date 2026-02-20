import sys
import importlib


REQUIRED = ["pandas", "numpy", "matplotlib"]


def check() -> bool:
    ok = True
    for pkg in REQUIRED:
        try:
            mod = importlib.import_module(pkg)
            print(f"[OK] {pkg} ({mod.__version__})")
        except ImportError:
            print(f"[ERROR] {pkg} missing")
            ok = False
    return ok


def run() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.DataFrame({"x": np.random.randn(100)})
    data.hist()
    plt.savefig("matrix_analysis.png")
    print("Saved matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS")
    if not check():
        print("Install with:")
        print("pip install -r requirements.txt")
        print("or: poetry install")
        sys.exit(1)
    run()


if __name__ == "__main__":
    main()