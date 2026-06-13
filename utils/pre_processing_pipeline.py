from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import numpy as np
def pre_processing_pipeline(X_train_data,X_test_data,y_train_data,y_test_data):
    print("X train data info")
    print(X_train_data.info())
    numeric_features = X_train_data.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = X_train_data.select_dtypes(include=['object', 'category']).columns.tolist()

    numeric_features_pipeline = Pipeline([('imputer',SimpleImputer(strategy='mean')),('scaler',StandardScaler())])
    categorical_features_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown="ignore"))
    ])
    preprocessor = ColumnTransformer(
        transformers=[
        ('encoder',categorical_features_pipeline,categorical_features),
        ('scaler',numeric_features_pipeline,numeric_features)
    ])
    final_model_pipeline = Pipeline([
    ('preprocessing', preprocessor),
    ('classifier', RandomForestClassifier(
        n_estimators=150,     # More trees to smooth out variance
        max_depth=8,
        class_weight='balanced',# Stops the trees from over-memorizing rows
        min_samples_leaf=4,   # Requires at least 4 similar matches to make a prediction rule
        random_state=42)) # Or any model you want to use!
    ])
    final_model_pipeline.fit(X_train_data,y_train_data)
    y_pred_data = final_model_pipeline.predict(X_test_data)
    accuracy = accuracy_score(y_test_data, y_pred_data)
    print("Classification  Report")
    print(classification_report(y_test_data,y_pred_data))

    print(f"Direct Accuracy Score (Actual vs Predicted): {accuracy:.4f}")







