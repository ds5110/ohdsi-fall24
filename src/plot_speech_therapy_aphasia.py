from utils import config, read_df, write_df, run_query
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


con, work_schema = config()
omop_schema = "omop_cdm_53_pmtx_202203"
omop_table = "concept"
work_table = "cohort_aphasia_speech_therapy"
work_table_2 = "stroke_cohort_w_aphasia"
query = f"""
SELECT ca.*, sc.has_aphasia
FROM {work_schema}.{work_table} ca
JOIN {work_schema}.{work_table_2} sc
    ON ca.person_id = sc.person_id
;
"""

df = read_df(con, query)
colors = ['#2292B5', '#001349']

print(df.info())
print(df)

df_aphasia_true = df[df["has_aphasia"] == 1]
df_aphasia_false = df[df["has_aphasia"] == 0]
cnt_visit_aphasia_true = df_aphasia_true["total_visits"].sum()
cnt_visit_aphasia_false = df_aphasia_false["total_visits"].sum()
cnt_patient_aphasia_true = len(df_aphasia_true)
cnt_patient_aphasia_false = len(df_aphasia_false)

# Plot.


fig, ax = plt.subplots()
plt.bar(
    ["Has Aphasia", "No Aphasia"],
    [
        cnt_visit_aphasia_true / cnt_patient_aphasia_true,
        cnt_visit_aphasia_false / cnt_patient_aphasia_false,
    ], color=colors
)
plt.xlabel("Aphasia Status", fontsize=12, labelpad=15)
plt.ylabel("Total visits of speech therapy per person", fontsize=12, labelpad=15)
plt.title("Speech Therapy Visits Based on Aphasia Status", fontsize=14, weight="bold", pad=20)
plt.tight_layout()
plt.savefig("figs/speech_therapy_aphasia.png")
plt.show()
