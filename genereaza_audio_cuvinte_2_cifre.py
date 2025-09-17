from gtts import gTTS
import os
import zipfile

cuvinte = [
    "12", "37", "45", "83", "96", "54", "71", "68", "29", "77",
    "64", "88", "19", "42", "31", "99", "21", "73", "56", "62",
    "84", "28", "39", "47", "58", "93", "15", "26", "35", "48",
    "67", "74", "91", "33", "53", "27", "86", "95", "44", "81"
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
zip_path = "genereaza_audio_cuvinte_2_litere.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in file_paths:
        zipf.write(file, os.path.basename(file))
    zipf.write(mapping_path, os.path.basename(mapping_path))

print(f"\nArhiva creată: {zip_path}")
