import os
import argparse
from pathlib import Path

def generate_train_val_txt(train_img_path, val_img_path, output_dir="./"):
    """
    Generate train.txt and val.txt files for YOLO training
    
    Args:
        train_img_path: Path to training images directory
        val_img_path: Path to validation images directory
        output_dir: Directory to save train.txt and val.txt files
    """
    
    # Supported image extensions
    img_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff'}
    
    # Generate train.txt
    train_txt_path = os.path.join(output_dir, 'train.txt')
    with open(train_txt_path, "w") as f:  # Use "w" instead of "a+" to overwrite
        if os.path.exists(train_img_path):
            img_list = os.listdir(train_img_path)
            img_list = [img for img in img_list if Path(img).suffix.lower() in img_extensions]
            img_list.sort()  # Sort for consistency
            
            for img in img_list:
                # Use absolute path and fix the newline placement
                img_path = os.path.abspath(os.path.join(train_img_path, img))
                f.write(img_path + "\n")
            
            print(f"Train.txt created with {len(img_list)} images")
        else:
            print(f"Error: Training image path '{train_img_path}' does not exist!")
    
    # Generate val.txt
    val_txt_path = os.path.join(output_dir, 'val.txt')
    with open(val_txt_path, "w") as f:  # Use "w" instead of "a+" to overwrite
        if os.path.exists(val_img_path):
            img_list = os.listdir(val_img_path)
            img_list = [img for img in img_list if Path(img).suffix.lower() in img_extensions]
            img_list.sort()  # Sort for consistency
            
            for img in img_list:
                # Use absolute path and fix the newline placement
                img_path = os.path.abspath(os.path.join(val_img_path, img))
                f.write(img_path + "\n")
            
            print(f"Val.txt created with {len(img_list)} images")
        else:
            print(f"Error: Validation image path '{val_img_path}' does not exist!")

def main():
    parser = argparse.ArgumentParser(description='Generate train.txt and val.txt for YOLO training')
    parser.add_argument('--train-img-path', type=str, required=True, 
                       help='Path to training images directory')
    parser.add_argument('--val-img-path', type=str, required=True,
                       help='Path to validation images directory')
    parser.add_argument('--output-dir', type=str, default='./',
                       help='Directory to save train.txt and val.txt files')
    
    args = parser.parse_args()
    
    generate_train_val_txt(args.train_img_path, args.val_img_path, args.output_dir)

if __name__ == '__main__':
    main()