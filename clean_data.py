"""Reproducible cleaning script for the Iris data-cleaning assignment."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
raw = pd.read_csv(ROOT / "iris_raw_with_quality_issues.csv", dtype=str)

# Standardize common representations of missing values.
raw = raw.replace(r"^\s*$", pd.NA, regex=True)
raw = raw.replace(["N/A", "NA", "null", "NULL"], pd.NA)

# Convert numeric columns: trim whitespace and normalize decimal commas.
numeric_cols = [
    "sepal_length_cm", "sepal_width_cm",
    "petal_length_cm", "petal_width_cm"
]
for col in numeric_cols:
    raw[col] = raw[col].astype("string").str.strip().str.replace(",", ".", regex=False)
    raw[col] = pd.to_numeric(raw[col], errors="coerce")

# Normalize category labels.
raw["species"] = raw["species"].astype("string").str.strip().str.lower()

# Remove exact duplicate rows.
raw = raw.drop_duplicates()

# Fill missing measurements using the median for the same species;
# if a species group has no usable value, use the column median.
for col in numeric_cols:
    raw[col] = raw[col].fillna(raw.groupby("species")[col].transform("median"))
    raw[col] = raw[col].fillna(raw[col].median())

# Validate species labels against the documented Iris categories.
valid_species = {"setosa", "versicolor", "virginica"}
raw = raw[raw["species"].isin(valid_species)].copy()
raw["record_id"] = pd.to_numeric(raw["record_id"], errors="coerce").astype("int64")
raw = raw.sort_values("record_id").reset_index(drop=True)

raw.to_csv(ROOT / "iris_cleaned.csv", index=False, float_format="%.2f")
print(f"Saved {len(raw)} cleaned records to iris_cleaned.csv")
