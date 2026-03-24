import akkadian.transliterate as akk
from datetime import datetime
import os

def main():
    log_file = "translation_log.txt"
    
    print("="*50)
    print("Akkademia Translator + Auto-Logger")
    print(f"Saving history to: {os.path.abspath(log_file)}")
    print("Type 'exit' to quit.")
    print("="*50)

    while True:
        user_input = input("\nSigns: ").strip()

        if user_input.lower() in ['exit', 'quit']:
            break

        if not user_input:
            continue

        try:
            # 1. Perform the translation
            result = akk.transliterate_bilstm(user_input)
            
            # 2. Get the current time
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 3. Print to screen
            print(f"Result: {result}")

            # 4. Append to the log file
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}]\n")
                f.write(f"Input:  {user_input}\n")
                f.write(f"Output: {result}\n")
                f.write("-" * 30 + "\n")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()