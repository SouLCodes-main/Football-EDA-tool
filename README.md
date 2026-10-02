# Football EDA & Tactical Analysis Tool ⚽📊

An Exploratory Data Analysis (EDA) and basic machine learning project examining the mathematical relationship between ball possession percentages and offensive output in top-tier football matches. 

This project cleans raw match logs, isolates key performance indicators, and computes a linear regression line of best fit using NumPy vector operations.

---

## 🚀 Features

- **Data Cleaning Pipeline:** Handles non-numeric strings, coerced missing values, and type conversions using `pandas`.
- **Vectorized Data Sorting:** Sorts continuous features to eliminate rendering artifacts during line plotting.
- **Linear Trend Modeling:** Computes slope ($m$) and intercept ($c$) via `numpy.polyfit` to model expected goals against possession metrics ($y = mx + c$).
- **Data Visualization:** Renders 2D scatter plots overlaid with calculated regression trendlines using `matplotlib`.

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Environment & Dependency Manager:** [uv](https://github.com/astral-sh/uv)
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib`

---

## 📋 Project Structure

```text
Football-EDA-tool/
├── data.csv            # FBref raw match log dataset
├── main.py             # Main data cleaning & visualization script
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Lockfile for reproducible builds
└── README.md           # Project documentation
⚙️ Quick Start
1. Prerequisites
Ensure you have uv installed on your system.

2. Installation & Setup
Clone the repository and install dependencies:

Bash
git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/Football-EDA-tool.git
cd Football-EDA-tool
uv sync
3. Run the Script
Execute the analysis script inside the isolated uv virtual environment:

Bash
uv run main.py
📊 Sample Output & Insights
The tool plots match-by-match possession against total goals scored (GF).

Plaintext
Equation: y = -0.041x + 4.382
Tactical Observation: In the analyzed match sample, higher ball possession yields a negative slope (m<0), visually highlighting the concept of "sterile possession"—where dominating the ball does not automatically translate to a higher goal tally.

