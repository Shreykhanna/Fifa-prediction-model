def filter_fifa_dataset(phik_matrix,dataFrame):
    target_variable = 'outcome'
    min_correlation_threshold = 0.10

    target_correlations = phik_matrix[target_variable].abs()
    print("Target correlatons")
    print(target_correlations)
    important_features = target_correlations[target_correlations >= min_correlation_threshold].index.tolist()
    filtered_dataFrame_by_target = dataFrame[important_features]
    print(f"Kept {len(important_features)} features out of {len(phik_matrix.columns)}.")
    print("Features kept:", important_features)
    return filtered_dataFrame_by_target

