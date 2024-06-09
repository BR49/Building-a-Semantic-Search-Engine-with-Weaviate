from sklearn.metrics import precision_score, recall_score, f1_score

# Assuming we have true labels and predicted labels for evaluation
true_labels = [...]  # True relevance labels
predicted_labels = [...]  # Predicted relevance labels

precision = precision_score(true_labels, predicted_labels, average='weighted')
recall = recall_score(true_labels, predicted_labels, average='weighted')
f1 = f1_score(true_labels, predicted_labels, average='weighted')
print(f"Precision: {precision}, Recall: {recall}, F1 Score: {f1}")
