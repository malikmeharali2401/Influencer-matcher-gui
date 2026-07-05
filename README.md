# Influencer Partnership Matcher

## Project Overview
This project was developed as part of my Week 1 AI/ML internship tasks. The primary goal is to solve a common marketing problem: helping brands accurately match with the most relevant social media influencers without manual, time-consuming searching.

The application features a fully interactive Graphical User Interface (GUI) built with **PyQt5** and implements a **Similarity Matching Algorithm** to process data-backed campaign pairing decisions.

## Features
* **Niche Filtering:** Instantly filters out candidates that do not align with the brand's targeted industry category (e.g., Tech, Fitness, Fashion).
* **Feature Normalization:** Normalizes diverse data points (large follower counts vs. small decimal engagement percentages) to ensure fair mathematical weight during calculations.
* **Euclidean Distance Engine:** Computes the direct geometric proximity between a brand's exact ideal targets and the influencer's real-world metrics.
* **Dynamic Sorting:** Renders a clean, organized table view displaying real-time match scores from 0% to 100%, sorted from the highest match down.

## Technical Stack
* **Language:** Python
* **GUI Framework:** PyQt5
* **Algorithm:** Multi-dimensional Proximity Similarity Matching (Euclidean Distance)

## How to Run
1. Install the required dependencies:
   ```bash
   pip install PyQt5
