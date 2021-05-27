import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns


def creating_folder(Anscombe_Quarter_Exercise: str) -> None:
    """
    Creating a new folder or showing information about existing folder

    :param Anscombe_Quarter_Exercise:
    :return: None
    """
    if os.path.exists(Anscombe_Quarter_Exercise):
        print("File exist")
    else:
        os.makedirs(Anscombe_Quarter_Exercise)

    print("Created folder named Anscombe_Quarter_Exercise")


def anscombe_dataset_download() -> pd.DataFrame:
    """
    Download dataset from Anscombe Quarter

    :param Anscombe DataFrame
    :return: anscombe_df
    """
    anscombe_df = sns.load_dataset("anscombe")
    print(anscombe_df)
    return anscombe_df


def anscombe_dataset_plots(anscombe_df: pd.DataFrame) -> print:
    """
    Function which create 4 plots in one JPG

    :param anscombe_df:
    :return: Plot
    """
    sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombe_df,
               col_wrap=2, palette="muted", height=4)
    plt.gcf().suptitle("Anscombe's Quartet", x=0.5, y=1)
    plt.savefig('Ascombe_Quarter_Exercise/anscombe_plot.jpg')
    plt.show()
    print("Created")


def anscombe_dataset_calculations(anscombe_df: pd.DataFrame) -> print:
    """
    Function that calculate mean, variance, correlation and standard deviation

    :param anscombe_df:
    :return: X / Y: mean, std, var AND correalation beetween X Y
    """
    grouped = anscombe_df.groupby('dataset')
    scores_into_csv_file = pd.DataFrame(columns=['mean_x', 'std_x', 'mean_y', 'std_y', 'correlation', 'var_x', 'var_y'])
    for key in grouped.groups.keys():
        scores_into_csv_file.loc[key] = (
            grouped.mean().loc[key]['x'],
            np.round(grouped.mean().loc[key]['y'], 2),
            np.round(grouped.std().loc[key]['x'], 5),
            np.round(grouped.std().loc[key]['y'], 2),
            np.round(grouped.corr().loc[(key, 'x')]['y'], 3),
            np.round(grouped.var().loc[key]['x'], 5),
            np.round(grouped.var().loc[key]['y'], 2),
        )

    scores_into_csv_file.to_csv('Anscombe_Quarter_Exercise/ascombe_calculations.csv')
    print("Created CSV file named Anscombe_Calculations")

def main():
    """
    Launching the program
    :return:
    """
    creating_folder("Anscombe_Quarter_Exercise")
    anscombe_df = anscombe_dataset_download()
    anscombe_dataset_plots(anscombe_df)
    anscombe_dataset_calculations(anscombe_df)

if __name__ == "__main__":
    main()