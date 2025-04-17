from pytube import YouTube
import os

def download_youtube_mp3(url, output_path="downloaded_audio.mp3"):
    try:
        # Erstelle YouTube-Objekt
        yt = YouTube(url)
        
        # Wähle den Audio-Stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        if not audio_stream:
            print("Kein Audio-Stream gefunden.")
            return
        
        # Lade den Stream herunter
        print(f"Lade herunter: {yt.title}")
        audio_stream.download(filename="temp_audio")
        
        # Konvertiere in MP3 (benötigt ffmpeg, muss installiert sein)
        os.system(f'ffmpeg -i temp_audio "{output_path}"')
        
        # Entferne temporäre Datei
        os.remove("temp_audio")
        
        print(f"Download abgeschlossen: {output_path}")
    except Exception as e:
        print(f"Fehler: {str(e)}")

# Beispielaufruf
if __name__ == "__main__":
    url = input("Gib die YouTube/YouTube Music URL ein: ")
    download_youtube_mp3(url)