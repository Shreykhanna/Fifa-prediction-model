def filter_fifa_dataset(phik_matrix,dataFrame):
    target_variable = 'outcome'
    min_correlation_threshold = 0.10
    target_correlations = phik_matrix[target_variable].abs()
    important_features = target_correlations[target_correlations >= min_correlation_threshold].index.tolist()
    filtered_dataframe_by_target = dataFrame[important_features]

    return filtered_dataframe_by_target

