import os
import random
import shutil
from pathlib import Path
import argparse

def split_data(images_path, labels_path, output_dir, train_ratio=0.8):
    """
    Split data into train and validation sets
    
    Args:
        images_path: Path to directory containing images
        labels_path: Path to directory containing labels
        output_dir: Path to output directory
        train_ratio: Ratio of training data (default: 0.8)
    """
    # Create output directories
    os.makedirs(f"{output_dir}/images/train", exist_ok=True)
    os.makedirs(f"{output_dir}/images/val", exist_ok=True)
    os.makedirs(f"{output_dir}/labels/train", exist_ok=True)
    os.makedirs(f"{output_dir}/labels/val", exist_ok=True)
    
    # Get all image files
    image_files = [f for f in os.listdir(images_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Shuffle the files
    random.seed(42)  # Set seed for reproducibility
    random.shuffle(image_files)
    
    # Calculate split point
    split_idx = int(len(image_files) * train_ratio)
    train_files = image_files[:split_idx]
    val_files = image_files[split_idx:]
    
    print(f"Total images: {len(image_files)}")
    print(f"Training images: {len(train_files)}")
    print(f"Validation images: {len(val_files)}")
    
    # Copy training files
    for file in train_files:
        # Copy image
        shutil.copy(
            os.path.join(images_path, file),
            os.path.join(output_dir, "images/train", file)
        )
        
        # Copy corresponding label (assuming same name with .txt extension)
        label_file = os.path.splitext(file)[0] + ".txt"
        if os.path.exists(os.path.join(labels_path, label_file)):
            shutil.copy(
                os.path.join(labels_path, label_file),
                os.path.join(output_dir, "labels/train", label_file)
            )
        else:
            print(f"Warning: Label file not found for {file}")
    
    # Copy validation files
    for file in val_files:
        # Copy image
        shutil.copy(
            os.path.join(images_path, file),
            os.path.join(output_dir, "images/val", file)
        )
        
        # Copy corresponding label
        label_file = os.path.splitext(file)[0] + ".txt"
        if os.path.exists(os.path.join(labels_path, label_file)):
            shutil.copy(
                os.path.join(labels_path, label_file),
                os.path.join(output_dir, "labels/val", label_file)
            )
        else:
            print(f"Warning: Label file not found for {file}")
    
    # Create a classes.txt file in the output directory
    with open(os.path.join(output_dir, "classes.txt"), "w") as f:
        f.write("led_on\nmotherboard")
    
    print(f"Data split complete. Files saved to {output_dir}")
    return len(train_files), len(val_files)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split dataset into train and validation sets')
    parser.add_argument('--images', type=str, required=True, help='Path to directory containing images')
    parser.add_argument('--labels', type=str, required=True, help='Path to directory containing labels')
    parser.add_argument('--output', type=str, required=True, help='Path to output directory')
    parser.add_argument('--ratio', type=float, default=0.8, help='Train ratio (default: 0.8)')
    
    args = parser.parse_args()
    
    split_data(args.images, args.labels, args.output, args.ratio)