import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns


def HiHeyHello() -> None:
    """
    Creating welcome message
    """

    print(
        "Welcome into Anscombe Quarter program. Here you will see basic calculations and plots for Anscombe Quarter. Enjoy!\n")


def creating_folder(Anscombe_Quarter_Exercise: str) -> None:
    """
    Creating a new folder or showing information about existing folder

    :param Anscombe_Quarter_Exercise:
    :return: None
    """
    if os.path.exists(Anscombe_Quarter_Exercise):
        print("File exist\n")
    else:
        os.makedirs(Anscombe_Quarter_Exercise)

    print("Created folder named Anscombe_Quarter_Exercise\n")


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
    plt.savefig('Anscombe_Quarter_Exercise/anscombe_plot.jpg')
    plt.show()
    print("Created\n")


def anscombe_dataset_calculations(anscombe_df: pd.DataFrame) -> print:
    """
    Function that calculate mean, variance, correlation and standard deviation

    :param anscombe_df:
    :return: X / Y: mean, std, var and correalation beetween X Y
       """
    mean_x = round(anscombe_df.mean().loc['x'])
    mean_y = round(anscombe_df.mean().loc['y'])
    std_x = round(anscombe_df.std().loc['x'])
    std_y = round(anscombe_df.std().loc['y'])
    var_x = round(anscombe_df.var().loc['x'])
    var_y = round(anscombe_df.var().loc['y'])
    correlation = round(anscombe_df.corr().loc['x']['y'])

    scores_into_csv_file = pd.DataFrame(np.array([mean_x, mean_y, std_x, std_y, var_x, var_y, correlation]))

    scores_into_csv_file.to_csv('Anscombe_Quarter_Exercise/anscombe_calculations.csv')
    print("Created CSV file named Anscombe_Calculations\n")


def main():
    """
    Launching the program
    :return:
    """
    HiHeyHello()
    creating_folder("Anscombe_Quarter_Exercise")
    anscombe_df = anscombe_dataset_download()
    anscombe_dataset_plots(anscombe_df)
    anscombe_dataset_calculations(anscombe_df)


if __name__ == "__main__":
    main()