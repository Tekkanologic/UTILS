import os
import PyPDF2

# Using OS iterate through file system, taking morning and afternoon PDF and adding them to a single file
def merge_pdfs(input_folder, output_file):
    merger = PyPDF2.PdfMerger()
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                merger.append(file_path)
    merger.write(output_file)
    merger.close()

# Using a PDF reader retrieve the cost per journey and sum it
if __name__ == "__main__":
    input_foler = r"C:\Users\LukeV\OneDrive\My Documents\Uber reciepts\Uber reciepts\01 - October 2023"
    output_file = r"C:\Users\LukeV\OneDrive\My Documents\Uber reciepts\Uber reciepts\01 - October 2023\merged.pdf"
    merge_pdfs(input_foler, output_file)
    