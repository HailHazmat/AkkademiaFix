import os
import sys
from pathlib import Path

# Fix: Add the 'akkadian' folder to the Python path so it can find helper modules
current_dir = os.path.dirname(os.path.abspath(__file__))
akkadian_path = os.path.join(current_dir, "akkadian")
if akkadian_path not in sys.path:
    sys.path.append(akkadian_path)

# Now we can safely import from the subfolder
from akkadian.translate_from_cuneiform import translate_cuneiform_file
from akkadian.translate_from_transliteration import translate_transliteration_file

def run_batch_translation():
    print("--- Akkadia Batch Translator (Windows Optimized) ---")
    print("1. Translate a folder of CUNEIFORM signs")
    print("2. Translate a folder of TRANSLITERATION syllables")
    
    choice = input("\nSelect an option (1 or 2): ")
    folder_name = input("Enter the folder name (e.g., input_texts): ").strip()

    # Ensure we are looking in the right spot relative to this script
    folder_path = os.path.join(current_dir, folder_name)

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    if not files:
        print(f"No .txt files found in {folder_path}.")
        return

    print(f"\nFound {len(files)} files. Starting translation...\n")

    for filename in files:
        full_path = os.path.join(folder_path, filename)
        print(f"--- Processing: {filename} ---")
        
        try:
            if choice == '1':
                translate_cuneiform_file(full_path)
            else:
                translate_transliteration_file(full_path)
        except Exception as e:
            print(f"Error translating {filename}: {e}")
        
        print("-" * 30)

if __name__ == "__main__":
    run_batch_translation()