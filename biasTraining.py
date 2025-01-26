
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments, DistilBertTokenizer
from datasets import Dataset



# Load the JSON file into a DataFrame
with open("merged_data.json", "r") as file:
    data = json.load(file)

# Convert JSON to a DataFrame
records = [
    {"id": article_id, "content": article_data["content"], "bias": article_data["bias"]}
    for article_id, article_data in data.items()
]
df = pd.DataFrame(records)

# Ensure labels are valid (0, 1, 2)
valid_labels = {0: 0, 1: 1, 2: 2}
df["bias"] = df["bias"].map(valid_labels)

# Drop rows with invalid or missing labels
df = df.dropna(subset=["bias", "content"])

# Shuffle and sample the dataset
random_sample2 = df.sample(n=200, random_state=84)

# Split into train, validation, and test sets
train_df, temp_df = train_test_split(random_sample2, test_size=0.2, random_state=52)
validation_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=51)

# Reset indices and rename columns for Hugging Face compatibility
train_df = train_df.rename(columns={"content": "text", "bias": "label"}).reset_index(drop=True)
validation_df = validation_df.rename(columns={"content": "text", "bias": "label"}).reset_index(drop=True)
test_df = test_df.rename(columns={"content": "text", "bias": "label"}).reset_index(drop=True)

# Convert to Hugging Face datasets
train_dataset = Dataset.from_pandas(train_df)
validation_dataset = Dataset.from_pandas(validation_df)
test_dataset = Dataset.from_pandas(test_df)



# Load the saved model and tokenizer
model = BertForSequenceClassification.from_pretrained("./bias_classifier_model_v6")
tokenizer = BertTokenizer.from_pretrained("./bias_classifier_model_v6")




# Tokenize the datasets
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

train_dataset = train_dataset.map(tokenize_function, batched=True)
validation_dataset = validation_dataset.map(tokenize_function, batched=True)
test_dataset = test_dataset.map(tokenize_function, batched=True)

# Remove unnecessary columns
columns_to_remove = [col for col in ["id", "text"] if col in train_dataset.column_names]
train_dataset = train_dataset.remove_columns(columns_to_remove)
validation_dataset = validation_dataset.remove_columns(columns_to_remove)
test_dataset = test_dataset.remove_columns(columns_to_remove)

# Ensure labels are integers
train_dataset = train_dataset.map(lambda x: {"labels": int(x["label"])})
validation_dataset = validation_dataset.map(lambda x: {"labels": int(x["label"])})
test_dataset = test_dataset.map(lambda x: {"labels": int(x["label"])})

# Set format for PyTorch
train_dataset.set_format("torch")
validation_dataset.set_format("torch")
test_dataset.set_format("torch")



# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
)

# Define the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=validation_dataset,
    tokenizer=tokenizer

)

# Train the model
trainer.train()

# Evaluate the model
results = trainer.evaluate(test_dataset)
print(results)

# Save the model and tokenizer
model.save_pretrained("./bias_classifier_model_v7")
tokenizer.save_pretrained("./bias_classifier_model_v7")


