"""Quick data-quality and KPI profile for the motor insurance dataset.

Usage:
    python scripts/profile_data.py [path/to/motor_data14-2018.csv[.gz]]

Reproduces the dashboard KPIs outside Power BI so the numbers can be verified.
Requires: pandas
"""
import sys
from pathlib import Path

import pandas as pd

DEFAULT = Path(__file__).resolve().parents[1] / "data" / "raw" / "motor_data14-2018.csv.gz"


def main(path: Path) -> None:
    df = pd.read_csv(path)
    df["YEAR"] = pd.to_datetime(df["INSR_BEGIN"], format="%d-%b-%y", errors="coerce").dt.year

    print(f"Rows: {len(df):,} | Columns: {df.shape[1] - 1} | Exact duplicate rows: {df.duplicated().sum():,}")
    print("\nMissing values:")
    print(df.isna().sum()[lambda s: s > 0].to_string())

    def kpis(g: pd.DataFrame) -> pd.Series:
        premium, claims = g["PREMIUM"].sum(), g["CLAIM_PAID"].sum()
        return pd.Series({
            "policies": len(g),
            "total_premium": premium,
            "total_claims": claims,
            "premium_to_claims": premium / claims if claims else float("nan"),
            "avg_premium": premium / len(g),
            "avg_claim": claims / len(g),
            "claim_count": g["CLAIM_PAID"].notna().sum(),
            "claim_frequency": g["CLAIM_PAID"].notna().mean(),
        })

    pd.options.display.float_format = "{:,.3f}".format
    print("\nOverall KPIs:\n", kpis(df).to_string())
    for col in ["YEAR", "SEX", "TYPE_VEHICLE", "USAGE"]:
        print(f"\nKPIs by {col}:\n", df.groupby(col).apply(kpis, include_groups=False).to_string())


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT)
