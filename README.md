# Identification of Patterns in Stroke Care Transitions using [OHDSI](https://ohdsi.northeastern.edu/) Pharmetrics+ data

Should we include a brief version of the story here?

## OHDSI + Setup

In order to access the OHDSI database, several initial steps are required. The user must complete CITI certifications specified by Northeastern's Observational Health Data Sciences and Informatics Center (OHDSI). After the certifications are completed, the user will follow OHDSI's [User Guide](https://northeastern.sharepoint.com/sites/OHDSINortheastern/Shared%20Documents/Forms/AllItems.aspx?ga=1&OR=Teams%2DHL&CT=1728075445537&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI1MC8yNDA4MTcwMDQyMSIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&id=%2Fsites%2FOHDSINortheastern%2FShared%20Documents%2FOHDSI%20Lab%20%2D%20User%20Group%2FUser%20Guide%2FLatest&viewid=e9534233%2D4089%2D42ed%2D8956%2D298feac7e723) to onboard onto OHDSI's dashboard and then set up the virtual desktop with AWS Workspaces. The primary tutorials provided for environment set up are in R so we created a tutorial to set up an enviroment using Python. Details are included below.

## Step 0

These steps work in relation to one having access to OHDSI's Amazon Workspace.

Follow each step in the [tutorial.md](tutorial/tutorial.md) file in this repo.
Steps include:

1. AWS Setup
2. Miniconda
3. Python environment
4. git
5. make
6. Config of Redshift credentials
7. Redshift database connection
8. Pandas to process tables, read, and write

<small>_Refer to [config_template.ini](/tutorial/config_template.ini) and [how_to_use_templates.md](/tutorial/how_to_use_templates.md) for additional help._</small>

## Step 1

Run Casey's query to create the stroke cohort?

```
 make tbd
```

## Step 2

tbd

```
 make tbd
```

## Step 3

tbd

```
 make tbd
```

## Step 4

tbd

```
 make tbd
```

## Step 5

tbd

```
 make tbd
```

## Lessons Learned

1. Did your project objectives change based on what your learned from the data or stakeholder?

   Our objectives changed both as we explored the data and as we met with the stakeholder each week to share our progress. Rob provided insight into the potential ways to access the data we needed for analysis of care pathways. He provided stroke and speech language codes and suggestions for how to determine if a visit could fall under PT vs OT. As our team tested tables and fields in queries, we often ran into dead ends because of missing data.

2. Were data-access or data processing challenges harder than you anticipated?

   As noted in our [docs/README.md](docs/README.md), there was a learning curve with the complexity of the OHDSI database since the data is drawn from real-world interactions and the schema connections can be hard to navigate without a medical knowledge. A medical condition can have various codes associated with it, and these codes can also change throughout a patient's care timeline.

## Next Steps - TO DO

1. Briefly describe and prioritize some next steps that you would take given sufficient time/resources.

2. Prioritize these somehow. For example: those that should be easy/hard, those that require more data, etc

Small next steps

- to-do
- to-do

Longer term next steps

- to-do
- to-do

## Attributions

#### Rob Cavanaugh | Stakeholder

- [List of speech language codes](https://northeastern-my.sharepoint.com/:w:/g/personal/r_cavanaugh_northeastern_edu/EffBdbdsX4hHokqQF2ryo9wBL7VERApjQ5klmlApGWdqzw?e=5w74PB)

#### Casey Tilton | Data Science Capstone Student

- [SQL query for cohort creation](https://northeastern-my.sharepoint.com/personal/tilton_ca_northeastern_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftilton%5Fca%5Fnortheastern%5Fedu%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files%2Fstroke%5Fcohort%5Fcreation%2Esql&parent=%2Fpersonal%2Ftilton%5Fca%5Fnortheastern%5Fedu%2FDocuments%2FMicrosoft%20Teams%20Chat%20Files&ga=1)

#### Philip Bogden | DS5110 Professor

- [git-intro repo](https://github.com/ds5110/git-intro)

## Resources

**OHDSI**

- [OHDSI Northeastern](https://ohdsi.northeastern.edu/)
- [OHDSI @ Northeastern | Sharepoint](https://northeastern.sharepoint.com/sites/OHDSINortheastern/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FOHDSINortheastern%2FShared%20Documents%2FOHDSI%20Lab%20%2D%20User%20Group&p=true&ga=1&OR=Teams%2DHL&CT=1728075445537&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI1MC8yNDA4MTcwMDQyMSIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D)
- [OHDSI User Guide](https://northeastern.sharepoint.com/sites/OHDSINortheastern/Shared%20Documents/Forms/AllItems.aspx?ga=1&OR=Teams%2DHL&CT=1728075445537&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI1MC8yNDA4MTcwMDQyMSIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&id=%2Fsites%2FOHDSINortheastern%2FShared%20Documents%2FOHDSI%20Lab%20%2D%20User%20Group%2FUser%20Guide%2FLatest&viewid=e9534233%2D4089%2D42ed%2D8956%2D298feac7e723)
- [The Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/)
- [OHDSI Lab Login](https://ohdsi-lab.roux-ohdsi-prod.aws.northeastern.edu/#/login)
- [Athena](https://athena.ohdsi.org/search-terms/start)

<br>

**OMOP**

- [OMOP Common Data Model](https://ohdsi.github.io/CommonDataModel/index.html)
- [OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html)
