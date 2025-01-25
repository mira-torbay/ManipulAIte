from flask import Flask, request, jsonify
from transformers import pipeline
from transformers import BertTokenizer, BertForSequenceClassification

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

if __name__ == '__main__':
    app.run(debug=True)
