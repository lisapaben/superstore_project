# superstore_project
Superstore exploratory data analysis (EDA) + Tableau visualizations

## Download dataset

1. Create Kaggle API token (kaggle.json) from Kaggle -> My Account -> API.
2. Place `kaggle.json` in `~/.kaggle/` (or set `KAGGLE_CONFIG_DIR`).
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python scripts/download_dataset.py`

## Cleaned Superstore Dataset

This cleaned version of the Superstore dataset supports Tableau dashboards and stakeholder analysis. Key transformations include:

- Standardized column names for compatibility
- Converted date fields to datetime format
- Derived metrics: profit margin, shipping delay
- Outlier flagging using Z-score methodology
- Removal of nulls (none found) and formatting inconsistencies

The cleaned file is located at: `data/superstore_data/cleaned_superstore.csv`

A lightweight data dictionary is included to support dashboard development and stakeholder walkthroughs.