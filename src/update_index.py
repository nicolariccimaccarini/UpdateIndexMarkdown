import sys
import re

def generate_index(markdown_text):
    index = "# Index\n\n"
    headers = re.findall(r'(?m)^(#+)\s+(.*)', markdown_text)

    paragraphs_counter = 1
    sub_paragraphs_in_paragraph = {}    # Stores the number of subsections for each paragraph.

    for header in headers:
        level = len(header[0])          # header level
        title = header[1].strip()       # header title
        anchor = title.lower()

        if level == 1:
            index += f"{paragraphs_counter}. [[#{anchor}]]\n"
            sub_paragraphs_in_paragraph[paragraphs_counter] = 1
            paragraphs_counter += 1
        else:
            sub_paragraphs_counter = sub_paragraphs_in_paragraph.get(paragraphs_counter, 1)

            indent_level = '    ' * (level - 1)
            index += f"{indent_level}{sub_paragraphs_counter}. [[#{anchor}]]\n" 
            
            sub_paragraphs_in_paragraph[paragraphs_counter] = sub_paragraphs_counter + 1

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
        print(f"An error occurred while updating the index: {str(e)}")  

def main():
    if len(sys.argv) != 2:
        print("Usage: python update_index.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    update_index_in_file(file_path)

if __name__ == "__main__":
    main()