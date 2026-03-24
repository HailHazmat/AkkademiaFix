import akkadian.transliterate as akk

# List of signs you want to translate
cuneiform_texts = [
    "𒁹𒀭𒌍𒋀𒈨𒌍𒌷𒁀",
    "𒀭𒊹𒆕𒀀",
]

print(f"{'Signs':<20} | {'Transliteration'}")
print("-" * 40)

for signs in cuneiform_texts:
    # Using the BiLSTM model
    translation = akk.transliterate_bilstm(signs)
    print(f"{signs:<20} | {translation}")