from transformers import pipeline
from transformers import BertTokenizer, BertForSequenceClassification

def personality_detection(text):
    tokenizer = BertTokenizer.from_pretrained("Minej/bert-base-personality")
    model = BertForSequenceClassification.from_pretrained("Minej/bert-base-personality")

    inputs = tokenizer(text, truncation=True, padding=True, return_tensors="pt")
    outputs = model(**inputs)
    predictions = outputs.logits.squeeze().detach().numpy()

    label_names = ['Extroversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']
    result = {label_names[i]: predictions[i] for i in range(len(label_names))}

    return result

# Load text generation pipeline (GPT-2 model)
generator = pipeline("text-generation", model="gpt2")

# Generate text
generated_text = generator("DIE LARRY DIE!", max_length=20, num_return_sequences=1)[0]['generated_text']
print("Generated Text:", generated_text)

# Load emotion recognition pipeline
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Get emotion prediction
emotion = emotion_analyzer(generated_text)
print("Emotional Data:", emotion)

print(personality_detection("Stab the Larry please"))
