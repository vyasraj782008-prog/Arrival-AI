# Google Map Arrival time prediction

# linear regression
# knn
# decision tree
# random forest






# print(main(2,12,0,0,0,0,35))
# print(main(150,9,0,0,1,1,60))

    

    
















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
    try:

        distance = float(request.form.get('distance'))
        hour = int(request.form.get('hour'))
        is_weekend = int(request.form.get('is_weekend'))
        is_holiday = int(request.form.get('is_holiday'))
        road = int(request.form.get('road'))
        vehicle = int(request.form.get('vehicle'))
        avg_speed_kmh = int(request.form.get('avg_speed_kmph'))
    
        # time = str(main(distance,hour,is_weekend,is_holiday,road,vehicle,avg_speed_kmh) + "Minutes")
        model = joblib.load('model.pkl')
    
        time = model.predict([[distance,hour,is_weekend,is_holiday,road,vehicle,avg_speed_kmh]])
        time = time[0]

        return render_template('index.html',time = time)
    

    except Exception as e:
    import os
    return str(("Model file exists:", os.path.exists("model.pkl")) + ("Model size:", os.path.getsize("model.pkl"), "bytes"))
    
        
    


if __name__ == "__main__":
    app.run(debug=True)





