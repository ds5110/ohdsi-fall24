home_id = {
    0: "1: Home",
    38004519: "1: Home Health Agency",
    581476: "1: Home Visit",
    9202: "1: Outpatient Visit",
}
inpatient_rehab_id = {
    8920: "2: Comprehensive Inpatient Rehabilitation Facility",
    38004285: "2: Rehabilitation Hospital",
}
skilled_nursing_id = {
    8676: "3: Nursing Facility",
    8863: "3: Skilled Nursing Facility",
    38004277: "3: Long Term Care Hospital",
}
acute_care_id = {
    8717: "4: Inpatient Hospital",
    32276: "4: Critical Access Hospital",
    32254: "4: Hospital-Swing Beds",
}
other_id = {
    8546: "5: Hospice",
    8951: "5: Intermediate Mental Care Facility",
    38004284: "5: Psychiatric Hospital",
    38003619: "5: Prison/Correctional Facility",
}
total_id = {
    **home_id,
    **inpatient_rehab_id,
    **skilled_nursing_id,
    **acute_care_id,
    **other_id,
}
group_mapping = {
    **{key: "Home" for key in home_id},
    **{key: "Inpatient Rehab" for key in inpatient_rehab_id},
    **{key: "Skilled Nursing" for key in skilled_nursing_id},
    **{key: "Acute Care" for key in acute_care_id},
    **{key: "Other" for key in other_id}
}