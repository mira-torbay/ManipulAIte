from transformers import pipeline

# Initialize the zero-shot-classification pipeline with the specified model
classifier = pipeline('zero-shot-classification', model='FacebookAI/roberta-large-mnli')

# Define the sequence to classify
sequence_to_classify = "Your input text here"

# Define the candidate labels
candidate_labels = ['Entailment', 'Neutral', 'Contradiction']

# Perform classification
result = classifier(sequence_to_classify, candidate_labels)

# Display the result
print(result["sequence"])
for i in range(len(candidate_labels)):
    print(f"{candidate_labels[i]}: {result['scores'][i]}")

