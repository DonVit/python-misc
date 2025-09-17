from gtts import gTTS
import os
import zipfile

cuvinte = [
    "127", "384", "592", "641", "713", "859", "904", "276", "318", "457",
    "682", "795", "234", "369", "421", "578", "693", "842", "915", "367",
    "102", "289", "345", "436", "527", "618", "729", "803", "954", "687",
    "111", "222", "333", "444", "555", "666", "777", "888", "999", "123"
]


# Director de lucru
output_dir = "cuvinte_audio"
os.makedirs(output_dir, exist_ok=True)

# Fișier de mapare cuvânt → nume increment
mapping_path = os.path.join(output_dir, "mapping.txt")
with open(mapping_path, "w", encoding="utf-8") as mapping_file:
    file_paths = []
    for idx, cuv in enumerate(cuvinte, start=1):
        file_name = f"{idx}.mp3"
        file_path = os.path.join(output_dir, file_name)

        tts = gTTS(cuv, lang="ro", slow=False)
        tts.save(file_path)
        file_paths.append(file_path)

        mapping_file.write(f"{file_name} -> {cuv}\n")
        print(f"Generat: {file_name} ({cuv})")

# Creăm arhiva ZIP
zip_path = "genereaza_audio_cuvinte_3_cifre.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in file_paths:
        zipf.write(file, os.path.basename(file))
    zipf.write(mapping_path, os.path.basename(mapping_path))

print(f"\nArhiva creată: {zip_path}")
