FROM python:3.11-slim

RUN apt-get update && apt-get install -y espeak-ng ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /home/user/app

COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=user . .

RUN python -c "from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC; n='facebook/wav2vec2-xlsr-53-espeak-cv-ft'; Wav2Vec2Processor.from_pretrained(n); Wav2Vec2ForCTC.from_pretrained(n)"

EXPOSE 7860 

CMD ["python", "app.py"]
