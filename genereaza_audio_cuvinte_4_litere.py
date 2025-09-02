from gtts import gTTS
import os
import zipfile
import uuid

# Lista de 40 cuvinte populare în română (4 litere fiecare)
cuvinte = [
    "apa", "mai", "era", "rau", "nou", "dar", "jos", "sus", "azi", "are",
    "voi", "tie", "mie", "noi", "ele", "ea", "el", "un", "doi", "tre",
    "bun", "dor", "nor", "sat", "bar", "nas", "cer", "mic", "cat", "tot",
    "cum", "cui", "aia", "azi", "iar", "ora", "foc", "vin", "zic", "pat"
]


# Director de lucru
output_dir = "cuvinte_audio"
os.makedirs(output_dir, exist_ok=True)

# Fișier de mapare cuvânt → nume random
mapping_path = os.path.join(output_dir, "mapping.txt")
with open(mapping_path, "w", encoding="utf-8") as mapping_file:
    file_paths = []
    for cuv in cuvinte:
        random_name = f"{uuid.uuid4().hex[:8]}.mp3"
        file_path = os.path.join(output_dir, random_name)
        
        tts = gTTS(cuv, lang="ro", slow=False)
        tts.save(file_path)
        file_paths.append(file_path)

        mapping_file.write(f"{random_name} -> {cuv}\n")
        print(f"Generat: {random_name} ({cuv})")

# Creăm arhiva ZIP
zip_path = "cuvinte_romana_random.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in file_paths:
        zipf.write(file, os.path.basename(file))
    zipf.write(mapping_path, os.path.basename(mapping_path))

print(f"\nArhiva creată: {zip_path}")
