from enum import Enum
import matplotlib.pyplot as plt
import matplotlib.patches as pltpatches
import seaborn as sns
import pandas as pd


class Graph(Enum):
    NO_GRAPH = "none"
    SCATTER = "scatter"
    AVERAGE_WEIGHT_BY_HEIGHT = "average_weight_by_height"
    KDE_PLOT = "kde_plot"


# @todo this class only work for the weight and height distribution, it should be improved to be generic or moved.
class DistributionVisualizer:
    """
    Provides different plotting methods for the synthetic data.
    """

    @staticmethod
    def plot_distributions(dataframes, graph_type: Graph):
        plt.figure(figsize=(8, 6))
        sns.set_theme()
        sns.set_style("whitegrid")

        if graph_type == Graph.SCATTER:
            DistributionVisualizer._plot_scatter(dataframes)
        elif graph_type == Graph.AVERAGE_WEIGHT_BY_HEIGHT:
            DistributionVisualizer._plot_average_weight_by_height(dataframes)
        elif graph_type == Graph.KDE_PLOT:
            DistributionVisualizer._plot_kde(dataframes)

        plt.grid(True)
        plt.show()

    @staticmethod
    def _plot_scatter(dataframes):
        sns.scatterplot(
            data=pd.concat(dataframes),
            x='height', y='weight',
            hue='group', style='group', palette='Set1', s=75
        )
        plt.title('Synthetic data of Height/Weight Distributions')
        plt.xlabel('Weight (kg)')
        plt.ylabel('Height (cm)')
        plt.legend(title="Group")

    @staticmethod
    def _plot_average_weight_by_height(dataframes):
        df_all = pd.concat(dataframes)
        df_all['height_rounded'] = df_all['height'].round(0)
        avg_weight_by_height = (
            df_all.groupby(['height_rounded', 'group'])['weight']
            .mean()
            .reset_index()
        )
        sns.lineplot(
            data=avg_weight_by_height,
            x='height_rounded',
            y='weight',
            hue='group',
            marker='o'
        )
        plt.xlabel('Height (cm)')
        plt.ylabel('Average Weight (kg)')
        plt.title("Synthetic Avg Weight/Height")

    @staticmethod
    def _plot_kde(dataframes):
        color_maps = ["Blues", "Greens", "Oranges", "Purples", "RdPu"]
        handles = []
        for idx, df in enumerate(dataframes):
            cmap = color_maps[idx % len(color_maps)]
            group_label = df['group'].iloc[0]
            color = plt.get_cmap(cmap)(0.95)
            legend = pltpatches.Patch(color=color, label=group_label)
            handles.append(legend)

            sns.kdeplot(
                x=df['height'],
                y=df['weight'],
                label=group_label,
                legend=False,
                fill=True,
                cmap=cmap,
                thresh=0.05,
            )
        plt.xlabel('Height (cm)')
        plt.ylabel('Weight (kg)')
        plt.title("2D KDE of Height vs Weight")
        plt.legend(handles=handles, title='Group', loc='upper left')
