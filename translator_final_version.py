import pandas as pd
from transformers import pipeline
import torch

chars_bengali = [
    'অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'ৠ', 'ঌ', 'ৡ',
    'এ', 'ঐ', 'ও', 'ঔ',
    'ক', 'খ', 'গ', 'ঘ', 'ঙ',
    'চ', 'ছ', 'জ', 'ঝ', 'ঞ',
    'ট', 'ঠ', 'ড', 'ঢ', 'ণ',
    'ত', 'থ', 'দ', 'ধ', 'ন',
    'প', 'ফ', 'ব', 'ভ', 'ম',
    'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ',
    'ৰ', 'ৱ',
    'ঃ', 'ং', 'ঁ',
    '়', '্', 'ড়', 'ঢ়', 'য়',
    '০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'
]

translated_text_list = []

total_bangla_data = 593
processed_bangla_data = 1
ID = 0

base_column_list = ['Name', 'Type', 'Strength', 'Generic Name', 'Availablity',
                    'Manufactured By', 'Price']

bangla_column_list = ['Administration', 'Chemical Structure', 'Composition', 'Contraindications',
                'Description', 'Dosage', 'Dosage & Administration', 'Duration of Treatment',
                'Indications', 'Interaction', 'Overdose Effects', 'Pharmacology',
                'Precautions & Warnings', 'Pregnancy & Lactation', 'Reconstitution', 'Side Effects',
                'Storage Conditions', 'Therapeutic Class', 'Use in Special Populations', 'Common Questions']

# translator pipeline
translator = pipeline(task="translation",
                      model="../models/nllb-200-distilled-600M",
                      torch_dtype=torch.bfloat16)

def convert_to_boiler_plate(id, column, old_value, new_value):
    translated_text_boilerplate = {
    "med_Id": 0,
    "attribute":"N/A",
    "bangla_text":"N/A",
    "translated_text":"N/A"
    }

    translated_text_boilerplate['med_Id'] = id
    translated_text_boilerplate['attribute'] = column   
    translated_text_boilerplate['bangla_text'] = old_value
    translated_text_boilerplate['translated_text'] = new_value

    return translated_text_boilerplate
    

def check_if_bangla_text_exists(bangla_char_list, long_string_to_check):
    for bangla_character in bangla_char_list:
        if bangla_character in long_string_to_check:
            return True
    return False

def translate_to_english(bangla_text):
    spitted_text = bangla_text.split("।")
    # spitted_text.remove("")cle
    translated_text = ""
    for part_of_text in spitted_text:
        part_of_translated_text = translator(part_of_text,
                                    src_lang = "ben_Beng",
                                    tgt_lang = 'eng_Latn')[0]["translation_text"]
        translated_text = translated_text + part_of_translated_text+"."
        translated_text = translated_text.strip()
        translated_text = translated_text.replace("..", ". ")
        translated_text = translated_text.strip()
    return translated_text

def update_count():
    global processed_bangla_data
    processed_bangla_data = processed_bangla_data + 1

def translate_rows(row):
    for column in bangla_column_list:
        current_text = row[column] 
        if check_if_bangla_text_exists(chars_bengali, current_text):
            print("translating text "+ str(processed_bangla_data)+"/"+str(total_bangla_data))
            translated_text = translate_to_english(current_text)
            update_count()
            translated_text_history = convert_to_boiler_plate(row["Id"], column, current_text, translated_text)
            translated_text_list.append(translated_text_history)
            row[column] = translated_text
            print("translation Done!")
            
    return row
    

df = pd.read_csv('medex_medicine_dataset_v1.csv', sep=",")
df = df.fillna("N/A")
df = df.drop("Unnamed: 0", axis=1)
df = df.apply(translate_rows, axis=1)

df.to_csv("medex_medicine_dataset_v2_translated.csv")

translated_df = pd.DataFrame(translated_text_list)
translated_df.to_csv("translated_rows.csv")

