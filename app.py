from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from transformers import BertTokenizer, BertForSequenceClassification

# Load models and pipelines
pipe = pipeline("text-classification", model="unitary/toxic-bert")
generator = pipeline("text-generation", model="gpt2")
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def personality_detection(text):
    tokenizer = BertTokenizer.from_pretrained("Minej/bert-base-personality")
    model = BertForSequenceClassification.from_pretrained("Minej/bert-base-personality")

    inputs = tokenizer(text, truncation=True, padding=True, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.squeeze().detach().numpy()

    label_names = ['Extroversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']
    result = {label_names[i]: predictions[i] for i in range(len(label_names))}

    return result


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve your HTML page

@app.route('/assess', methods=['GET'])
def assess():
    user_input = request.args["msg"]

    # Generate text
    generated_text = generator(user_input, max_length=len(user_input), num_return_sequences=1)[0]['generated_text']

    # Analyze emotion
    emotion = emotion_analyzer(generated_text)

    # Personality detection
    personality = personality_detection(user_input)

    # Combine results
    response = {
        "generated_text": generated_text,
        "emotion": emotion,
        "personality": personality
    }



    # Dummy response (replace this with your actual model logic)
    '''if "propaganda" in user_input.lower():
        prediction = "High likelihood of propaganda"
    elif "neutral" in user_input.lower():
        prediction = "Likely neutral content"
    else:
        prediction = "Content not classified"
'''
    prediction = "ealjkesrlkweajrlke jarlkejrlkejarlkejarlkeajrleskjrlksd"
    return jsonify({"prediction": prediction})

@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
