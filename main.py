

## Question 1#
def proportion_of_education(data):
    total_children = len(data)

    # Count the number of children with each education level
    education_counts = {
        "less than high school": 0,
        "high school": 0,
        "more than high school but not college": 0,
        "college": 0
    }

    for row in data:
        education_level = row["education"]
        if education_level == "less than high school":
            education_counts["less than high school"] += 1
        elif education_level == "high school":
            education_counts["high school"] += 1
        elif education_level == "more than high school but not college":
            education_counts["more than high school but not college"] += 1
        elif education_level == "college":
            education_counts["college"] += 1

    # Calculate the proportions
    proportions = {
        "less than high school": education_counts["less than high school"] / total_children,
        "high school": education_counts["high school"] / total_children,
        "more than high school but not college": education_counts["more than high school but not college"] / total_children,
        "college": education_counts["college"] / total_children
    }

    return proportions


## Question 2

def average_influenza_doses(data):
    # Initialize variables to keep track of the sum and count for each group
    breastmilk_sum = 0
    breastmilk_count = 0
    no_breastmilk_sum = 0
    no_breastmilk_count = 0

    # Iterate through the dataset and calculate the sum and count for each group
    for row in data:
        received_breastmilk = row["received_breastmilk"]
        influenza_doses = row["influenza_doses"]

        if received_breastmilk == "yes":
            breastmilk_sum += influenza_doses
            breastmilk_count += 1
        elif received_breastmilk == "no":
            no_breastmilk_sum += influenza_doses
            no_breastmilk_count += 1

    # Calculate the average for each group, avoiding division by zero
    average_breastmilk = breastmilk_sum / breastmilk_count if breastmilk_count != 0 else 0
    average_no_breastmilk = no_breastmilk_sum / no_breastmilk_count if no_breastmilk_count != 0 else 0

    return (average_breastmilk, average_no_breastmilk)


## Question 3

def chickenpox_by_sex(data):
    # Initialize variables to keep track of counts for each group
    vaccinated_and_contracted = {"male": 0, "female": 0}
    vaccinated_and_not_contracted = {"male": 0, "female": 0}

    # Iterate through the dataset and calculate the counts for each group
    for row in data:
        sex = row["sex"]
        varicella_doses = row["varicella_doses"]
        has_chickenpox = row["has_chickenpox"]

        if varicella_doses >= 1:
            if has_chickenpox == "yes":
                vaccinated_and_contracted[sex] += 1
            elif has_chickenpox == "no":
                vaccinated_and_not_contracted[sex] += 1

    # Calculate the ratio for each sex, avoiding division by zero
    ratio_by_sex = {
        "male": vaccinated_and_contracted["male"] / vaccinated_and_not_contracted["male"] if vaccinated_and_not_contracted["male"] != 0 else 0,
        "female": vaccinated_and_contracted["female"] / vaccinated_and_not_contracted["female"] if vaccinated_and_not_contracted["female"] != 0 else 0
    }

    return ratio_by_sex

## Question 4

import scipy.stats as stats
import numpy as np
import pandas as pd


def corr_chickenpox():
    # This is just an example dataframe, replace it with your actual dataset
    df = pd.DataFrame({
        "had_chickenpox_column": np.random.randint(1, 3, size=(100)),
        "num_chickenpox_vaccine_column": np.random.randint(0, 6, size=(100))
    })

    # Here is the actual code to calculate the correlation and p-value
    corr, pval = stats.pearsonr(df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"])

    return corr
# Example usage with your actual dataset
# Assuming you have loaded your data into a variable called "data"
result = corr_chickenpox(data)
print(result)
