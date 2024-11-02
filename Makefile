test_create_table:
	python -B src/template_create_table.py

test_write_table:
	python -B src/template_write_syn_cohort.py

test_pandas:
	python -B src/template_pandas.py

test_delete_table:
	python -B src/template_delete_table.py

inpatient_stroke:
	python -B src/inpatient_stroke.py

stroke_cohort_w_aphasia:
	python -B src/stroke_cohort_w_aphasia.py

test:
	python -B src/test.py
