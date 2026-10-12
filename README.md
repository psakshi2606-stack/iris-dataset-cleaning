# Iris Dataset Cleaning Project

## Objective
Identify and fix common data-quality problems using Python and pandas.

## Dataset
This project uses the public **Iris flower dataset** (150 records, 4 numeric measurements and a species label), originally published by R. A. Fisher and distributed by scikit-learn.

- Public dataset information: https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset
- Original dataset source: https://archive.ics.uci.edu/dataset/53/iris

## Files
- `iris_raw_with_quality_issues.csv` — working copy with clearly documented example data-quality issues added for demonstrating the cleaning steps.
- `iris_cleaned.csv` — cleaned output.
- `clean_data.py` — reproducible cleaning script.
- `README.md` — explanation of the work.

**Important transparency note:** The public Iris dataset is the starting point. To make all requested data-quality checks demonstrable in a small assignment, the raw working copy intentionally includes a few examples of missing values, duplicate rows, mixed numeric types, inconsistent category capitalization/spacing, and a decimal-comma value. Do not describe these injected issues as defects in the original public dataset.

## Issues identified and fixes

| Issue | Example in working copy | Cleaning action |
|---|---|---|
| Missing values | Blank cells and `N/A` | Convert to missing values; impute numeric measurements using species-wise median, with overall median fallback |
| Duplicate records | One repeated row | Remove exact duplicate rows |
| Incorrect data types | Numeric measurements stored as text | Trim text, normalize decimal commas, convert measurements to numeric |
| Inconsistent values | `Setosa ` and `VERSICOLOR` | Trim whitespace and convert species names to lowercase |
| Category validation | Species labels outside the known set | Keep only `setosa`, `versicolor`, and `virginica` |

## How to run
Requires Python 3 and pandas.

```bash
pip install pandas
python clean_data.py
```

The script reads `iris_raw_with_quality_issues.csv` and regenerates `iris_cleaned.csv`.

## Quality checks
After running the script, verify:
- no exact duplicate rows remain;
- all four measurement columns are numeric;
- no missing measurement values remain;
- species values are from the three documented categories.

Example checks in Python:

```python
import pandas as pd
df = pd.read_csv("iris_cleaned.csv")
print(df.isna().sum())
print("Exact duplicate rows:", df.duplicated().sum())
print(df.dtypes)
print(df["species"].value_counts())
```

## Conclusion
The workflow demonstrates a reproducible data-cleaning process and keeps the raw working copy so the changes can be reviewed.
