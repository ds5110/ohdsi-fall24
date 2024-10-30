# Exploratory Data Analysis (EDA)

Per instructions in the class repo: (will delete, here for reference)

- Add an "eda.md" file to your repository that includes the following...
- Exploratory Data Analysis (EDA) should demonstrate data accessibility.
- The data should be visualized in a manner that adds insights on the project's analytic objectives & proposal.
- Use results of the EDA to demonstrate that your project objectives are feasible.
- Figures should support the feasibility of the project objectives.
- Create a "docs/draft.md" that describes your EDA and proposal to the general public.
- EDA will be graded like a hoomework assignment.
- "eda.md" must be reproducible following the guidance in https://ds5110/git-intro

# Note that currently we do not have access to our AWS workspaces (though we have been able to access the AWS previously) so we have indicated where data and images will be inserted once that problem is resolved:

Our project will establish stroke patient ‘paths’ through treatment, to further disaggregate the initial cohort definition that captures first-occurance in-patient and emergency department stroke diagnosis.  We will focus our path on physical location of patients while receiving treatment, and indication of whether they have received physical/occupational and/or speech therapy.  THe objective is to create defined paths that will support future research on the efficacy of different treatment processes, timing, and duration. 

Our cohort definition is based on a SQL query developed by Casey Tilton, a capstone student also working with the OHDSI database on questions around stoke victims. We plan to review and refine Casey’s script; his original SQL code is stored here: docs/Stroke_cohort.md

Population (N) = 67,000
(N may change as we refine the cohort definition)

TABLES 1 and 2: Summary statistics (mean, median, STD DEV, max, min, quartiles) for the following to inform potential categorization or groupings:

- Number of occurences attached to each patient
- Time (in days) from first stroke occurance to final treatment occurance associated with the stroke

Hypothesis: The first 'cut' will be to divide N by type of stroke dianosis rather than the first actual activity related to the patient, as the category of stroke is a more important demarcation than the type of each initial visit. 

The stroke diagnosis categories are:

Concept ID and Name

372924	Cerebral artery occlusion

375557	Cerebral embolism

376713	Cerebral hemorrhage

443454	Cerebral infarction

441874	Cerebral thrombosis

439847	Intracranial hemorrhage

432923	Subarachnoid hemorrhage



    IMAGE1: histogram of n for each type of stroke, with data point inserted for each n



Each of the different diagnosis groups will then be divided by in-patient, emergency room, or combination first visit

Concept ID and Name

262 Emergency Room and Inpatient Visit

9203 Emergency Room Visit

9201 Inpatient Visit



    IMAGE2: Multiple histogram plots with each stroke type by in-patient, ER, or combination



From there, each group, now divided first by diagnosis and then by ER-only, inpatient, and combination will be further divided into discharge type:

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


