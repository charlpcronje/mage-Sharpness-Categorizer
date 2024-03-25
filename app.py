import cv2
import os
import shutil
import sys
import json
from pathlib import Path

def read_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def calculate_blur(image_path):
    image = cv2.imread(image_path)
    return cv2.Laplacian(image, cv2.CV_64F).var()

def sort_images(folder_path, percentages):
    sharpness_scores = []
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        if os.path.isfile(image_path):
            try:
                blur = calculate_blur(image_path)
                sharpness_scores.append((image_name, blur))
            except Exception as e:
                print(f"Error processing {image_path}: {e}")
    sharpness_scores.sort(key=lambda x: x[1], reverse=True)

    total_images = len(sharpness_scores)
    best_threshold = int(total_images * (percentages['best'] / 100.0))
    better_threshold = best_threshold + int(total_images * (percentages['better'] / 100.0))
    med_threshold = better_threshold + int(total_images * (percentages['med'] / 100.0))

    categorized_images = {
        "best": sharpness_scores[:best_threshold],
        "better": sharpness_scores[best_threshold:better_threshold],
        "med": sharpness_scores[better_threshold:med_threshold]
    }

    return categorized_images

def main(folder_path):
    config = read_config("config.json")
    percentages = config["percentages"]
    sorted_images = sort_images(folder_path, percentages)
    for category, images in sorted_images.items():
        dest_path = os.path.join(folder_path, category)
        os.makedirs(dest_path, exist_ok=True)
        for image, _ in images:
            src_path = os.path.join(folder_path, image)
            shutil.copy(src_path, dest_path)
            print(f"Copied {image} to {dest_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_folder>")
    else:
        folder_path = sys.argv[1].strip("\"' ")
        folder_path = os.path.normpath(folder_path)
        main(folder_path)
