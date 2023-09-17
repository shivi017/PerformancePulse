# PerformancePulse: Insights into Test Success

Welcome to PerformancePulse, an educational data analysis project powered by Python. This project helps predict student performance based on various factors, including gender, race/ethnicity, parental education, lunch type, test preparation, reading scores, and writing scores.

## Quick Start Guide

### Prerequisites
To get started, make sure you have the following tools installed:
* Python 3.x
* Git

### Installation
Clone the Repository: Begin by cloning this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/PerformancePulse.git
Navigate to the Project Folder: Move into the project directory:

bash
Copy code
cd PerformancePulse

### Create a Virtual Environment (Optional): For better project isolation, create a virtual environment:

bash
Copy code
python -m venv venv

### Activate the Virtual Environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate

### Install Dependencies: Install the project's dependencies:

bash
Copy code
pip install -r requirements.txt

### Usage:
Run the Application: Launch the Flask application:

bash
Copy code
python app.py
Access the Web Interface: Open your web browser and go to http://localhost:5000.

### Predict Student Performance: 
Use the user-friendly web interface to input student data and receive performance predictions.

## Project Structure
* **app.py:** The heart of the application, serving the Flask web app.
* **src/:** The source code for the project.
* **pipeline/:** Components of the machine learning pipeline.
* **utils.py:** Handy utility functions.
**data_ingestion.py:** Handles data ingestion.
**data_transformation.py:** Manages data preprocessing.
**model_trainer.py: **Trains and selects the best-performing model.
**templates/:** HTML templates for the web interface.
**artifacts/:** Storage for model and preprocessor files.

### Dependencies
PerformancePulse relies on the following Python libraries:

* Flask
* Pandas
* Scikit-learn
* NumPy
* CatBoost
* XGBoost

### Core Components
**Data Ingestion**
* File: data_ingestion.py
Description: Handles the loading of raw data, conducts train-test splitting, and saves data as CSV files for training and testing.
**Data Transformation**
* File: data_transformation.py
Description: Prepares data by addressing missing values, scaling numerical features, and one-hot encoding categorical attributes. It also saves the preprocessing object for future predictions.
**Model Trainer**
* File: model_trainer.py
Description: Trains a variety of regression models (e.g., Random Forest, XGBoost) on the preprocessed data. The best-performing model is selected and saved for future predictions.
**Custom Data Classes**
* File: custom_data.py
Description: Contains custom data classes to structure input data.
**Exception Handling**
* File: exception.py
Description: Provides custom exception handling for the project.
**Logging**
* File: logger.py
Description: Sets up project logging for better debugging and monitoring.

## Contributing
Contributions to this project are encouraged! If you'd like to contribute, follow these steps:

* Fork the repository.
* Create a new branch for your feature or bug fix.
* Make your changes and commit them with clear and concise messages.
* Push your changes to your fork.
* Open a pull request to the main repository.
