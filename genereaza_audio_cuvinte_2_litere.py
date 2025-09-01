from gtts import gTTS
import os
import zipfile

cuvinte = [
    # Pronume / articole / gramaticale
    "am", "au", "ce", "ci", "cu", "da", "de", "ea", "ei", "el", "eu",
    "ia", "ie", "îi", "în", "la", "le", "li", "lo", "lu", "ma", "mi",
    "ne", "ni", "nu", "o", "or", "pe", "re", "sa", "se", "si", "și",
    "su", "ta", "te", "ti", "to", "tu", "un"
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
