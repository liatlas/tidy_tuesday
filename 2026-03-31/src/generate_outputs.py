import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data() -> pd.DataFrame:
    df = pd.read_csv("../data/ocean_temperature.csv")
    return df
    
def clean_data():
    pass

def draw_mom_graph(input_df):
    pass


def draw_yoy_graph(input_df):
    pass


def draw_heatmap(input_df):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
