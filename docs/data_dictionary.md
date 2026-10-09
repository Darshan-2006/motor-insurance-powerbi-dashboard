# Data Dictionary: `motor_data14-2018.csv`

508,499 rows × 16 columns. One row = one policy period for one insured object (vehicle).

| Column | Type | Description | Notes |
|---|---|---|---|
| `SEX` | int | Policyholder category code | 0, 1, 2 (labels not documented in the source) |
| `INSR_BEGIN` | date (`dd-Mon-yy`) | Policy start date | Used for the year axis |
| `INSR_END` | date (`dd-Mon-yy`) | Policy end date | |
| `EFFECTIVE_YR` | text | Effective year/month code | Mixed values (e.g. 11, 15, 95); 3 missing |
| `INSR_TYPE` | int | Insurance type code | 1201, 1202, 1204 |
| `INSURED_VALUE` | float | Sum insured | 0 for some rows |
| `PREMIUM` | float | Premium charged | 13 missing |
| `OBJECT_ID` | int | Vehicle identifier | 223,136 unique vehicles |
| `PROD_YEAR` | float | Vehicle production year | 63 missing |
| `SEATS_NUM` | float | Number of seats | Outliers up to 198 |
| `CARRYING_CAPACITY` | float | Carrying capacity | ~23 % missing |
| `TYPE_VEHICLE` | text | Vehicle type | 11 categories (Motor-cycle, Truck, Pick-up, …) |
| `CCM_TON` | float | Engine cc or tonnage | 6 missing |
| `MAKE` | text | Vehicle make | 746 distinct; 5 missing |
| `USAGE` | text | Usage category | 14 categories (Own Goods, Private, Taxi, …) |
| `CLAIM_PAID` | float | Claim amount paid | Blank = no claim (92.6 % of rows) |

## Report measures

| Measure | Logic |
|---|---|
| Policies Opened | Count of policy rows in the filter context |
| Total Premium | Sum of `PREMIUM` |
| Total Claims | Sum of `CLAIM_PAID` |
| Premium To Claims Ratio | Total Premium ÷ Total Claims |
| Avg Premium | Total Premium ÷ Policies |
| Avg Claim2 | Total Claims ÷ Policies |
| Claim Count | Count of rows with a `CLAIM_PAID` value |

The logic above is reconstructed from the report's numbers and reproduced in `scripts/profile_data.py`, which matches the dashboard exactly (for example 2018: 384 M premium, 337 M claims, 114 %, 1,979 claims).
