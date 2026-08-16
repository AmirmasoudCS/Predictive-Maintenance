from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Depth 1

DATASET = ROOT / "Dataset"
CONFIG = ROOT / "config"
LOG = ROOT / "log"
ASSETS = ROOT / "assets"

# Depth 2

CSV_DATASET = DATASET / "ai4i2020.csv"
PLOTS = ASSETS / "plots"
PROCESSED = DATASET / "processed"

# Depth 3

X_TRAIN = PROCESSED / "x_train.csv"
X_TEST = PROCESSED / "x_test.csv"
Y_TRAIN = PROCESSED / "y_train.csv"
Y_TEST = PROCESSED / "y_test.csv"