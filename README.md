# Predicting US Soybean Yields Using State-Level Data

## Objective

Train a basic machine learning model in Python to predict annual soybean yields in the US on a state level.

Analysis was fully completed in the `soybean_us_yield_prediction.ipynb` notebook.

## Setup & Installation

This project uses [UV](https://github.com/astral-sh/uv) for environment and dependency management.

```bash
# Install UV (if not installed)
pip install uv

git clone <repo-url>
cd <repo-name>

# Create environment and install dependencies
uv sync
```

Open `soybean_us_yield_prediction.ipynb`, activate virtual environmant and run all cells.


## Project structure

- Full analysis is done in `soybean_us_yield_prediction.ipynb`
- Input data is stored in the `data/raw` directory. 
    Provided datasets are:
    - 2t.csv: daily 2m maximum temperature in Kelvin
    - tp.csv: daily total precipitation in mm
    - yield.csv: annual soybean yield in bushels per acre
- Custom methods are stored in `src/`.


##  Results

Key findings and model performance are documented directly in the notebook.

## Notes

This project was completed as part of a technical assessment.