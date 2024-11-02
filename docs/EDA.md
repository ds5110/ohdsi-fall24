# Exploratory Data Analysis (EDA)

# Setup

- Read [tutorial](tutorial.md) to setup your environment.
- [how_to_use_templates](how_to_use_templates.md) teaches you how to use python to access redshift database. You can use dbeaver as a visualization tool with it.

## Create intermediate tables

- Following command will create a table 'inpatient_stroke' into your work schema:

```
make inpatient_stroke
```

- Following command will create a table 'stroke_cohort_w_aphasia' into your work schema:

```
make stroke_cohort_w_aphasia
```

## Analysis

- Run following command to get table information and figures from 'stroke_cohort_w_aphasia':

```
make test
```

- The info of Pandas dataframe of 'stroke_cohort_w_aphasia' is following:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 67128 entries, 0 to 67127
Data columns (total 10 columns):
 #   Column                         Non-Null Count  Dtype
---  ------                         --------------  -----
 0   condition_occurrence_id        67128 non-null  int64
 1   person_id                      67128 non-null  int64
 2   condition_concept_id           67128 non-null  int64
 3   condition_start_date           67128 non-null  object
 4   condition_end_date             67128 non-null  object
 5   row_num                        67128 non-null  int64
 6   observation_period_start_date  67128 non-null  object
 7   observation_period_end_date    67128 non-null  object
 8   observation_period_id          67128 non-null  int64
 9   has_aphasia                    67128 non-null  int64
dtypes: int64(6), object(4)
```

- The number of data points are reduced to 67128, since we are only looking into datapoints that are 'inpatient' and 'strokes'. This is much manageable size of data now.

<br>
<img src="../figs/test.png" width=600>
<br>

- The plot shows that '443454' code, which is Cerebral infarction, is the most common case.
- There are many other 'condition_concept_id' in here, which are more specific disease codes within the 7 strokes.
  <br>
  <br>

# Further Proposal Notes

Our project will establish stroke patient ‘paths’ through treatment, to further disaggregate the initial cohort definition that captures first-occurance in-patient and emergency department stroke diagnosis. We will focus our path on physical location of patients while receiving treatment, and indication of whether they have received physical/occupational and/or speech therapy. The objective is to create defined paths that will support future research on the efficacy of different treatment processes, timing, and duration.

Our cohort definition is based on a SQL query developed by Casey Tilton, a capstone student also working with the OHDSI database on questions around stoke victims. We plan to review and refine Casey’s script; his original SQL code is stored here: docs/Stroke_cohort.md

**Population (N) = 67,000**

(N may change as we refine the cohort definition)

TABLES 1 and 2: Summary statistics (mean, median, STD DEV, max, min, quartiles) for the following to inform potential categorization or groupings:

- Number of occurences attached to each patient
- Time (in days) from first stroke occurance to final treatment occurance associated with the stroke

Hypothesis: The first 'cut' will be to divide N by type of stroke dianosis rather than the first actual activity related to the patient, as the category of stroke is a more important demarcation than the type of each initial visit.

**The Stroke Diagnosis Categories Are:**

<img src="img/stroke_ids.png" width=300>
<br>
<br>

    IMAGE1: histogram of n for each type of stroke, with data point inserted for each n

**Each of the different diagnosis groups will then be divided by In-patient, Emergency room, or Combination first visit:**

<img src="img/Inpatient_ids.png" width=300>
<br>
<br>

    IMAGE2: Multiple histogram plots with each stroke type by in-patient, ER, or combination

**From there, each group, now divided first by diagnosis and then by ER-only, inpatient, and combination will be further divided into discharge type:**

- Home Visit
- Discharged to Home
- Rehabilitation Hospital
- Skilled Nursing Facility
- Home Health Agency
- Long Term Care Facility
- Hospice

Note that further investigations may find that the following additional, low incidence discharge facilities may be appropriately included in one of the larger above groups. We will run separate analysis of these groups to determine if their subsequent experience and process is close enough to the top seven discharge facilities to include in one:

- Intermediate Medical Care Facility
- Hospital Swing Beds
- Critical Access Hospital
- Comprehensive Inpatient Rehabiloitation Facility

At this point, there will be the following initial paths:

- Type of stroke (7 separate groups including dependencies)
- Initial visit (7 stroke types divided into three visit types, or 21 groups)
- Discharge destination (21 groups divided into 7 discharge locations or 147 groups)

The project stakeholder has suggested we end the trace of a path when the cohort following the path reaches approximately n = 1% to 2% of the original cohort group, or when the path reaches a ‘dead end’ because remaining data splits are not relevant.

Potential further path tracing, dependent on sample size in group (minimum n for pursuing addition paths approxiamtely 670 unique patients):

- Type of therapy (physical/occupational combined, speech alone, physical/occupational/speech combined) for 441 groups
- To identify if there is a need for and establish the appropriate groupings for duration of therapy (measured in number of occurances):

TABLE 3: Summary statistics (mean, median, STD DEV, max, min, quartiles) of total overall occurances for all physical, occupational, and speech therapies
<br>
<br>

# Background

**Entity-Relationship Diagram of OMOP, the model OHDSI is based on:**

![](https://raw.githubusercontent.com/OHDSI/CommonDataModel/main/rmd/images/erd.jpg)

<br>
<br>

**Our edited version of the ER diagram based on the current Cohort Query:**

<img src="img/cohort_er_diagram.png" width=500>
