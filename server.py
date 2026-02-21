from flask import Flask,request,jsonify,render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("carmodel.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Convert types
        data["year"] = int(data["year"])
        data["mileage"] = int(data["mileage"])
        data["tax"] = int(data["tax"])
        data["mpg"] = float(data["mpg"])
        data["engineSize"] = float(data["engineSize"])

        df = pd.DataFrame([data])
        df.columns = df.columns.str.lower()

        prediction = model.predict(df)[0]

        return jsonify({"prediction": round(float(prediction), 2)})

    except Exception as e:
        return jsonify({"error": str(e)})




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)