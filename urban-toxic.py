# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch

# # Load the tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
# model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")

# # Input text to classify
# text = "I hate you"

# # Tokenize the input text
# inputs = tokenizer(text, return_tensors="pt")

# # Make a prediction
# with torch.no_grad():
#     outputs = model(**inputs)
#     logits = outputs.logits
#     predicted_class = logits.argmax().item()

# # Map the predicted class to its label
# labels = ["non-toxic", "toxic"]
# prediction = labels[predicted_class]
# print(f"Prediction: {prediction}")


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")

# Input text to classify
text = "I want world peace"

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

print(f"Toxicity level (0.00 to 1.00): {normalized_toxicity_score}")

