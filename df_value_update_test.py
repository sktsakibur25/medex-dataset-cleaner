import pandas as pd

bangla_column_list = ['Administration', 'Chemical Structure', 'Composition', 'Contraindications',
                'Description', 'Dosage', 'Dosage & Administration', 'Duration of Treatment',
                'Indications', 'Interaction', 'Overdose Effects', 'Pharmacology',
                'Precautions & Warnings', 'Pregnancy & Lactation', 'Reconstitution', 'Side Effects',
                'Storage Conditions', 'Therapeutic Class', 'Use in Special Populations', 'Common Questions']

def remove_text(row):
    for column in bangla_column_list:
        row[column] = row[column].replace("I'm not.", "")
    return row

df = pd.read_csv('medex_medicine_dataset_v2_translated.csv', sep=",")
df = df.fillna("N/A")
df = df.drop("Unnamed: 0", axis=1)
df = df.apply(remove_text, axis=1)
df.to_csv("medex_medicine_dataset_v3.csv")