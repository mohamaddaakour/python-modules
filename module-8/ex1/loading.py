import sys, importlib.metadata

print("LOADING STATUS: Loading programs...")
all_ok = True
for pkg in ['pandas', 'numpy', 'matplotlib', 'requests']:
    try:
        print(f"  [OK] {pkg} ({importlib.metadata.version(pkg)})")
    except:
        print(f"  [MISSING] {pkg}")
        all_ok = False

if not all_ok:
    print("\nInstall: pip install -r requirements.txt")
    sys.exit(1)

import pandas as pd, numpy as np
import matplotlib.pyplot as plt

print("\nAnalyzing Matrix data...")
np.random.seed(42)
df = pd.DataFrame({'level': np.random.randint(1, 11, 1000)})
print(f"Processing {len(df)} data points...")

print("\nGenerating visualization...")
counts = df['level'].value_counts().sort_index()
plt.bar(counts.index, counts.values, color='green')
plt.title('Matrix Level Distribution')
plt.savefig('matrix_analysis.png')
print("Results saved to: matrix_analysis.png")
