
from transformers import pipeline

# Initialize the zero-shot-classification pipeline with the specified model
classifier = pipeline('zero-shot-classification', model='FacebookAI/roberta-large-mnli')

# Define the sequence to classify
sequence_to_classify = "the tree in in the sky and planted on the ground"

# Define the candidate labels
candidate_labels = ['Entailment', 'Neutral', 'Contradiction']

# Perform classification
result = classifier(sequence_to_classify, candidate_labels)

# Display the result
print(f"Sequence: {result['sequence']}")
for label, score in zip(result['labels'], result['scores']):
    print(f"{label}: {score:.4f}")

# Find the label with the highest score
max_score = max(result['scores'])
max_label = result['labels'][result['scores'].index(max_score)]

# Print the highest value and corresponding label
print(f"Highest value: {max_score:.4f}")
print(f"Label with highest value: {max_label}")
