from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text

def check_words_in_text(text, words):
    results = {}
    lowercase_text = text.lower()

    for word in words:
        lowercase_word = word.lower()
        results[word] = lowercase_word in lowercase_text

    return results

def save_results_to_file(results, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for word, found in results.items():
            if found:
                file.write(f"{word}: found\n")
            else:
                file.write(f"{word}: not found\n")

pdf_path = "example.pdf"
words_to_check = ["Herning", "Aarhus", "Banana", "Mathias", "mif"]
output_file = "results.txt"

pdf_text = extract_text_from_pdf(pdf_path)
results = check_words_in_text(pdf_text, words_to_check)
save_results_to_file(results, output_file)

for word, found in results.items():
    print(word, found)
