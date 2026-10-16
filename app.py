# Google Map Arrival time prediction

# linear regression
# knn
# decision tree
# random forest






# print(main(2,12,0,0,0,0,35))
# print(main(150,9,0,0,1,1,60))

    

    


def main(distance,hour,is_weekend,is_holiday,road,vehicle,avg_speed_kmh):
    import pandas as pd



    from sklearn.ensemble import RandomForestRegressor



    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import CountVectorizer

    from sklearn.metrics import mean_absolute_error

    df = pd.read_csv('dataset.csv')

    # data cleaning (removing null values, drop duplicates)
    df = df.dropna(how='any')
    df = df.drop_duplicates()

    # understanding data

    


    # feature engineering
    df['day'] = None
    for i in range(len(df)):
        if(df.loc[i,'day_of_week'] == 'Monday'):
            df.loc[i,'day'] = 0
        elif(df.loc[i,'day_of_week'] == 'Tuesday'):
            df.loc[i,'day'] = 1
        elif(df.loc[i,'day_of_week'] == 'Wednesday'):
            df.loc[i,'day'] = 2
        elif(df.loc[i,'day_of_week'] == 'Thursday'):
            df.loc[i,'day'] = 3
        elif(df.loc[i,'day_of_week'] == 'Friday'):
            df.loc[i,'day'] = 4
        elif(df.loc[i,'day_of_week'] == 'Saturday'):
            df.loc[i,'day'] = 5
        elif(df.loc[i,'day_of_week'] == 'Sunday'):
            df.loc[i,'day'] = 6




    df['road'] = None
    for i in range(len(df)):
        if(df.loc[i,'road_type'] == "Urban"):
            df.loc[i,'road'] = 0
        elif(df.loc[i,'road_type'] == "Highway"):
            df.loc[i,'road'] = 1
        else:
            df.loc[i,'road'] = None


    df['vehicle'] = None
    for i in range(len(df)):
        if(df.loc[i,'vehicle_type'] == "Bike" or df.loc[i,'vehicle_type'] == "Motorcycle"):
            df.loc[i,'vehicle'] = 0
        elif(df.loc[i,'vehicle_type'] == "Car" or df.loc[i,'vehicle_type'] == "SUV"):
            df.loc[i,'vehicle'] = 1
        else:
            df.loc[i,'vehicle'] = None



    df = df.dropna(how='any')
    df = df.drop_duplicates()
            
    X = df[['distance_km','hour','is_weekend','is_holiday','road','vehicle','avg_speed_kmph']]
    y = df['actual_travel_time_min']

    xtrain,xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,shuffle=True)




    model = RandomForestRegressor(n_estimators=1500)
    model.fit(xtrain,ytrain)

    out = model.predict(xtest)

    MAE = mean_absolute_error(y_pred=out,y_true=ytest)

    time = model.predict([[distance,hour,is_weekend,is_holiday,road,vehicle,avg_speed_kmh]])
    return time
    












import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/submit",methods = ['POST'])
def submit():
    # X = df[['distance_km','hour','is_weekend','is_holiday','road','vehicle','avg_speed_kmph']]

    # is_weekend = request.form.get('is_weekend')    
    
    # print(is_weekend)
    
    
    distance = float(request.form.get('distance'))
    hour = int(request.form.get('hour'))
    is_weekend = int(request.form.get('is_weekend'))
    is_holiday = int(request.form.get('is_holiday'))
    road = int(request.form.get('road'))
    vehicle = int(request.form.get('vehicle'))
    avg_speed_kmh = int(request.form.get('avg_speed_kmph'))
    
    # time = str(main(distance,hour,is_weekend,is_holiday,road,vehicle,avg_speed_kmh) + "Minutes")
    time = main(distance,hour,is_weekend,is_holiday,road,vehicle,avg_speed_kmh)

    
    return render_template('index.html',time = time)
    
    
    

    


if __name__ == "__main__":
    app.run(debug=True)





