from phik.report import plot_correlation_matrix
from filter_fifa_dataset import filter_fifa_dataset
from matplotlib import pyplot as plt
import numpy as np
def phik_matrix_calculation(fifa_dataset):
    numeric_features = fifa_dataset.select_dtypes(include=[np.number]).columns.tolist()
    phik_matrix = fifa_dataset.phik_matrix(interval_cols = numeric_features)
    filtered_fifa_data = filter_fifa_dataset(phik_matrix, fifa_dataset)
    filtered_sample = filtered_fifa_data.sample(n=500, random_state=42)
    numeric_feature_filtered_sample = filtered_sample.select_dtypes(include=[np.number]).columns.tolist()
    phik_matrix = filtered_sample.phik_matrix(interval_cols=numeric_feature_filtered_sample)
    plot_correlation_matrix(phik_matrix.values, vmax=1.0, vmin=-1.0, x_labels=phik_matrix.columns,
                            y_labels=phik_matrix.index, color_map='viridis', figsize=(20, 18))
    plt.xticks(rotation=90, fontsize=10)
    plt.yticks(fontsize=10)
    plt.subplots_adjust(bottom=0.25, left=0.25)
    plt.show()

    return filtered_fifa_data

