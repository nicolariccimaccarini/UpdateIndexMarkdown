import sys
import re

def generate_index(markdown_text):
    index = "# Index\n\n"
    headers = re.findall(r'(?m)^(#+)\s+(.*)', markdown_text)

    counters = [0] * 6                                          # One counter for each header level (1-6)

    for header in headers:
        level = len(header[0])                                  # header level
        title = header[1].strip()                               # header title
        anchor = title.lower()

        counters[level - 1] += 1                                # Increment the counter for the current level
        counters[level:] = [0] * len(counters[level:])          # Reset the counters for the lower levels

        indent_level = '    ' * (level - 1)
        index += f"{indent_level}{'.'.join(map(str, counters[:level]))}. [[#{anchor}]]\n"

    return index

def update_index_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            markdown_text = file.read()

        has_index = markdown_text.startswith("[TOC]\n")         # check if the index already exists

        index = generate_index(markdown_text)

        with open(file_path, 'w', encoding='utf-8') as file:
            if has_index:
                # remove the existing index
                markdown_lines = markdown_text.split('\n')
                markdown_text = '\n'.join(markdown_lines[markdown_text.count('[TOC]')+1:])

            file.write(index + '\n\n' + markdown_text)

        print("Index updated successfully.")

    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred while updating the index: {str(e)}")  

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_index.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    update_index_in_file(file_path)

if __name__ == "__main__":
    main()