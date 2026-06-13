from sklearn.model_selection import train_test_split

def _train_test_split(filtered_fifa_data):
    X = filtered_fifa_data.drop(columns=['outcome'])
    y = filtered_fifa_data['outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test