# Create intermediate tables.
create_tables:
	python -B src/inpatient_stroke.py
	python -B src/stroke_cohort_w_aphasia.py
	python -B src/stroke_cohort_w_aphasia_FALSE.py
	python -B src/stroke_cohort_w_aphasia_TRUE.py
	python -B src/stroke_ancestor.py
	python -B src/discharge_ancestor.py
	python -B src/visit_oc_stroke_cohort.py
	python -B src/stroke_cohort_w_aphasia_co.py
	python -B src/stroke_cohort_w_aphasia_co_vo.py
	python -B src/speech_therapy_count_dates.py

# Individual commands for creating intermediate tables.
inpatient_stroke:
	python -B src/inpatient_stroke.py

stroke_cohort_w_aphasia:
	python -B src/stroke_cohort_w_aphasia.py

stroke_cohort_w_aphasia_FALSE:
	python -B src/stroke_cohort_w_aphasia_FALSE.py

stroke_cohort_w_aphasia_TRUE:
	python -B src/stroke_cohort_w_aphasia_TRUE.py

stroke_ancestor:
	python -B src/stroke_ancestor.py

discharge_ancestor:
	python -B src/discharge_ancestor.py

visit_oc_stroke_cohort:
	python -B src/visit_oc_stroke_cohort.py

stroke_cohort_w_aphasia_co:
	python -B src/stroke_cohort_w_aphasia_co.py

stroke_cohort_w_aphasia_co_vo:
	python -B src/stroke_cohort_w_aphasia_co_vo.py

speech_therapy_count_dates:
	python -B src/speech_therapy_count_dates.py

src/new_visit_occ_5_discharge:
	python -B src/new_visit_occ_5_discharge.py

# Plot.
plot_stroke_desc_concept:
	python -B src/plot_stroke_desc_concept.py

plot_has_aphasia:
	python -B src/plot_has_aphasia.py

plot_stroke_type_aphasia_TRUE:
	python -B src/plot_stroke_type_aphasia_TRUE.py

plot_stroke_type_aphasia_FALSE:
	python -B src/plot_stroke_type_aphasia_FALSE.py

plot_first_discharge:
	python -B src/plot_first_discharge.py
	python -B src/plot_first_discharge_aphasia_TRUE.py
	python -B src/plot_first_discharge_aphasia_FALSE.py

plot_speech_therapy_aphasia:
	python -B src/plot_speech_therapy_aphasia.py

# Utility.
drop_table:
	python -B src/drop_table.py

read_table:
	python -B src/read_table.py

# Test file.
test:
	python -B src/test.py
