import sys
import re

def generate_index(markdown_text):
    index = "# Index\n\n"
    headers = re.findall(r'(?m)^#+\s+(.*)', markdown_text)
    
    for header in headers:
        level = header.count('#')
        title = header.strip('#').strip()
        anchor = title.lower()
        index += f"{'  ' * (level - 1)}1. [[#{anchor}]]\n"
    
    return index

def update_index_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            markdown_text = file.read()

        index = generate_index(markdown_text)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(index + '\n' + markdown_text)

        print("Index updated successfully.")

    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred while updating the index: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_index.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    update_index_in_file(file_path)

if __name__ == "__main__":
    main()
