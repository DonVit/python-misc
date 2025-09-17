from gtts import gTTS
import os
import zipfile

cuvinte = [
    "1023", "2847", "3956", "4671", "5832", "6904", "7128", "8365", "9471", "1582",
    "2634", "3749", "4810", "5926", "6073", "7184", "8295", "9346", "1047", "2158",
    "3269", "4370", "5481", "6592", "7603", "8714", "9825", "1096", "2107", "3218",
    "4329", "5430", "6541", "7652", "8763", "9874", "1985", "2096", "3107", "4218"
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
zip_path = "genereaza_audio_cuvinte_4_cifre.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in file_paths:
        zipf.write(file, os.path.basename(file))
    zipf.write(mapping_path, os.path.basename(mapping_path))

print(f"\nArhiva creată: {zip_path}")
