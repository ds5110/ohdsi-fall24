from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
table = "stroke_cohort_w_aphasia"
query = f"""
SELECT *
FROM {work_schema}.{table}
;
"""
# run_query(con, query)
df = read_df(con, query)

# Print info of the table.
print(df.info())

# Convert the data type to str for plotting purpose.
df["has_aphasia"] = df["has_aphasia"].apply(str)

# Plot.
fig, ax = plt.subplots()
sns.histplot(data=df, x="has_aphasia")
ax.set_xticklabels(["No Aphasia", "Has Aphasia"])
plt.savefig("figs/aphasia_dist.png", bbox_inches="tight")
plt.tight_layout()
plt.show()
