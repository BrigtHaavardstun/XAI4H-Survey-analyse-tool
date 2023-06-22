import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def run():
    # load data file
    df = pd.read_csv(
        "https://reneshbedre.github.io/assets/posts/anova/onewayanova.txt", sep="\t")
    # reshape the d dataframe suitable for statsmodels package
    print(df)
    df_melt = pd.melt(df.reset_index(), id_vars=[
        'index'], value_vars=['A', 'B', 'C', 'D'])
    print(df_melt)
    # replace column names
    df_melt.columns = ['index', 'treatments', 'value']

    # generate a boxplot to see the data distribution by treatments. Using boxplot, we can
    # easily detect the differences between different treatments
    ax = sns.boxplot(x='treatments', y='value', data=df_melt, color='#99c2a2')
    ax = sns.swarmplot(x="treatments", y="value",
                       data=df_melt, color='#7d0013')
    plt.show()


if __name__ == '__main__':
    run()
