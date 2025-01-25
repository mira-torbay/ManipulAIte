from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve your HTML page

@app.route('/assess', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data.get('input', '')

    # Dummy response (replace this with your actual model logic)
    if "propaganda" in user_input.lower():
        prediction = "High likelihood of propaganda"
    elif "neutral" in user_input.lower():
        prediction = "Likely neutral content"
    else:
        prediction = "Content not classified"

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
