# CodeClauseInternship_PlagiarismChecker-Python
 Plagiarism Checker

The Plagiarism Checker is a user-friendly tool that allows users to compare text documents 
and determine potential plagiarism. This project features a graphical user interface (GUI) 
that enables users to input text manually or load text from both text files and PDF documents.
Using the Jaccard similarity metric, the tool calculates the similarity between the provided texts 
and indicates whether plagiarism is detected based on a user-specified threshold. With support for 
text and PDF file comparisons, this tool offers a versatile and accessible solution for content originality verification.
A simple plagiarism checker tool for comparing text documents. This project provides a user-friendly GUI for 
comparing text from both text files and PDF documents.

## Table of Contents

- [Features]
- [Prerequisites]
- [Usage]
- [License]

## Features

- Compare text from text files (.txt) and PDF files (.pdf).
- Calculate Jaccard similarity between texts.
- Determine whether plagiarism is detected based on a specified threshold.
- User-friendly GUI for easy input and result visualization.

## Prerequisites

- Python 3.x
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI
- [PyMuPDF](https://pypi.org/project/PyMuPDF/) for PDF text extraction (for PDF support)

##Usage
Run the Plagiarism Checker:
The GUI will open, allowing you to enter text manually or load text from text files or PDF files.

Click the "Check Plagiarism" button to compare the texts and view the results.

Adjust the similarity threshold as needed in the calculate_similarity function of the plagiarism_checker.py script.


##License
This project is licensed under the MIT License - see the LICENSE file for details.
