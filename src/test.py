from utils import config, read_df
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

con, work_schema = config()
table = "inpatient_stroke"  # "stroke_cohort_w_aphasia"

query = f"""
SELECT *
FROM {work_schema}.{table}
"""

df = read_df(con, query)

print(df.info())
condition_concept_id_instroke = df["condition_concept_id"].unique().apply(str)
print(condition_concept_id_instroke)
"""
condition_concept_id of inpatient_stroke
[  443454  4108356 45767658 45772786  4017107  4134162  4144154  4148906
 43530727  4110192  4111709  4043731  4071732  4306943  4110190  4006294
  4110189 46273649  4176892 43530851 42873157 37016924 42535425 43530674
  4049659 46270031  4110186   434155   372924 40479572  4048277   260841
  4345688  4046360  4319328   436430   444197  4112023  4111717   444198
  4111708  4045738   444196  4111716  4108952  4111714   437106  4249574
  4071589  4048606  4048278  4048279  4130539  4045737  4196276   432923
   376713   436526   378544  4071066   439040  4154699  4196275   438595]
   """

df["condition_concept_id"] = df["condition_concept_id"].apply(str)
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x="condition_concept_id")
# sns.jointplot(
#    data=df, x="condition_concept_id", y="condition_occurrence_id", kind="hist"
# )
plt.xticks(rotation=90)
plt.xlabel("Condition concept id", labelpad=20)
plt.savefig("figs/test.png", bbox_inches="tight")
plt.tight_layout()
plt.show()
