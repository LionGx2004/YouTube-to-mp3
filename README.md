### Anleitung zur Verwendung des YouTube MP3 Downloaders

Dieser Python-Code ermöglicht es, Audio von YouTube-Videos oder YouTube Music als MP3-Datei herunterzuladen. Folge dieser Anleitung, um den Code zu verwenden:

---

#### Voraussetzungen
1. **Python installieren**:
   - Stelle sicher, dass Python (Version 3.x) auf deinem Computer installiert ist. Du kannst Python von [python.org](https://www.python.org/downloads/) herunterladen.
   - Überprüfe die Installation mit dem Befehl:
     ```bash
     python --version
     ```

2. **Erforderliche Bibliotheken installieren**:
   - Installiere die `pytube`-Bibliothek, die für den Download von YouTube-Videos benötigt wird. Führe folgenden Befehl im Terminal oder in der Eingabeaufforderung aus:
     ```bash
     pip install pytube
     ```

3. **FFmpeg installieren**:
   - Der Code verwendet `ffmpeg`, um das heruntergeladene Audio in das MP3-Format zu konvertieren. Lade FFmpeg von [ffmpeg.org](https://ffmpeg.org/download.html) herunter oder installiere es mit einem Paketmanager:
     - **Windows**: 
       - Lade FFmpeg von einer vertrauenswürdigen Quelle herunter (z. B. [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)).
       - Füge den Pfad zum `ffmpeg.exe` zu deiner Systemumgebungsvariable `PATH` hinzu.
     - **macOS** (mit Homebrew):
       ```bash
       brew install ffmpeg
       ```
     - **Linux** (mit apt):
       ```bash
       sudo apt update
       sudo apt install ffmpeg
       ```
   - Überprüfe die Installation mit:
     ```bash
     ffmpeg -version
     ```

---

#### Vorbereitung des Codes
1. **Code speichern**:
   - Kopiere den bereitgestellten Code in eine Datei und speichere sie als `youtube_mp3_downloader.py`.

2. **Datei anpassen (optional)**:
   - Standardmäßig wird die MP3-Datei als `downloaded_audio.mp3` gespeichert. Du kannst den `output_path` im Code ändern, um einen anderen Dateinamen oder Speicherort zu verwenden, z. B.:
     ```python
     download_youtube_mp3(url, output_path="mein_lieblingslied.mp3")
     ```

---

#### Ausführen des Codes
1. **Terminal oder Eingabeaufforderung öffnen**:
   - Navigiere in das Verzeichnis, in dem die Datei `youtube_mp3_downloader.py` gespeichert ist. Beispiel:
     ```bash
     cd Pfad/zum/Ordner
     ```

2. **Skript starten**:
   - Führe das Skript aus, indem du folgenden Befehl eingibst:
     ```bash
     python youtube_mp3_downloader.py
     ```

3. **YouTube-URL eingeben**:
   - Du wirst aufgefordert, eine YouTube- oder YouTube Music-URL einzugeben. Kopiere die URL des gewünschten Videos oder Songs (z. B. `https://www.youtube.com/watch?v=XXXXXXX`) und füge sie ein. Drücke Enter.

4. **Download starten**:
   - Das Skript lädt den Audio-Stream herunter, konvertiert ihn in MP3 und speichert die Datei im angegebenen Pfad (standardmäßig im gleichen Verzeichnis wie das Skript).
   - Du siehst Fortschrittsmeldungen wie:
     ```
     Lade herunter: [Titel des Videos]
     Download abgeschlossen: downloaded_audio.mp3
     ```

---

#### Fehlerbehebung
- **Fehler: "Kein Audio-Stream gefunden"**:
  - Stelle sicher, dass die URL korrekt ist und das Video Audio enthält.
- **Fehler: "ffmpeg nicht gefunden"**:
  - Überprüfe, ob FFmpeg korrekt installiert ist und im Systempfad verfügbar ist.
- **Fehler: "pytube funktioniert nicht"**:
  - Aktualisiere pytube mit:
    ```bash
    pip install --upgrade pytube
    ```
- **Andere Fehler**:
  - Lies die Fehlermeldung im Terminal. Häufige Probleme sind eine ungültige URL oder fehlende Internetverbindung.

---

#### Hinweise
- **Rechtliche Hinweise**:
  - Lade nur Inhalte herunter, für die du die Erlaubnis hast. Das Herunterladen von urheberrechtlich geschütztem Material ohne Genehmigung kann illegal sein.
- **Dateispeicherort**:
  - Die MP3-Datei wird im gleichen Verzeichnis wie das Skript gespeichert, es sei denn, du gibst einen anderen `output_path` an.
- **Mehrere Downloads**:
  - Um mehrere Dateien herunterzuladen, führe das Skript erneut aus oder passe den Code an, um mehrere URLs zu verarbeiten.

---

Mit dieser Anleitung solltest du den YouTube MP3 Downloader problemlos verwenden können! 
