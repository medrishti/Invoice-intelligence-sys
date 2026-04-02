from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,classification_report,make_scorer,f1_score

def train_random_forest(X_train_scaled,y_train):
    rf=RandomForestClassifier(
        random_state=42,
        n_jobs=-1
    )

    param_grid={
    'n_estimators':[100,200,300],
    'max_depth':[None,4,5,6],
    'min_samples_split':[2,3,5],
    'min_samples_leaf':[1,2,3],
    'criterion':['gini','entropy']
   }

    scorer=make_scorer(f1_score)
    gridSearch=GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        scoring=scorer,
        cv=5,
        verbose=2,
        n_jobs=-1
    )
    gridSearch.fit(X_train_scaled,y_train)

    return gridSearch
def evaluate_classifier(model,X_test,y_test,model_name):
    preds=model.predict(X_test)

    accuracy=accuracy_score(y_test,preds)
    report=classification_report(y_test,preds)

    print(f"Model: {model_name}")
    print(f"Accuracy: {accuracy:.4f}")
    print(report)

    


   
