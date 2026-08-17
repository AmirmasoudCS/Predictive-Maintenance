# ⚙️ Predictive-Maintenance-Machine-Failure-Classification

![Project Banner](assets/banner.png)

---

## My Motivation

As the population grows, the demand on different assets grows as well, and you can supply this demand by either building more and more factories and machineries, or improve the 
quality of the ones that we currently have, and since we only have so much land to place firms and factories on, it is a good idea to start improving the way factories and machines inside them are monitored and handles.

There are different ways you can improve a factory to name a few: predict the hourly output, replace the manual labor with machines that never rest, using sensors to gather data in order to find hidden patterns in failure mode of machines and ...

In this project, I delve intp predictive maintanance, using the data gathered from the AI4I 2020 dataset to see how does bagging and boosting algorithms can help with predicting the machine failure with logistic regression as a simple baseline, and I also recommend a model to be user based on the results we get in different situations.

---

A binary classification project predicting machine failure on the AI4I 2020 Predictive
Maintenance Dataset, comparing Logistic Regression, Random Forest, and XGBoost.


## Overview

Manufacturing equipment failures are costly and often preventable. This project builds
and compares three classification models to predict machine failure from sensor
readings (temperature, rotational speed, torque, tool wear) and product type, with a
focus on handling severe class imbalance (~3.4% failure rate) correctly.

## Dataset

- **Source:** [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) (UCI Machine Learning Repository)
- 10,000 rows, 14 columns - sensor readings, product type, and failure labels
- Target: `Machine failure` (binary), with 5 individual failure-mode flags (TWF, HDF, PWF, OSF, RNF)

## Approach

1. **Sanity check**: verified data integrity (no missing values, no duplicates, correct types)
2. **EDA**: explored feature distributions, correlations, and failure patterns
3. **Preprocessing**: dropped identifiers and target-leaking columns, one-hot encoded `Type`, stratified train/test split, 10-fold stratified cross-validation for evaluation
4. **Modeling**: trained and evaluated three classifiers:
   - Logistic Regression (baseline)
   - Random Forest
   - XGBoost
5. **Comparison**: evaluated all models on precision, recall, F1, ROC-AUC, and PR-AUC

## Key EDA Findings

- Machines don't fail randomly, failures cluster in two distinct operating zones
  (low-speed/high-torque and high-speed/low-torque), each tied to a different failure mechanism:

  ![Speed vs Torque by Failure Mode](assets/plots/scatter_speed_vs_torque_by_failure_mode.png)

- Counterintuitively, the **lowest quality product variant (Type L)** had the highest
  failure rate, not the highest quality variant:

  ![Failure Rate by Type](assets/plots/failure_rate_by_type.png)

Full EDA writeup: [`data inspection and eda`](./notebooks/01_inspection_and_EDA.ipynb)

## Results

Given the severe class imbalance, **PR-AUC and recall on the failure class** were
prioritized over accuracy.

| Model | Precision | Recall | F1 | ROC-AUC | PR-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 0.144 | 0.824 | 0.245 | 0.907 | 0.396 |
| Random Forest | 0.750 | 0.706 | 0.727 | 0.970 | 0.781 |
| **XGBoost** | 0.675 | **0.794** | **0.730** | 0.963 | **0.812** |

![Model Comparison Bars](results/model_comparison_bars.png)

![Precision-Recall Curve Comparison](results/model_comparison_pr_curves.png)

![ROC Curve Comparison](results/model_comparison_roc_curves.png)

### Recommendation

**XGBoost** is the recommended model, it achieves the best PR-AUC and highest recall,
which matters most in predictive maintenance since missed failures are typically far
costlier than false alarms. **Random Forest** is a strong alternative if minimizing
false alarms (technician callouts) is the higher priority, thanks to its better precision.

Logistic Regression is kept as an interpretable baseline but isn't practical to deploy
on its own, nearly 9 out of 10 of its failure alerts would be false alarms.

## Repository Structure

```
 
├── 📁 assets
│   └── 📁 plots
│       ├── 🖼️ boxplot_Air_temperature_by_failure.png
│       ├── 🖼️ boxplot_Process_temperature_by_failure.png
│       ├── 🖼️ boxplot_Rotational_speed_by_failure.png
│       ├── 🖼️ boxplot_Tool_wear_by_failure.png
│       ├── 🖼️ boxplot_Torque_by_failure.png
│       ├── 🖼️ boxplots_by_failure_combined.png
│       ├── 🖼️ correlation_matrix.png
│       ├── 🖼️ distribution_Air_temperature.png
│       ├── 🖼️ distribution_Process_temperature.png
│       ├── 🖼️ distribution_Rotational_speed.png
│       ├── 🖼️ distribution_Tool_wear.png
│       ├── 🖼️ distribution_Torque.png
│       ├── 🖼️ failure_rate_by_type.png
│       ├── 🖼️ numeric_distributions_combined.png
│       ├── 🖼️ scatter_speed_vs_torque_by_failure.png
│       ├── 🖼️ scatter_speed_vs_torque_by_failure_mode.png
│       └── 🖼️ Target_Distribution.png
├── 📁 config
│   ├── 🐍 constants.py
│   └── 🐍 paths.py
├── 📁 Dataset
│   ├── 📁 processed
│   │   ├── 📊 x_test.csv
│   │   ├── 📊 x_train.csv
│   │   ├── 📊 y_test.csv
│   │   └── 📊 y_train.csv
│   └── 📊 ai4i2020.csv
├── 📁 log
├── 📁 notebooks
│   ├── 📄 01_inspection_and_EDA.ipynb
│   ├── 📄 02_preprocessing.ipynb
│   ├── 📄 03_logistic_regression.ipynb
│   ├── 📄 04_random_forest.ipynb
│   ├── 📄 05_xgboost.ipynb
│   └── 📄 06_comparison.ipynb
├── 📁 results
│   ├── 📁 logistic_regression
│   │   ├── 📁 charts
│   │   │   ├── 🖼️ coefficients.png
│   │   │   ├── 🖼️ confusion_matrix.png
│   │   │   ├── 🖼️ pr_curve.png
│   │   │   └── 🖼️ roc_curve.png
│   │   ├── 📊 metrics.csv
│   │   └── 📄 model.pkl
│   ├── 📁 random_forest
│   │   ├── 📁 charts
│   │   │   ├── 🖼️ confusion_matrix.png
│   │   │   ├── 🖼️ feature_importance.png
│   │   │   ├── 🖼️ pr_curve.png
│   │   │   └── 🖼️ roc_curve.png
│   │   ├── 📊 metrics.csv
│   │   └── 📄 model.pkl
│   ├── 📁 xgboost
│   │   ├── 📁 charts
│   │   │   ├── 🖼️ confusion_matrix.png
│   │   │   ├── 🖼️ feature_importance.png
│   │   │   ├── 🖼️ pr_curve.png
│   │   │   └── 🖼️ roc_curve.png
│   │   ├── 📊 metrics.csv
│   │   └── 📄 model.pkl
│   ├── 🖼️ model_comparison_bars.png
│   ├── 🖼️ model_comparison_pr_curves.png
│   └── 🖼️ model_comparison_roc_curves.png
├── ⚖️ LICENSE
├── 📘 README.md
└── 📝 requirements.txt
```
> Generated using [directory-tree-printer](https://github.com/AmirmasoudCS/Tree-Printer.git)

## How to Run

```bash
# clone the repo
git clone <repo-url>
cd Predictive-Maintenance

# install dependencies
pip install -r requirements.txt

# run notebooks in order
```

## License

[MIT License](./LICENSE)