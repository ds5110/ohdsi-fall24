from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
table = "discharge_one"
query = f"""
SELECT *
FROM {work_schema}.{table}
;
"""
# run_query(con, query)
df = read_df(con, query)

print(df.info())

dischargeID_to_cat = {
    0:'Category 1 - Home',
    38004519:'Category 1 - Home',
    581476:'Category 1 - Home',
    9202:'Category 1 - Home',
    8920:'Category 2 - Inpatient Rehab',
    38004285:'Category 2 - Inpatient Rehab',
    8676:'Category 3 - Skilled Nursing',
    8863:'Category 3 - Skilled Nursing',
    38004277:'Category 3 - Skilled Nursing',
    8717:'Category 4 - Acute Care',
    32276:'Category 4 - Acute Care',
    32254:'Category 4 - Acute Care',
    8546:'Category 5 - Acute Care',
    8951:'Category 5 - Acute Care',
    38004284:'Category 5 - Acute Care',
    38003619:'Category 5 - Acute Care'
} 

df['category'] = df['discharge_to_concept_id'].map(dischargeID_to_cat)

# Convert the data type to str for plotting purpose.
#df["discharge_to_concept_id"] = df["discharge_to_concept_id"].apply(str)

'''plt.figure(figsize=(12,6))
sns.histplot(data=df, x="discharge_to_concept_id")
plt.xticks(rotation=90)
plt.xlabel("Discharge to type", labelpad=20)'''

plt.figure(figsize=(12,6))
sns.histplot(data=df, x="category", hue="category", palette="ocean", shrink=0.9)
plt.xticks(rotation=90)
plt.xlabel("Discharge by Category", fontsize=14, labelpad=20)
plt.ylabel("Count", fontsize=14, labelpad=20)

plt.savefig("figs/discharge_one.png", bbox_inches="tight")
plt.show()
