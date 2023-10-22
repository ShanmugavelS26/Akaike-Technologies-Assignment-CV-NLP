# -*- coding: utf-8 -*-

import PyPDF2
import random

def text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
    
def get_mca_questions(context):
    # Split the context into sentences
    sentences = context.strip().split('. ')

    # Generate multiple-choice questions
    mca_questions = []
    for sentence in sentences:
        question = "Which of the following is true about " + sentence + "?"
        choices = random.sample(sentences, k=3)  # Randomly select 3 choices
        choices.append(sentence)  # Add the correct answer to the choices
        random.shuffle(choices)  # Shuffle the choices

        mca_question = question + "\n"
        for i, choice in enumerate(choices):
            mca_question += chr(ord('a') + i) + ") " + choice + "\n"

        mca_questions.append(mca_question)

    return mca_questions 


file_path = 'chapter-2.pdf'
context = text_from_pdf(file_path)

questions = get_mca_questions(context)
for i, question in enumerate(questions):
    print("Questions from chapter 2")
    print(f"Question {i+1}: {question}")
    

file_path = 'chapter-3.pdf'
context = text_from_pdf(file_path)

questions = get_mca_questions(context)
for i, question in enumerate(questions):
    print("Questions from chapter 3")
    print(f"Question {i+1}: {question}")
    
    
file_path = 'chapter-4.pdf'
context = text_from_pdf(file_path)

questions = get_mca_questions(context)
for i, question in enumerate(questions):
    print("Questions from chapter 4")
    print(f"Question {i+1}: {question}")