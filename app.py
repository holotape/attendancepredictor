from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ''
    attendance_values = [0]*10  # Default values
    if request.method == 'POST':
        years = np.array(range(1, 11)).reshape(-1, 1)
        attendance = np.array([int(x) for x in request.form.values()]).reshape(-1, 1)

        model = LinearRegression()
        model.fit(years, attendance)

        eleventh_year = np.array([11]).reshape(-1, 1)
        prediction = model.predict(eleventh_year)[0][0]
        attendance_values = list(request.form.values())

    return render_template('index.html', prediction=prediction, attendance_values=attendance_values)

if __name__ == '__main__':
    app.run(debug=True)
