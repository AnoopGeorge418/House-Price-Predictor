from flask import Flask, request, render_template
import pickle as pkl
import numpy as np

application = Flask(__name__)
app = application

# Load model and scaler pickle files
model = pkl.load(open('./model/Model.pkl', 'rb'))
scaler = pkl.load(open('./model/Scaler.pkl', 'rb'))

@app.route("/", methods=['GET', 'POST'])
def predict_data():
    if request.method == 'POST':
        try:
            # Retrieve and process the input value
            Number_Of_Private_Rooms = float(request.form.get('Number_Of_Private_Rooms'))
            
            # Transform input and make a prediction
            new_scaled_data = scaler.transform(np.array([[Number_Of_Private_Rooms]]))
            result = model.predict(new_scaled_data)
            
            # Multiply the prediction result by 1000 to scale it
            scaled_result = result[0] * 1000
            
            # Format the prediction as a price value with 2 decimal places and thousands separator
            formatted_result = f"${scaled_result:,.2f}"

            return render_template('home.html', results=formatted_result)
        
        except Exception as e:
            print(f"Error: {e}")
            return render_template('home.html', results='Error occurred during prediction.')
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)