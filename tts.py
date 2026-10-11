import subprocess
import sys



def text_to_speech(text, output_path="output.wav", voice="fr_FR-siwis-medium"):
    subprocess.run([sys.executable, "-m", "piper", "-m", voice, "-f", output_path, "--", text],
                    check = True, )
    
    return output_path