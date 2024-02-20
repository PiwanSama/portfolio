from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved benchmark model and the scaler
model = pickle.load(open('final_benchmark_model.pkl', 'rb'))

# Define the home route
@app.route('/')
def home():
    # Render the home page with form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch the form inputs
        purchase_frequency = float(request.form['PURCHASES_FREQUENCY'])
        purchases_trx = float(request.form['PURCHASES_TRX'])
        purchases = float(request.form['PURCHASES'])
        cash_advance = float(request.form['CASH_ADVANCE'])
        cash_advance_frequency = float(request.form['CASH_ADVANCE_FREQUENCY'])
        cash_advance_trx = float(request.form['CASH_ADVANCE_TRX'])

        inputs = [purchase_frequency, purchases_trx, purchases,
                      cash_advance, cash_advance_frequency, cash_advance_trx]

        input_array = np.array(inputs)
        inputs_values = input_array.reshape(1,-1)
            
        result = model.predict(inputs_values)

       # Generate the results that will be displayed to the user
        if int(result)== 0:
            predicted_class ='Gold Tier Customer'
            color='darkorange'
        else:
            predicted_class ='Silver Tier Customer'
            color='gainsboro'

    except ValueError as e:
        print(f"Caught a ValueError: {e}")
    
    # Render the prediction result page
    return render_template('predict.html', prediction=predicted_class, color_signal=color)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
