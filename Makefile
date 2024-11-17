inpatient_stroke:
	python -B src/inpatient_stroke.py

stroke_cohort_w_aphasia:
	python -B src/stroke_cohort_w_aphasia.py

plot_stroke_desc_concept:
	python -B src/plot_stroke_desc_concept.py

plot_has_aphasia:
	python -B src/plot_has_aphasia.py

stroke_cohort_w_aphasia_FALSE:
	python -B src/stroke_cohort_w_aphasia_FALSE.py

stroke_cohort_w_aphasia_TRUE:
	python -B src/stroke_cohort_w_aphasia_TRUE.py

stroke_ancestor:
	python -B src/stroke_ancestor.py

plot_stroke_type_aphasia_TRUE:
	python -B src/plot_stroke_type_aphasia_TRUE.py

plot_stroke_type_aphasia_FALSE:
	python -B src/plot_stroke_type_aphasia_FALSE.py

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