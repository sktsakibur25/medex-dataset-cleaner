import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('medex_medicine_dataset_v1.csv', index_col="Id")
df = df.fillna("N/A")
short_df = df.head(10)
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

column_list = ['Administration', 'Chemical Structure', 'Composition', 'Contraindications',
                'Description', 'Dosage', 'Dosage & Administration', 'Duration of Treatment',
                'Indications', 'Interaction', 'Overdose Effects', 'Pharmacology',
                'Precautions & Warnings', 'Pregnancy & Lactation', 'Reconstitution', 'Side Effects',
                'Storage Conditions', 'Therapeutic Class', 'Use in Special Populations', 'Common Questions']

def check_if_bangla_text_exists(bangla_char_list, long_string_to_check):
    for bangla_character in bangla_char_list:
        if bangla_character in long_string_to_check:
            return True
    return False

for column in column_list:
    medex_column_list = df[column].values.tolist()
    bengali_string_count = 0
    for data in medex_column_list:
        data = data.encode().decode("utf-8")
        if check_if_bangla_text_exists(chars_bengali, data):
            print(data)
            bengali_string_count += 1
    print(column + " contains "+ str(bengali_string_count) +" bengali data")