from transformers import pipeline
import torch

# translator pipeline
translator = pipeline(task="translation",
                      model="../models/nllb-200-distilled-600M",
                      torch_dtype=torch.bfloat16)

text_to_translate = 'প্রস্তাবিত প্রারম্ভিক ডোজ হল 120mg দিন বিভক্ত ডোজে, রোগীর প্রতিক্রিয়ার উপর নির্ভর করে বিভক্ত ডোজে 180mg দিনে বৃদ্ধি পায়। বয়স্ক রোগীদের চিকিত্সার জন্য, ডোজ সামঞ্জস্য সাধারণত প্রয়োজন হয় না। যাইহোক, এনএসএআইডিগুলি বয়স্ক রোগীদের বিশেষ যত্নের সাথে ব্যবহার করা উচিত যারা প্রতিকূল প্রতিক্রিয়ার জন্য বেশি প্রবণ হতে পারে। গ্যাস্ট্রো-অন্ত্রের ব্যাঘাতের সম্ভাবনা কমাতে খাবার, দুধ বা অ্যান্টাসিডের সাথে অ্যাসিমেটাসিন গ্রহণ করা উচিত।'

spitted_text = text_to_translate.split("।")
spitted_text.remove("")
translated_text = ""
for part_of_text in spitted_text:
    part_of_translated_text = translator(part_of_text,
                                src_lang = "ben_Beng",
                                tgt_lang = 'eng_Latn')[0]["translation_text"]
    translated_text = translated_text + part_of_translated_text+"."
    translated_text = translated_text.strip()
    translated_text = translated_text.replace("..", ". ")
    translated_text = translated_text.strip()

print(translated_text)
