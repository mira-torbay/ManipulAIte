from transformers import pipeline

# Load the fine-tuned model and tokenizer
classifier = pipeline("text-classification", model="./bias_classifier_model_v7", tokenizer="./bias_classifier_model_v7")

# Function to classify a single text
def classify_text(text):
    prediction = classifier(text)
    predicted_label = prediction[0]['label']  # Return raw label (LABEL_0, LABEL_1, LABEL_2)
    confidence = prediction[0]['score']
    return predicted_label, confidence

# Test with an example
if __name__ == "__main__":
    # Replace this with the text you want to classify
    test_text = "christian"
    # Get prediction
    label, confidence = classify_text(test_text)
    
    # Print the results
    print(f"Text: \"{test_text}\"")
    print(f"Predicted Bias Level: {label}, Confidence: {confidence:.2f}")
 