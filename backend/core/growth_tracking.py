import json
import cv2
import numpy as np
from backend.core.Preprocessing.preprocess import url_to_cv2_image, preprocess_image
from backend.core.Preprocessing.dynamicThresholding import get_dynamic_green_bounds
from backend.utils.comparison_metrics import (
    calculate_bounding_box_area,
    calculate_green_pixel_count,
    estimate_leaf_count,
    calculate_color_health_index,
    estimate_sunlight_proxy
)

# Load species-specific weights
with open("backend/utils/species_weight.json", "r") as f:
    SPECIES_WEIGHTS = json.load(f)

def extract_metrics(image):
    """
    Extracts all growth metrics from a given image.
    Returns a dictionary of metrics.
    """
    preprocessed = preprocess_image(image)
    hsv = cv2.cvtColor(preprocessed["blurred"], cv2.COLOR_BGR2HSV)

    # # Dynamically get green bounds
    # lower_green, upper_green = get_dynamic_green_bounds(image)

    # Bounding Box Area
    bounding_box_area, _ = calculate_bounding_box_area(preprocessed["mask"])

    # Green Pixel Count and Ratio
    green_pixel_count, green_pixel_ratio = calculate_green_pixel_count(image)

    # Leaf Count Estimation
    leaf_count = estimate_leaf_count(preprocessed["plant_only"])

    # Color Health Index
    color_health = calculate_color_health_index(preprocessed["plant_only"])

    # Sunlight Proxy Estimation
    sunlight_proxy = estimate_sunlight_proxy(image)

    return {
        "bounding_box": bounding_box_area,
        "green_ratio": green_pixel_ratio,
        "leaf_count": leaf_count,
        "color_health": color_health,
        "sunlight_proxy": sunlight_proxy
    }

def compare_and_score_growth(current_img_url, previous_img_url, species):
    """
    Compare growth metrics of current and previous images and generate a growth score.
    Returns the score and delta values of each metric.
    """
    # Fetch images
    current_img = url_to_cv2_image(current_img_url)
    previous_img = url_to_cv2_image(previous_img_url)

    # Extract metrics
    current_metrics = extract_metrics(current_img)
    previous_metrics = extract_metrics(previous_img)

    # Get weights for the species
    weights = SPECIES_WEIGHTS.get(species.lower())
    if not weights:
        raise ValueError(f"Species '{species}' not found in weight configuration.")

    # Compute deltas and score
    deltas = {}
    growth_score = 0
    for key in weights:
        prev_val = previous_metrics[key]
        curr_val = current_metrics[key]
        delta = (curr_val - prev_val) / (prev_val + 1e-5)  # Prevent division by zero
        deltas[key] = delta
        growth_score += weights[key] * delta
    
    clamped_score = max(min(growth_score, 1.0), -1.0)
    normalized_score = (clamped_score + 1) * 5

    return normalized_score, deltas