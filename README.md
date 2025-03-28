# Hoda Dataset Reader & CNN Digit Recognizer

This Google Colab notebook demonstrates how to read and preprocess the Hoda handwritten digits dataset, train a Convolutional Neural Network (CNN) using PyTorch, and evaluate its performance. A trained model is saved at the end of the notebook.

## Features

- **Data Loading & Preprocessing**  
  Reads the Hoda dataset (CDB files), resizes, normalizes, and binarizes the images.

- **Data Visualization**  
  Displays sample images with their corresponding labels.

- **CNN Model**  
  Defines a CNN with two convolutional blocks (each with batch normalization, pooling, and dropout) followed by two fully connected layers.

- **Training & Evaluation**  
  - The model was trained for 15 epochs with the Adam optimizer and Cross Entropy Loss.
  - **Training Loss:**  
    - Epoch 1: 0.16766  
    - Epoch 2: 0.07790  
    - Epoch 3: 0.05842  
    - Epoch 4: 0.04947  
    - Epoch 5: 0.04059  
    - Epoch 6: 0.03726  
    - Epoch 7: 0.03220  
    - Epoch 8: 0.02918  
    - Epoch 9: 0.02811  
    - Epoch 10: 0.02485  
    - Epoch 11: 0.02318  
    - Epoch 12: 0.02107  
    - Epoch 13: 0.01879  
    - Epoch 14: 0.01641  
    - Epoch 15: 0.01799
  - **Test Accuracy:** 99.24%

- **Model Saving & Download**  
  The trained model is saved as `CNN_Digit_Recognizer.pth`.  
  You can download the model from [this link](https://your-model-download-link.com).

## Requirements

- Python 3.x
- [PyTorch](https://pytorch.org/)
- [Torchvision](https://pytorch.org/vision/stable/index.html)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- Git (to clone the [HodaDatasetReader](https://github.com/amir-saniyan/HodaDatasetReader) repository)

## Setup and Usage

1. **Clone the Repository**  
   The notebook automatically clones the HodaDatasetReader repository using:
   ```bash
   !git clone https://github.com/amir-saniyan/HodaDatasetReader
   ```
   Make sure the dataset files (`Train 60000.cdb`, `Test 20000.cdb`, and `RemainingSamples.cdb`) are in the `DigitDB` folder.

2. **Run the Notebook**  
   - Open the notebook in [Google Colab](https://colab.research.google.com/).
   - Run all cells sequentially to load the data, visualize samples, train the CNN, and evaluate its performance.
   - The final cell saves the trained model.

3. **Download the Trained Model**  
   After training, download the saved model (`CNN_Digit_Recognizer.pth`) from [this link](https://your-model-download-link.com).

## Customization

- **Image Dimensions:**  
  Change `images_height` and `images_width` parameters to adjust the input image size.
- **Model Architecture:**  
  Modify the `CNN` class if you wish to experiment with different network configurations.
- **Training Parameters:**  
  Tweak the number of epochs, batch size, or learning rate to explore different training setups.

## License

This project is provided as-is without any warranty. You may modify and use it for educational or research purposes.
