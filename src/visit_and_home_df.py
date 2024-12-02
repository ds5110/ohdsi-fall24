from utils import config, read_df, write_df, run_query
import pandas as pd
from discharge_to_concept_id import total_id

# this function creates separate dataframes for visit locations 1 - 5 within six months of diagnosis, with visit #1 being the original location post-diagnosis. 
# once the patient is discharged to home, that event is recorded in the at_home dataframe
# from here, procedures tied to dates can be appended to the locations or to home for further analysis 

def visit_and_home_df():
    # Configurations
    con, work_schema = config()
    work_table = "visit_occurrence_discharge_all"
    omop_schema = "omop_cdm_53_pmtx_202203"
    omop_table = "procedure_occurrence"
    work_table_aphasia = "stroke_cohort_w_aphasia"

    # Query to fetch visit data
    query = f"""
    SELECT *
    FROM {work_schema}.{work_table}
    ;
    """

    # Execute the query and fetch the results into a Pandas DataFrame
    df = read_df(con, query)

    # Ensure date columns are in datetime format
    df["visit_end_date"] = pd.to_datetime(df["visit_end_date"])
    df["condition_start_date"] = pd.to_datetime(df["condition_start_date"])

    # Filter rows where visit_end_date is within 180 days of condition_start_date
    df = df[
        (df["visit_end_date"] > df["condition_start_date"])
        & (df["visit_end_date"] <= df["condition_start_date"] + pd.Timedelta(days=180))
    ]

    # Filter rows where discharge_to_concept_id is valid
    valid_concept_ids = set(total_id.keys())
    df = df[df["discharge_to_concept_id"].isin(valid_concept_ids)]

    # Map discharge_to_concept_id to its label
    df["discharge_to_concept_id"] = df["discharge_to_concept_id"].map(total_id)

    # Add a row number per person_id to distinguish multiple pairs
    df["pair_number"] = df.groupby("person_id").cumcount() + 1

    # Sort by person_id and pair_number to ensure sequential order
    df = df.sort_values(by=["person_id", "pair_number"])

    # Shift the discharge_to_concept_id to the next visit pair
    df["discharge_to_previous"] = df.groupby("person_id")["discharge_to_concept_id"].shift(1)

    # Replace NaN values in the first visit pair with "Acute_care"
    df["discharge_to_previous"] = df["discharge_to_previous"].fillna("Acute_care")

    # Define the list of discharge_to_previous values to filter
    home_related_values = [
        "1: Home",
        "1: Home Health Agency",
        "1: Home Visit",
        "1: Outpatient Visit",
    ]

    # Filter rows with discharge_to_previous in the specified values
    at_home = (
        df[df["discharge_to_previous"].isin(home_related_values)]
        .groupby("person_id", as_index=False)
        .agg({"visit_start_date": "min"})
    )

    # Remove rows with discharge_to_previous in home_related_values from the main DataFrame
    df = df[~df["discharge_to_previous"].isin(home_related_values)]

    # Create separate DataFrames for each visit pair (1 through 5)
    visit_dataframes = {}
    for i in range(1, 6):
        visit_dataframes[f"visit_{i}"] = df[df["pair_number"] == i][
            [
                "person_id",
                "visit_start_date",
                "visit_source_concept_id",
                "visit_end_date",
                "discharge_to_concept_id",
                "discharge_to_previous",
            ]
        ]

    # Return the visit dataframes and the at_home dataframe
    return visit_dataframes, at_home

