import PyPDF2
from decimal import Decimal
import statistics
import math

def truncate(n, decimals=2):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier

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
    num_of_journeys = len(array)
    lowest_journey = min(array)
    highest_journey = max(array)
    mean_journeys = truncate(statistics.mean(array))
    print(f"Number of journeys: {num_of_journeys} \nBetween (£{lowest_journey} ~ £{highest_journey}) \nMean: £{mean_journeys} \nTotal: £{total} \nTotal contribution: £{total_2}\n ")
    print(f"Total to claim: {Decimal(total) - Decimal(total_2)}")
    return total, total_2, num_of_journeys, lowest_journey, highest_journey, mean_journeys


if __name__ == "__main__":
    pdf_file = r"C:\Users\LukeV\OneDrive\My Documents\Uber reciepts\Uber reciepts\01 - October 2023\merged.pdf"
    with open('output.txt', 'w') as file:
        total, total_2, num_of_journeys, lowest_journey, highest_journey, mean_journeys = search_keyword(pdf_file, "Payments")
        file.write(f"Number of journeys: {num_of_journeys} \nBetween (£{lowest_journey} ~ £{highest_journey}) \nMean: £{mean_journeys} \nTotal Cost: £{total} \nTotal Contribution: £{total_2}\n")
        file.write(f"Total to claim back: {Decimal(total) - Decimal(total_2)}")
