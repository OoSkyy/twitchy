# Twitchy Discord Bot

## Übersicht

Twitchy ist ein Discord-Bot, der den Online-Status von Twitch-Streamern überwachen kann und Benachrichtigungen im Discord-Server sendet, wenn ein Streamer online geht. Der Bot bietet auch Befehle zum Hinzufügen und Entfernen von Twitch-Kanälen, die überwacht werden sollen, sowie zum Abrufen von Informationen zu einem Twitch-Nutzer.

## Voraussetzungen

- Python 3.x
- Discord Bot Token
- Twitch Client ID und Client Secret

## Installation

### 1. Repository klonen

Klone das Repository und wechsle in das Verzeichnis:

```sh
git clone https://github.com/dein-username/twitchy.git
cd twitchy
```
### 2. Virtuelle Umgebung erstellen und aktivieren

Erstelle eine virtuelle Umgebung und aktiviere sie:


```sh
python -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate
```
### 3. Abhängigkeiten installieren

Installiere die notwendigen Abhängigkeiten:

```sh
pip install -r requirements.txt
```
### 4. .env Datei erstellen

Kopiere die Datei .env.example zu .env und füge deine eigenen Werte ein:

```sh
cp .env.example .env
```
Bearbeite die .env Datei und füge deine eigenen Werte hinzu:


```plaintext
DISCORD_TOKEN=your_discord_token_here
TWITCH_CLIENT_ID=your_twitch_client_id_here
TWITCH_CLIENT_SECRET=your_twitch_client_secret_here
```
## Verwendung

Starte den Bot:

```sh
python app.py
```
Befehle

    !set_command_channel: Setzt den aktuellen Kanal als Befehlskanal.
    !set_message_channel: Setzt den aktuellen Kanal als Nachrichtkanal.
    !new_channel <username>: Fügt einen neuen Twitch-Kanal zur Überwachungsliste hinzu.
    !delete_channel <username>: Entfernt einen Twitch-Kanal von der Überwachungsliste.
    !twitch <username>: Gibt Informationen zu einem Twitch-Nutzer aus.

## Beispiel

Setze den Befehlskanal:

In einem Discord-Kanal, den du als Befehlskanal festlegen möchtest, schreibe:

    !set_command_channel

Setze den Nachrichtkanal:

In einem Discord-Kanal, in dem du Benachrichtigungen erhalten möchtest, schreibe:

    !set_message_channel

Füge einen Twitch-Kanal hinzu:

Um einen Twitch-Kanal zur Überwachungsliste hinzuzufügen, schreibe:

    !new_channel user_1337

Entferne einen Twitch-Kanal:

Um einen Twitch-Kanal von der Überwachungsliste zu entfernen, schreibe:

    !delete_channel user_1337

Hole Informationen zu einem Twitch-Nutzer:

Um Informationen zu einem Twitch-Nutzer zu erhalten, schreibe:

    !twitch user_1337

## Entwicklung
### Ordnerstruktur

```
twitchy/
│
├── app.py
├── config.py
├── twitch.py
├── commands.py
├── tasks.py
├── utils.py
├── .env.example
├── requirements.txt
└── README.md
```

## Beschreibung der Dateien

    app.py: Der Einstiegspunkt des Bots. Initialisiert den Bot, lädt Konfigurationen und startet die Tasks.
    config.py: Beinhaltet Funktionen zum Laden und Speichern der Konfiguration und der Kanalliste.
    twitch.py: Beinhaltet Funktionen zur Kommunikation mit der Twitch-API.
    commands.py: Definiert die Discord-Befehle.
    tasks.py: Definiert die Hintergrundtasks zum Überprüfen des Online-Status der Twitch-Kanäle.
    utils.py: Beinhaltet Hilfsfunktionen.
    .env.example: Beispiel für die .env Datei mit den notwendigen Umgebungsvariablen.
    requirements.txt: Beinhaltet die benötigten Python-Pakete.
    README.md: Diese Datei, die das Projekt beschreibt und Anweisungen zur Installation und Verwendung gibt.

## Entwickler

### John Klose