# Exploratory Data Analysis (EDA)

Our project will establish stroke patient ‘paths’ through treatment, to further disaggregate the initial cohort definition that captures first-occurance in-patient and emergency department stroke diagnosis and subsequent treatments.

Our cohort definition is based on a SQL query developed by Casey Tilton, a capstone student also working with the OHDSI database on questions around stoke victims.  We plan to review and refine Casey’s script; his original SQL code is stored here: (link to a MD file in the doc folder with Casey’s code)

Population (N) =  
(N may change as we refine the cohort definition)

We could pull summary statistics (mean, median, STD DEV, max, min) - I think that statistics that reflect Casey’s query could be a useful guide:
* Number of records attached to each patient
* Time (in days) from first patient record to first stroke record
* Elapsed time (in days) of complete patient record



The project stakeholder has suggested we end the trace of a path when the cohort following the path reaches approximately n =  1 to 2% of the original cohort group, or when the path reaches a ‘dead end’ because remaining data splits are not relevant.

Hypothesis: The first 'cut' will be to divide N by type of stroke dianosis rather than the first actual activity related to the patient, as the category of stroke is a more important demarcation than the type of each initial visit

(image = histogram of n for each type of stroke, with data point inserted for each n)

Each of the different diagnosis groups will then be divided by in-patient, emergency room, or combination visit

(Multiple plots with each stroke type by in-patient, ER, or combo)

To identify the appropriate hospital stay groupsing, the length of stay in days for in-patient and combo patients will be bucketed by quartile - show statisitcs for quartiles, but if those numbers are too small, break into thirds

From there, each group will be further divided into discharge type:
* Home Visit
* Discharged to Home
* Rehabilitation Hospital
* Skilled Nursing Facility
* Home Health Agency
* Long Term Care Facility
* Hospice

Note that further investigations may find that these additional, low incidence discharge facilities may be appropriately included in one of the larger above groups.  We will run separate analysis of these groups to determine if their subsequent experience and process is close enough to the top seven discharge facilities to include:
* Intermediate Medical Care Facility
* Hospital Swing Beds
* Critical Access Hospital
* Comprehensive Inpatient Rehabiloitation Facility
