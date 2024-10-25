from pydub import AudioSegment

# Fonction de conversion audio
def convert_to_wav(input_file, output_file):
    # Charger le fichier audio
    audio = AudioSegment.from_file(input_file)
    # Exporter au format WAV
    audio.export(output_file, format="wav")
    print(f"Conversion terminée : {output_file}")

# Exemple d'utilisation
input_file = "C:/Users/Professional/Desktop/Convert/Entretien.dat.unknown"  # Remplace par ton fichier d'entrée
output_file = "Entretien.wav"  # Nom du fichier de sortie
convert_to_wav(input_file, output_file)
