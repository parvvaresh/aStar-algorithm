# Hoda Dataset Reader & CNN Digit Recognizer

This notebook demonstrates how to read and process the Hoda dataset (a Persian handwritten digits dataset) using a custom reader and then train a simple CNN with PyTorch to perform digit recognition.

## Features

- **Data Reading**: Implements functions to parse the Hoda dataset's CDB files.
- **Image Processing**: Resizes, normalizes, and binarizes the images.
- **Data Visualization**: Displays sample images and their labels.
- **Model Training**: Trains a Convolutional Neural Network (CNN) on the training data.
- **Evaluation**: Evaluates the trained model on the test set.

## Requirements

- Python 3.x
- [PyTorch](https://pytorch.org/)
- [Torchvision](https://pytorch.org/vision/stable/index.html)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/) (for visualization)
- Git (to clone the [HodaDatasetReader](https://github.com/amir-saniyan/HodaDatasetReader) repository)

## Setup and Usage

1. **Clone the Repository**  
   The notebook uses `!git clone` to download the HodaDatasetReader. This step is executed automatically in the notebook.

2. **Dataset Files**  
   Ensure that the dataset files (`Train 60000.cdb`, `Test 20000.cdb`, and `RemainingSamples.cdb`) are available in a folder named `DigitDB` in the notebook's working directory.

3. **Run the Notebook**  
   - Open the notebook in [Google Colab](https://colab.research.google.com/).
   - Run all cells sequentially.
   - The notebook reads the dataset, preprocesses the images, visualizes samples, trains the CNN, and finally evaluates the model on the test data.

4. **Model Training and Evaluation**  
   - The CNN is defined using PyTorch.
   - The training loop uses the Adam optimizer and Cross Entropy Loss.
   - After training for 10 epochs, the model's accuracy on the test set is printed.

## Customization

- **Image Size**: You can adjust the target image size by modifying the `images_height` and `images_width` parameters.
- **Model Architecture**: The CNN architecture can be changed by editing the `CNN` class.
- **Training Parameters**: Modify the number of epochs, batch size, or learning rate to experiment with different training settings.

