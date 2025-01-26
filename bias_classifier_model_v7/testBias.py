from transformers import pipeline

# Load the fine-tuned model and tokenizer
classifier = pipeline("text-classification", model="./bias_classifier_model_v7", tokenizer="./bias_classifier_model_v7")

# Map raw labels to integers
label_mapping = {
    "LABEL_0": 0, #No bias
    "LABEL_1": 0.5, #Some bias
    "LABEL_2": 1 #Strong bias
}

# Function to classify a single text
def classify_text(text):
    prediction = classifier(text)
    raw_label = prediction[0]['label']  # Return raw label (0,1,or 2) 
    confidence = prediction[0]['score']
    # Map the raw label to an integer
    predicted_label = label_mapping[raw_label]
    return [predicted_label, round(confidence, 2)]

print(classify_text("hate"))