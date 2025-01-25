from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load the pipeline
pipe = pipeline("text-classification", model="FacebookAI/roberta-large-mnli")

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("FacebookAI/roberta-large-mnli")
model = AutoModelForSequenceClassification.from_pretrained("FacebookAI/roberta-large-mnli")

# Load zero-shot classification pipeline
classifier = pipeline('zero-shot-classification', model='FacebookAI/roberta-large-mnli')

sequence_to_classify = "one day I will see the world"
candidate_labels = ['travel', 'cooking', 'dancing']
result = classifier(sequence_to_classify, candidate_labels)

print(result)