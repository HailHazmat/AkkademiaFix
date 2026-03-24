import subprocess
import os
import sys
from pathlib import Path
from translation_tokenize import tokenize
from translate_common import source, translation, detokenize_cuneiform, detokenize_translation

def translate_cuneiform_base(file, capture_output=False):
    # Ensure the local tmp directory exists
    os.makedirs("tmp", exist_ok=True)
    
    # Process the signs using the char-level tokenizer
    tokenize("signs_char", file, False, Path("NMT_input/tokenization"), Path(""), Path("tmp"))
    
    # Correct paths and flags for Cuneiform translation
    cmd = [
        sys.executable,
        "../fairseq/fairseq_cli/interactive.py",
        "data-bin-not-divided-by-three-dots/",
        "--task", "translation",
        "--source-lang", "ak",
        "--target-lang", "en",
        "--path", "not_divided_by_three_dots_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt",
        "--beam", "5",
        "--input", "tmp/" + file
    ]

    result = subprocess.run(cmd, capture_output=True)
    
    # Diagnostics for troubleshooting
    if result.returncode != 0 or not result.stdout:
        print("\n--- FAIRSEQ DIAGNOSTICS ---")
        print(f"Interpreter: {sys.executable}")
        print(f"Error Message:\n{result.stderr.decode('utf-8', errors='ignore')}")
        print("----------------------------\n")
        
    return result

def translate_cuneiform_raw(file):
    translate_cuneiform_base(file)

def translate_cuneiform_file(file):
    raw_result = translate_cuneiform_base(file, True).stdout
    if not raw_result:
        return

    for line in raw_result.decode().split('\n'):
        if source(line):
            print(detokenize_cuneiform(line, "NMT_input/not_divided_by_three_dots/tokenization/signs_char.model"))
        if translation(line):
            print(detokenize_translation(line,
                                         "NMT_input/not_divided_by_three_dots/tokenization/translation_bpe.model",
                                         True) + "\n")

if __name__ == '__main__':
    cuneiform_file = input("Please enter the name of the Akkadian file for translation\n")
    translate_cuneiform_file(cuneiform_file)