import numpy as np
import cv2
import json, os
import pandas as pd
from typing import List, Tuple, Dict


def draw_annotations(bboxes: List[Dict], image_width: int, image_height: int) -> Tuple[np.ndarray, List[int]]:
        for bbox in bboxes:
            # Convert float coordinates to integers
            x_min, y_min = int(round(bbox['x'])), int(round(bbox['y']))
            width, height = int(round(bbox['width'])), int(round(bbox['height']))
            if bbox['class_name'] == 'ruler':    
                w , h = min(width,height), max(width,height)
                angle = bbox['rotate']

                # Define the original points of the rectangle
                points = np.array([[x_min, y_min],
                    [x_min + h, y_min],
                    [x_min + h, y_min + w],
                    [x_min, y_min + w]], dtype="float32")
                
                # Convert the angle to radians
                theta_rad = np.deg2rad(angle)

                # Create the rotation matrix
                R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                            [np.sin(theta_rad), np.cos(theta_rad)]])

                # Translate points to the origin (center), apply rotation, and translate back
                rotated_points = np.dot(points - [x_min, y_min], R.T) + [x_min, y_min]

                # Convert the rotated points to integer format for OpenCV
                rotated_points_int = rotated_points.astype("int32")
            
            
                # Draw the rotated rectangle
                cv2.polylines(image, [rotated_points_int], isClosed=True, color=(0, 255, 0), thickness=2)

            else:
                w , h = width,height
                angle = bbox['rotate']

                # Define the original points of the rectangle
                points = np.array([[x_min, y_min],
                    [x_min + w, y_min],
                    [x_min + w, y_min + h],
                    [x_min, y_min + h]], dtype="float32")
                
                # Convert the angle to radians
                theta_rad = np.deg2rad(angle)

                # Create the rotation matrix
                R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                            [np.sin(theta_rad), np.cos(theta_rad)]])

                # Translate points to the origin (center), apply rotation, and translate back
                rotated_points = np.dot(points - [x_min, y_min], R.T) + [x_min, y_min]

                # Convert the rotated points to integer format for OpenCV
                rotated_points_int = rotated_points.astype("int32")
                # Draw the rectangle that represent 1mm scale
                cv2.polylines(image, [rotated_points_int], isClosed=True, color=(0, 0, 255), thickness=2)
                # Calculate the maximum side length
                max_side = max(width, height)
                
        output_path = f"annotated_examples/{image_path.split('/')[-1].split('.')[0]}_annotated.png"
        cv2.imwrite(output_path, image)
        return image, max_side


if __name__ == "__main__":
    images_path = "example_data/"
    csv_file = "annotation_example.csv"
    annotations = pd.read_csv(csv_file)
    for _, row in annotations.iterrows():
        # Load data of the image from annotation file
        image_name = row['image_path_local']
        image_path = os.path.join(images_path,image_name)
        image_width, image_height = int(row['image_width']), int(row['image_height'])
        bboxes = json.loads(row['view_annotation_result_Bounding-Box'].replace("'", "\""))
        image = cv2.imread(image_path)
    
        # Draw annotations on the image and get max sides
        annotated_image, max_side = draw_annotations(bboxes, image_width, image_height)