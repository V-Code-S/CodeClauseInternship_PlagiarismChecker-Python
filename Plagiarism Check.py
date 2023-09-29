import string
import tkinter as tk
from tkinter import filedialog, messagebox
import fitz  # Import PyMuPDF for PDF text extraction

def text_preprocessing(text):
    # Remove punctuation and convert text to lowercase
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()
    return text

def calculate_similarity(text1, text2):
    # Preprocess both texts
    text1 = text_preprocessing(text1)
    text2 = text_preprocessing(text2)

    # Split texts into words
    words1 = set(text1.split())
    words2 = set(text2.split())

    # Calculate Jaccard similarity
    intersection = len(words1.intersection(words2))
    union = len(words1) + len(words2) - intersection

    similarity = intersection / union
    return similarity

def load_text_from_file(entry, file_type):
    file_path = filedialog.askopenfilename(filetypes=[(file_type, "*" + file_type)])
    if file_path:
        if file_type == ".pdf":
            text = extract_text_from_pdf(file_path)
        else:
            text = extract_text_from_text_file(file_path)
        
        entry.delete("1.0", "end")
        entry.insert("1.0", text)

def extract_text_from_pdf(pdf_file_path):
    text = ""
    try:
        pdf_document = fitz.open(pdf_file_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text += page.get_text()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    return text

def extract_text_from_text_file(text_file_path):
    try:
        with open(text_file_path, "r") as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ""

def check_plagiarism():
    text1 = entry1.get("1.0", "end-1c")  # Get text from the first text box
    text2 = entry2.get("1.0", "end-1c")  # Get text from the second text box

    if not text1 or not text2:
        messagebox.showerror("Error", "Please enter both texts.")
        return

    similarity = calculate_similarity(text1, text2)

    threshold = 0.7

    if similarity >= threshold:
        result_label.config(text=f"Plagiarism Detected. Similarity: {similarity:.2f}", fg="red", font=("Arial", 12, "bold"))
    else:
        result_label.config(text=f"No Plagiarism Detected. Similarity: {similarity:.2f}", fg="green", font=("Arial", 12, "bold"))

# Create a GUI window
window = tk.Tk()
window.title("Plagiarism Checker - By VIRUPAKSHI")

# Create text input boxes
label1 = tk.Label(window, text="Enter the first text or load from file:")
label1.pack()

entry1 = tk.Text(window, height=10, width=50)
entry1.pack()

load_button1 = tk.Button(window, text="Load Text File for Text 1", command=lambda: load_text_from_file(entry1, ".txt"), bg="lightblue")
load_button1.pack(pady=5)

load_pdf_button1 = tk.Button(window, text="Load PDF for Text 1", command=lambda: load_text_from_file(entry1, ".pdf"), bg="lightblue")
load_pdf_button1.pack(pady=5)

label2 = tk.Label(window, text="Enter the second text or load from file:")
label2.pack()

entry2 = tk.Text(window, height=10, width=50)
entry2.pack()

load_button2 = tk.Button(window, text="Load Text File for Text 2", command=lambda: load_text_from_file(entry2, ".txt"), bg="lightblue")
load_button2.pack(pady=5)

load_pdf_button2 = tk.Button(window, text="Load PDF for Text 2", command=lambda: load_text_from_file(entry2, ".pdf"), bg="lightblue")
load_pdf_button2.pack(pady=5)

# Create a button to check plagiarism
check_button = tk.Button(window, text="Check Plagiarism", command=check_plagiarism, bg="green", fg="white")
check_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="", fg="black")
result_label.pack()

window.mainloop()
