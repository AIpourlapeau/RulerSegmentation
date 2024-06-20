# RulerSegmentation test set

[RulerSegmentation dataset](https://path/to/images)

## Dataset Description
This dataset contains a collection of annotated dermoscopic images primarily used for identifying and segmenting rulers and scales within these images. The annotations are provided in a CSV file, which includes details such as image dimensions and bounding boxes for each annotation, as well as the origin source for the public images. Below is a detailed description of the dataset's structure and contents.
The of the dataset contains 100 images, and corresponds to the whole test set of the algorithm described on the paper.  **For now, we only published a sample of the annotations, but the whole dataset will be published after acceptation of our paper.**

## Dataset Structure
- **"images"**: The dataset contains dermoscopic images with varying resolutions and dimensions.
- **"annotation"**: Each image is accompanied by annotation data that identifies the locations of rulers and scales within the image. These annotations are represented as bounding boxes with specific coordinates and dimensions.

### Annotation CSV File: 
The CSV file has the following columns:

1. `image_path_local`: The local path to the image file.
2. `image_width`: The width of the image in pixels.
3. `image_height`: The height of the image in pixels.
4. `discussions`: A column reserved for any discussions or notes about the annotations (currently empty).
5. `view_annotation_result_Bounding-Box`: A JSON-formatted string containing a list of dictionaries. Each dictionary represents a bounding box with the following keys:
  * x: The x-coordinate of the bounding box center.
  * y: The y-coordinate of the bounding box center.
  * width: The width of the bounding box.
  * height: The height of the bounding box.
  * rotate: The rotation angle of the bounding box.
  * class_name: The class of the annotated object (e.g., "ruler", "scale").

### Example of Annotation Data
Below are examples of the annotations for two images from the dataset:

- *Example 1*
```
"image_path_local": "Claire_Aless1.jpg"
"image_width": 1932
"image_height": 1449
"discussions": ""
"view_annotation_result_Bounding-Box": "[{'x': 1063.7311537501948, 'y': 297.54852676079395, 'width': 200.24773574690806, 'height': 6.762622219149231, 'rotate': 269.87563516349496, 'class_name': 'ruler'}, ...]"

```
- *Example 2*
```
"image_path_local": "JLP_wruler2.jpg"
"image_width": 1920
"image_height": 1080
"discussions": ""
"view_annotation_result_Bounding-Box": "[{'x': 1021.3929287528508, 'y': 826.535968299397, 'width': 60.26069886280168, 'height': 2.1821350218130195, 'rotate': 326.66664926435146, 'class_name': 'ruler'}, ...]"
```

### Notable Annotations

- **"Rulers"**: Identified by their characteristic elongated shapes and usually annotated with their orientation and dimensions.
- **"Scales"**: Annotated similarly to rulers but distinguished by their specific use-case and potentially different dimensions or orientations.


The file `draw_ruler_annotation.py` is one example of how to plot the ruler lines and the scales on the images. In the folder *examples/*, we provide samples of annotated images (in green the ruler lines and in red the rectangle which heigt corresponds to the 1 mm scale of the image).

<img title="a title" alt="ISIC.jpg" src="examples/Claire_Aless7_annotated.png"  width="500"> 
