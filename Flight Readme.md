

# Flight Price Prediction Project

This project aims to predict the prices of flights for various cities in India using machine learning algorithms. The prediction models are trained on historical flight data to forecast future prices accurately.

## Algorithms Used
- CatBoost Algorithm
- XGBoost
- Extra Trees Regressor

## Tools and Technologies
- Python
- Scikit-learn
- CatBoost
- XGBoost
- PyCharm (for web-based application development)

## Project Structure
- **data/**: Contains the dataset used for training and testing the prediction models.
- **models/**: Stores the trained machine learning models.
- **src/**: Source code for the flight price prediction application.
  - **train_model.py**: Python script to train the prediction models.
  - **predict.py**: Python script to make predictions using the trained models.
  - **app.py**: Main Flask application for the web-based flight price prediction interface.
  - **templates/**: HTML templates for the web application.
  - **static/**: Static files (e.g., CSS, JavaScript) for the web application.

## Usage
1. **Training the Models**:
   - Run `train_model.py` to train the machine learning models using the provided dataset.
   - Models will be saved in the `models/` directory.

2. **Making Predictions**:
   - Use `predict.py` to make predictions on new flight data.
   - Provide the required input features to get the predicted flight prices.

3. **Running the Web Application**:
   - Start the Flask application by running `app.py`.
   - Access the web interface in your browser to interactively predict flight prices.

## Dependencies
- numpy
- pandas
- scikit-learn
- catboost
- xgboost
- flask
- flask_cors

Install the dependencies using `pip install -r requirements.txt`.

## Contributors
- Umer Abbasi

Feel free to contribute to this project by submitting pull requests or reporting issues.


## Authors

- [@Umer Abbasi](https://www.github.com/umerabbasi658)

