from flask import Flask, request, jsonify
from transformers import pipeline
import torch
from transformers import BertTokenizer, BertForSequenceClassification, AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

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

@app.route('/assess', methods=['POST'])
def process_text():
    try:
        # Parse JSON input
        data = request.get_json()
        if 'text' not in data:
            return jsonify({"error": "No 'text' field provided"}), 400
        
        text = data['text']

        # Generate text
        generated_text = generator(text, max_length=283, num_return_sequences=1)[0]['generated_text']

        # Analyze emotion
        emotion = emotion_analyzer(generated_text)

        # Personality detection
        personality = personality_detection(text)

        # Combine results
        response = {
            "generated_text": generated_text,
            "emotion": emotion,
            "personality": personality
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

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
    max_score = max(result['scores'])
    max_label = result['labels'][result['scores'].index(max_score)]

    return {"Label": max_label, "Value": max_score}

if __name__ == '__main__':
    app.run(debug=True)
