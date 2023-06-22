from statsmodels.formula.api import ols
import statsmodels.api as sm
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def run():
    # load data file
    df = pd.read_csv("csv_files/aggregated_file.csv", sep=",")
    # reshape the d dataframe suitable for statsmodels package

    # generate a boxplot to see the data distribution by treatments. Using boxplot, we can
    # easily detect the differences between different treatments
    ax = sns.boxplot(x='treatment', y='score', data=df, color='#99c2a2')
    ax = sns.swarmplot(x="treatment", y="score", data=df, color='#7d0013')
    plt.show()

    # stats f_oneway functions takes the groups as input and returns ANOVA F and p value
    # Group by A,B and C
    print(list(df["treatment"]))
    print(list(df["score"]))
    """
    A_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "A"])
    B_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "B"])
    C_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "C"])
    """
    S_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "S"])
    R_scores = list([float(score) for (score, treatment) in zip(
        df["score"], df["treatment"]) if treatment == "R"])
    fvalue, pvalue = stats.f_oneway(S_scores, R_scores)
    print(fvalue, pvalue)
    # 17.492810457516338 2.639241146210922e-05

    # get ANOVA table as R like output

    # Ordinary Least Squares (OLS) model
    """
    model = ols('value ~ C(treatments)', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    anova_table
    """
