import os
import cv2
import numpy as np

import cv2

def annotate_image(image, bounding_box, label):
    x, y, width, height = bounding_box
    cv2.rectangle(image, (x, y), (x + 200, y + 400), (0, 255, 0), 2)
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

def create_annotated_images(original_image_path, partially_annotated_image_path, fully_annotated_image_path):
    # Load the original image
    
    original_image = cv2.imread("D:/Guvi/placement/Akaike technologies task/task 1 CV/Shanmugavel-assignment-cv-main/Dataset/img3/original_image.jpg")

    # Create a copy of the original image for partial annotation
    partially_annotated_image = original_image.copy()

    # Create a copy of the original image for full annotation
    fully_annotated_image = original_image.copy()

    # Define the bounding boxes and labels for the cat and dog
    cat_bounding_box = (400, 400, 200, 200)
    dog_bounding_box = (300, 200, 180, 150)
    cat_label = 'Cat'
    dog_label = 'Dog'

    # Partially annotate the cat
    annotate_image(partially_annotated_image, cat_bounding_box, cat_label)

    # Fully annotate the cat and dog
    annotate_image(fully_annotated_image, cat_bounding_box, cat_label)
    annotate_image(fully_annotated_image, dog_bounding_box, dog_label)

    # Save the partially annotated image
    cv2.imwrite("D:/Guvi/placement/Akaike technologies task/task 1 CV/Shanmugavel-assignment-cv-main/Saved images/partially_annotated_image.png", partially_annotated_image)

    # Save the fully annotated image
    cv2.imwrite("D:/Guvi/placement/Akaike technologies task/task 1 CV/Shanmugavel-assignment-cv-main/Saved images/fully_annotated_image.png", fully_annotated_image)

# Usage example
original_image_path = "original_image.jpg"
fully_annotated_image_path = "D:/Guvi/placement/Akaike technologies task/task 1 CV/Shanmugavel-assignment-cv-main/Saved images/fully_annotated_image.png"
partially_annotated_image_path = "D:/Guvi/placement/Akaike technologies task/task 1 CV/Shanmugavel-assignment-cv-main/Saved images/partially_annotated_image.png"

create_annotated_images(original_image_path, partially_annotated_image_path, fully_annotated_image_path)
