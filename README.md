# Image Sharpness Categorizer

The Image Sharpness Categorizer is a Python-based tool that automatically analyzes and categorizes images in a folder based on their sharpness. Using a dynamic percentage-based approach, it organizes images into "best", "better", and "med" categories, aiding in the efficient management and selection of high-quality images.

## Features

- **Sharpness Assessment**: Leverages the Laplacian variance method to evaluate the sharpness of images.
- **Dynamic Categorization**: Sorts images into categories based on configurable percentage thresholds, ensuring a balanced distribution.
- **Customizable**: Allows easy adjustment of categorization criteria through a `config.json` file.
- **User-Friendly**: Simple command-line execution with a single required argument: the path to the images folder.

## Prerequisites

Ensure you have the following prerequisites installed on your system:

- Python 3.6 or higher
- OpenCV-Python

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/charlpcronje/Image-Sharpness-Categorizer.git
cd Image-Sharpness-Categorizer
```

### Install Dependencies

After cloning the repository, install the required Python package, OpenCV-Python, using `pip`:

```bash
pip install -r requirements.txt
```

This will ensure that all dependencies needed for the tool to run are installed in your Python environment.

## Configuration

Before running the application, configure the categorization thresholds in the `config.json` file, located in the root directory of the project. The file format should be as follows:

```json
{
    "percentages": {
        "best": 20,
        "better": 20,
        "med": 20
    }
}
```

Adjust the percentage values according to your needs. These values determine the proportion of images assigned to each category based on sharpness.

## Usage

To categorize images, run the script from the command line, providing the path to the folder containing the images you want to categorize:

```bash
python app.py "<path_to_images_folder>"
```

Replace `<path_to_images_folder>` with the actual path to your folder.

## How It Works

1. **Read Configuration**: The application starts by loading the categorization thresholds from `config.json`.
2. **Calculate Sharpness**: It calculates the sharpness of each image using the Laplacian variance method.
3. **Sort and Categorize**: Images are sorted by sharpness and categorized into "best", "better", and "med" based on the configuration.
4. **Organize Images**: Categorized images are moved to respective subfolders within the original images folder.

## Contributing

Contributions to the Image Sharpness Categorizer are welcome. Please fork the repository, make your improvements, and submit a pull request with your changes.

## License

The Image Sharpness Categorizer is open-sourced under the MIT License. For more details, see the LICENSE file in the repository.