import sys
import re

def generate_index(markdown_text):
    index = "## Indice\n\n"
    headers = re.findall(r'(?m)^#+\s+(.*)', markdown_text)
    
    for header in headers:
        level = header.count('#')
        title = header.strip('#').strip()
        anchor = title.lower().replace(' ', '-')
        index += f"{'  ' * (level - 1)}- [{' '.join(title.splitlines())}](#{anchor})\n"
    
    return index

def update_index_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            markdown_text = file.read()

        index = generate_index(markdown_text)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(index + '\n' + markdown_text)

        print("Indice aggiornato correttamente.")

    except FileNotFoundError:
        print("Il file specificato non è stato trovato.")
    except Exception as e:
        print(f"Si è verificato un errore durante l'aggiornamento dell'indice: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 update.py <percorso_file_markdown>")
    else:
        file_path = sys.argv[1]
        update_index_in_file(file_path)
