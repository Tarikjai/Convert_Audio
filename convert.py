 
import whisper

# Chemin vers ton fichier WAV



# Charger le modèle
modele = whisper.load_model("base")  # "small", "medium", "large" selon tes besoins

# Chemin vers ton fichier WAV
fichier_audio = "C:/Users/Professional/Desktop/Convert/Entretien.wav" # Remplace ce chemin par le chemin de ton fichier WAV

# Transcription
resultat = modele.transcribe(fichier_audio, language="fr")  # Spécifie "fr" pour le français

# Enregistrement du texte dans un fichier .txt
with open("Entretien.txt", "w", encoding="utf-8") as fichier:
    fichier.write(resultat['text'])

print("La transcription a été enregistrée dans 'Entretien.txt'.")