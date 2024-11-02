from utils import config, read_df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

con, work_schema = config()
table = "stroke_cohort_w_aphasia"

query = f"""
SELECT *
FROM {work_schema}.{table}
"""

df = read_df(con, query)

print(df.info())

df["condition_concept_id"] = df["condition_concept_id"].apply(str)
sns.histplot(data=df, x="condition_concept_id")
# sns.jointplot(
#    data=df, x="condition_concept_id", y="condition_occurrence_id", kind="hist"
# )
plt.xticks(rotation=60)
plt.savefig("figs/test.png")
plt.show()
