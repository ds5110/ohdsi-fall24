# Create intermediate tables.
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

visit_oc_discharge:
	python -B src/visit_oc_discharge.py

visit_oc_first_discharge:
	python -B src/visit_oc_first_discharge.py
	
visit_oc_second_discharge:
	python -B src/visit_oc_second_discharge.py

condition_oc_stroke_cohort:
	python -B src/condition_oc_stroke_cohort.py

condition_oc_discharge:
	python -B src/condition_oc_discharge.py
	
condition_oc_first_discharge:
	python -B src/condition_oc_first_discharge.py

speech:
	python -B src/speech.py
	
speech_stroke_cohort:
	python -B src/speech_stroke_cohort.py

visit_detail_stroke_cohort:
	python -B src/visit_detail_stroke_cohort.py

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

# Utility.
drop_table:
	python -B src/drop_table.py

read_table:
	python -B src/read_table.py

# Test tutorial files.
test:
	python -B src/test.py

test_create_table:
	python -B src/template_create_table.py

test_write_table:
	python -B src/template_write_syn_cohort.py

test_pandas:
	python -B src/template_pandas.py

test_delete_table:
	python -B src/template_delete_table.py