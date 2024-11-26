# Identification of Patterns in Stroke Care Transitions, using [OHDSI](https://ohdsi.northeastern.edu/) Pharmetrics+ data

## Story

Strokes are the leading cause of long-term disability in the United States; there are in excess of 800,000 new strokes annually and most of the approximately 680,000 survivors suffer from a combination of life-altering deficits in mobility, cognition, independence in daily activities, and communication.

The most critical point in stroke treatment is, of course, at the onset. Timely care for a stroke victim means the difference between life and death but also influences the severity of longer-term issues. Our work does not include evaluation of initial care nor time elapsed from stroke onset to initial treatment. Our proposal is to focus on treatment after the patient has been discharged from the emergency room or in-patient hospital after their first stroke occurrence, independent of the severity of the initial event.

Stroke survivors receive rehabilitation services (physical therapy, occupational therapy, and/or speech-language therapy) in different locations at different rates in the year following their stroke. The physical location of care could be the acute inpatient hospital, inpatient rehabilitation facilities, skilled nursing facilities, long-term acute care hospitals, home health services, and outpatient care. The composition of care can include physical, occupational, and/or speech therapy, delivered daily, weekly, or other cadence. Differences between levels of care location as well as type of care delivered has been identified as a path to understanding the differences in the quality of stroke post-acute treatment in order to optimize stroke outcomes.

A critical missing piece of information in improving care is to better understand the pathways stroke survivors take across these levels of care locations. Our hypothesis is that it is possible to trace the various paths that stroke survivors take through post-incident care so that the efficacy and efficiency of the different care transitions can be evaluated.

Our project will establish stroke patient ‘paths’ through treatment, to further disaggregate the initial cohort definition that captures first-occurrence in-patient and emergency department stroke diagnosis. We will focus our path on the physical location of patients after inpatient discharge, and indication of whether they have received physical/occupational and/or speech therapy. The objective is to create defined paths that will support future research on the efficacy of different treatment processes, location, and duration.

## Approach

Our cohort definition is based on a SQL query developed by Casey Tilton, a capstone student also working with the OHDSI database on questions around stoke victims. Casey's cohort query focuses on a set of 7 stroke codes highlighted by the project stakeholder, Rob Cavanaugh, along with a focus on aphasia, which is an area of study for the stakeholder.

We chose to add the presence or absence of aphasia, or speech difficulty, to our original scope to enable comparisons of treatment between stroke patients with aphasia and without. The path tracing for post stroke care transitions will be attempted using the IQVIA Pharmetrics+ database, a large commercial health insurance claims database that is part of the OHDSCI system. Once these paths are developed, the next step in analysis could be to investigate the potential for developing an outcome score to compare the different treatment locations and plans. That score development is currently outside the scope of this project.

**The deliverables that we plan to produce in this project will be:**

- Creation of the various cohorts that will represent each path (could be as many as 147 different groups, depending on cohort size)

- Visualization of stroke patient paths through post-acute treatment

- A set of reproducible SQL scripts for each relevant path cohort so that future analysts can both replicate our work and produce the cohorts necessary to bring the work through to the next step in the process, e.g. creating an outcome score to compare the efficacy of treatment paths

- A comprehensive set of instructions to access and manipulate OHDSCI using Python scripts. Currently, documentation centers on the use of R for working with the OHDSCI database. Our set of instructions, which we plan to additionally include in a separate public repo, will complement exisiting documentation and be a tool for future students and researchers to reference when interacting with OHDSI.

**Challenges that this project will likely face:**

- The dataset itself is complex; there is a steep and time-consuming learning curve to simply access the data

- The dataset is incomplete, and critical pieces of information may not be available for our analysis

- All of the supporting documentation to which we have access has been created for R users, and many data scientists and researchers prefer to work in Python (ourselves included)
  <br>
  <br>
