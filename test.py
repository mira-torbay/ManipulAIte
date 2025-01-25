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