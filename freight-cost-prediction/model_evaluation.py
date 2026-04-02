from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split    
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error

def train_LinearRegression(X_train,y_train):
    model=LinearRegression()
    model.fit(X_train,y_train)
    return model

def train_decision_tree(X_train,y_train,max_depth=4):
    model=DecisionTreeRegressor(max_depth=max_depth)
    model.fit(X_train,y_train)
    return model

def train_random_forest(X_train,y_train,n_estimators=100,max_depth=4):
    model=RandomForestRegressor(n_estimators=n_estimators,max_depth=max_depth)
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_test,y_test,model_name):
    y_pred=model.predict(X_test)
    mse=mean_squared_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)
    mae=mean_absolute_error(y_test,y_pred)
    print(f'{model_name} - MSE: {mse}, R2: {r2}, MAE: {mae}')
    return{
        'model_name': model_name,
        'mse': mse,
        'r2': r2,
        'mae': mae
    }
