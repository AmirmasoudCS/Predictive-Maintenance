from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Depth 1

DATASET = ROOT / "Dataset"
CONFIG = ROOT / "config"
LOG = ROOT / "log"
ASSETS = ROOT / "assets"
RESULTS = ROOT / "results"

# Depth 2

CSV_DATASET = DATASET / "ai4i2020.csv"
PLOTS = ASSETS / "plots"
PROCESSED = DATASET / "processed"

LOGISTIC_REGRESSION = RESULTS / "logistic_regression"
RANDOM_FOREST = RESULTS / "random_forest"
XGBOOST = RESULTS / "xgboost"

# Depth 3

X_TRAIN = PROCESSED / "x_train.csv"
X_TEST = PROCESSED / "x_test.csv"
Y_TRAIN = PROCESSED / "y_train.csv"
Y_TEST = PROCESSED / "y_test.csv"

LOGISTIC_REGRESSION_METRICS = LOGISTIC_REGRESSION / "metrics.csv"
LOGISTIC_REGRESSION_MODEL = LOGISTIC_REGRESSION / "model.pkl"
LOGISTIC_REGRESSION_CHARTS = LOGISTIC_REGRESSION / "charts"

RANDOM_FOREST_METRICS = RANDOM_FOREST / "metrics.csv"
RANDOM_FOREST_MODEL = RANDOM_FOREST / "model.pkl"
RANDOM_FOREST_CHARTS = RANDOM_FOREST / "charts"

XGBOOST_METRICS = XGBOOST / "metrics.csv"
XGBOOST_MODEL = XGBOOST / "model.pkl"
XGBOOST_CHARTS = XGBOOST / "charts"