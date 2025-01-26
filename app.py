from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import torch
from transformers import BertTokenizer, BertForSequenceClassification, AutoTokenizer, AutoModelForSequenceClassification



# Load models and pipelines
pipe = pipeline("text-classification", model="unitary/toxic-bert")
generator = pipeline("text-generation", model="gpt2")
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve your HTML page


def toxicity_test(text): 
    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
    model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")

    

    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt")


    # Make a prediction
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # Extract the toxicity score (assuming a single output for toxicity)
    toxicity_score = logits[0][0].item()  # This should directly give a score between 0 and 1

    # Normalize the toxicity score to be between 0.00 and 1.00
    min_score = -7.5
    max_score = 4.5
    normalized_toxicity_score = (toxicity_score - min_score) / (max_score - min_score)

    # Ensure the score is within the range [0.00, 1.00]
    normalized_toxicity_score = max(0.0, min(1.0, normalized_toxicity_score))

    return normalized_toxicity_score

def logic_test(text): 
    
    # Initialize the zero-shot-classification pipeline with the specified model
    classifier = pipeline('zero-shot-classification', model='FacebookAI/roberta-large-mnli')


    # Define the candidate labels
    candidate_labels = ['Entailment', 'Neutral', 'Contradiction']

    # Perform classification
    result = classifier(text, candidate_labels)

    # Display the result
    print(f"Sequence: {result['sequence']}")
    for label, score in zip(result['labels'], result['scores']):
        print(f"{label}: {score:.4f}")

    # Find the label with the highest score
    scores = result['scores']
    labels = result['labels']
    
    
    return {"Contradiction": scores[labels.index("Contradiction")], "Entailment": scores[labels.index("Entailment")]}


@app.route('/assess', methods=['GET'])
def assess():
    user_input = request.args["msg"]

    # Generate text
    generated_text = generator(user_input, max_length=len(user_input), num_return_sequences=1)[0]['generated_text']

    # Analyze emotion
    emotion = emotion_analyzer(generated_text)
    
    # Combine results
    response = emotion

    toxicity = toxicity_test(generated_text)

    logic_val = logic_test(generated_text)
    
    return jsonify([response, toxicity, logic_val])

@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
