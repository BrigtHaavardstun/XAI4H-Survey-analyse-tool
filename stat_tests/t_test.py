import numpy as np
from scipy import stats
from numpy.random import seed
from numpy.random import randn
from numpy.random import normal
from scipy.stats import ttest_ind
import pandas as pd


def preform_t_test(sample_group_one, sample_group_two):
    t_stat, p_value = ttest_ind(sample_group_one, sample_group_two)
    return t_stat, p_value


def load_sample_groups_old():
    df = pd.read_csv("csv_files/aggregated_file.csv", sep=",")
    S_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "S"])
    R_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "R"])

    return [S_scores, R_scores]


def load_sample_groups_new():
    df = pd.read_csv("csv_files/aggregated_file.csv", sep=",")
    A_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "A"])
    B_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "B"])
    C_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "C"])
    return [A_scores, B_scores, C_scores]


def main():
    # A and B
    S, R = load_sample_groups_old()
    print(f"R and S gives ", preform_t_test(
        sample_group_one=R, sample_group_two=S))


if __name__ == "__main__":
    main()
