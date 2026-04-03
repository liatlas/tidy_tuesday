import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_data() -> pd.DataFrame:
    df = pd.read_csv("../data/ocean_temperature.csv")
    return df


def clean_data(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    df["date"] = pd.to_datetime(df["date"])

    return df


def draw_mom_graph(input_df: pd.DataFrame, year: int, output_name: str):
    df = input_df.copy()
    palette = sns.color_palette("mako_r", 7)

    plt.figure(figsize=(24, 6))
    sns.lineplot(
        data=df[df["date"].dt.year == year],
        x="date",
        y="mean_temperature_degree_c",
        hue="sensor_depth_at_low_tide_m",
        palette=palette,
    )
    plt.ylim(0, 20)
    plt.xticks(rotation=90)
    plt.savefig(f"../outputs/{output_name}.png")


def draw_yoy_graph(input_df: pd.DataFrame):
    df = input_df.copy()

    df = df.groupby("date")["mean_temperature_degree_c"].agg(mean="mean").reset_index()
    df["year"] = df["date"].dt.year
    df["day"] = df["date"].dt.dayofyear

    plt.figure(figsize=(24, 6))
    sns.lineplot(df, x="day", y="mean", hue="year")

    plt.xticks(
        [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335],
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
    )
    plt.savefig("../outputs/yay_graph.png")


def draw_heatmap(input_df):
    df = input_df.copy()
    corrs = df.corr()

    sns.heatmap(corrs, annot=True, cmap="coolwarm")
    plt.title("Correlation Map of Columns")
    plt.savefig("../outputs/heatmap.png")


def main():
    df = load_data()
    df = clean_data(df)

    draw_mom_graph(df, 2018, "mom_2018")
    draw_mom_graph(df, 2024, "mom_2024")
    draw_yoy_graph(df)
    draw_heatmap(df)

    print("Graphs done generating")


if __name__ == "__main__":
    main()
