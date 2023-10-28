import PyPDF2
from decimal import Decimal

def search_keyword(pdf_file, keyword):
    array = []
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if keyword in text:
                words = text.split()
                index = words.index(keyword)
                if index < len(words) - 1:
                    next_word = words[index + 1]
                    print(f"{next_word}")
                    array.append(Decimal(next_word[1:]))
    total = sum(array)
    total_2 = len(array) * 5.25
    print(f"Total: £{total}, Total contribution: £{total_2}")

if __name__ == "__main__":
    pdf_file = r"C:\Users\LukeV\OneDrive\My Documents\Uber reciepts\Uber reciepts\01 - October 2023\merged.pdf"
    search_keyword(pdf_file, "Payments")
