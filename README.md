# Question answering SQuAD 2.0.
## Final Project (Group 7)
### Data Science, Columbian College of Arts & Science, George Washinton University
### Cody Yu, Pon Swarnalaya Ravichandran, Ei Tanaka

## Overview
Our goal is to develop a system that can efficiently and accurately provide answers to factoid questions, harnessing the strengths of both IR-based and knowledge-based approaches by using two models BERT and ELECTRA 

## Project Structure
- `Code`: Contains all code files including data preprocessing and model training scripts. (Details in the Code folder)
- `Group-Project-Proposal`: Initial project proposal outlining the objectives and methodology.
- `Final-Group-Project-Presentation`: Presentation slides detailing the project findings and results.
- `Final-Group-Project-Report`: Comprehensive report including detailed analysis, results, and discussions.
- `Individual-Project-Reports`: Contributions and reports from each team member.

## Installation and Usage

1. **Clone the Repository**:
   To start working with the project, clone it from GitHub using the following command:
   ```bash
   Git clone https://github.com/eitanaka/NLP_Final_Project_Group7.git

2. **Fine-Tuning the ELECTRA**:
   The train_ELECTRA.py script is designed to fine-tune the ELECTRA model for the task of question answering using the SQuAD 2.0 dataset. This script handles the entire process from data preprocessing to training and evaluating the model.
**Prerequisites**
   Before running the script, ensure you have the following prerequisites installed:
   - Python 3.6 or later
   - PyTorch
   - Transformers library
   - Datasets library
   - Accelerate library
   - Seaborn and Matplotlib for visualization (optional)
   - tqdm for progress bars
   You can install these prerequisites using pip:
   ```bash
   pip install torch transformers datasets accelerate seaborn matplotlib tqdm

**Script Usage**   
   1. Navigate to the Script Directory: Make sure you are in the directory containing the train_ELECTRA.py script.
   2. Set Up Parameters (Optional): You can modify the script to change parameters like max_length, stride, learning_rate, etc., according to your requirements.
   3. Run the Script: Execute the script using the following command:
   ```bash
   python train_ELECTRA.py
   ```

   4. 
   This will start the training process of the ELECTRA model on the SQuAD 2.0 dataset. The script handles the following:

Data loading and preprocessing: Tokenizes the SQuAD dataset and prepares it for training.
Model initialization: Loads the ELECTRA model pre-trained on the Google ELECTRA base discriminator.
Training: Fine-tunes the model on the prepared dataset.
Evaluation: Evaluates the model on the validation set.
   
5. **Fine-Tuning the BERT with LoRA**:

6. **Play with the streamlit app**
   To start working with the streamlit, make sure to install streamlit
   ```bash
   pip install streamlit

## Contributors
- Cody Yu
- Pon swarnalaya Ravichandran
- Ei Tanaka

# License
(add only if applicable)

# Acknowledgments
(Acknowledgments to people, resources, or institutions)

For more details, please refer to individual files and folders.

   
