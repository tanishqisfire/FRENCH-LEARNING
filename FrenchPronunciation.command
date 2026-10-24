#!/bin/bash

cd "$(dirname "$0")"

MODEL="llama3.1:8b"

load_brew() {
    if [ -x /opt/homebrew/bin/brew ]; then eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [ -x /usr/local/bin/brew ]; then eval "$(/usr/local/bin/brew shellenv)"
    fi
}
load_brew

if [ -f api_key.txt ]; then
   export LLM_API_KEY="$(cat api_key.txt)"
fi

if [ ! -f .setup_done ]; then
   echo "First-time setup. This can take 20-40 minutes, please keep this window open."

   if ! command -v brew >/dev/null; then
     echo "Installing Homebrew (it will ask for your Mac password)..."
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || { echo "Homebrew install failed."; exit 1;}
      load_brew
    fi

    brew install python@3.12 espeak-ng ffmpeg ollama || { echo "brew install failed."; exit 1;}

    "$(brew --prefix python@3.12)/bin/python3.12" -m venv .venv || { echo "venv creation failed."; exit 1; }
    source .venv/bin/activate 
    pip install --upgrade pip
    pip install -r requirements.txt || { echo "pip install failed."; exit 1; }

    echo "Downloading the speech model (about 1.2 GB)..."
    python -c "
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
n = 'facebook/wav2vec2-xlsr-53-espeak-cv-ft'
Wav2Vec2Processor.from_pretrained(n)
Wav2Vec2ForCTC.from_pretrained(n)
" || { echo "Speech model download failed."; exit 1; }

 touch .setup_done 
 echo "Setup finished."
fi

source .venv/bin/activate
export PHONEMIZER_ESPEAK_LIBRARY="$(brew --prefix espeak-ng)/lib/libespeak-ng.dylib"


OLLAMA_PID=""
if ! curl -s http://localhost:11434 >/dev/null; then
  echo "Starting Ollama..."
  ollama serve >/dev/null 2>&1 &
  OLLAMA_PID=$!
  until curl -s http://localhost:11434 >/dev/null; do sleep 1; done 
fi

if ! ollama list | grep -q "$MODEL"; then
   echo "Downloading $MODEL (about 8 GB, only happens once)..."
   ollama pull "$MODEL" || { echo "Model download failed."; exit 1; }
fi 

cleanup() {
    if [ -n "$OLLAMA_PID" ]; then kill "$OLLAMA_PID" 2>/dev/null; fi

}
trap cleanup EXIT


( until curl -s http://localhost:7860 >/dev/null; do sleep 1; done; open http://localhost:7860 ) &

python app.py