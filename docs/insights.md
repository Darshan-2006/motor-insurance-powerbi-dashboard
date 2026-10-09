# Insights

All figures computed with `scripts/profile_data.py`. Year = year of `INSR_BEGIN`.

## By year

| Year | Policies | Premium | Claims | Premium ÷ Claims | Claim freq. |
|---|---|---|---|---|---|
| 2014 | 65,870 | 518 M | 1,510 M | 34 % | 9.4 % |
| 2015 | 116,015 | 927 M | 2,699 M | 34 % | 8.2 % |
| 2016 | 130,412 | 1,047 M | 2,666 M | 39 % | 7.9 % |
| 2017 | 138,902 | 1,163 M | 1,968 M | 59 % | 7.0 % |
| 2018 | 57,300 | 384 M | 337 M | 114 % | 3.5 % |

2018 is a partial year and recent claims are still being reported, so its ratio is overstated.

## By policyholder group (`SEX`)

| Code | Policies | Claim freq. | Premium ÷ Claims |
|---|---|---|---|
| 0 | 247,055 | 9.7 % | 69 % |
| 1 | 217,809 | 5.2 % | 29 % |
| 2 | 43,635 | 5.8 % | 37 % |

Group 0 claims most often. Group 1 claims less often but much more expensively, so it has the worst ratio.

## Vehicle types

- **Motor-cycle**: 105,977 policies, 0.5 % claim frequency, ratio 286 % (profitable).
- **Tractor**: ratio 335 % on a small base (7.5 K policies).
- **Trailers/semitrailers**: ratio 21 % (weakest large segment).
- **Truck**: highest premium (1.43 B), ratio 33 %.
- **Station wagons** have the highest claim frequency (12.4 %), followed by buses (11.6 %).

## Suggested follow-ups

- Re-price or review trucks and trailers, where claims run at 3–5× premium.
- Rerun the analysis once 2018 is complete.
- Obtain labels for `SEX` and `INSR_TYPE` codes.
- Remove the 78 duplicate rows in Power Query.
