# Movie Recommendation System

This project is a simple Movie Recommendation System using Collaborative Filtering. The system recommends movies to users based on the similarity between users' movie ratings.

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mohamedbenhasan1/Encryptix/Task_4.git
```
2. Navigate to the project directory:
```bash
cd Task_4
```
3. Install the required packages:
```bash
pip install pandas numpy scikit-learn
```
4. Run the script:
```bash
python Rsys.py
```
## Dataset
The dataset used in this project consists of two CSV files:

- ratings.csv: Contains user ratings for movies.
- movies.csv: Contains movie information.
You can download the dataset from the ` MovieLens dataset `. For simplicity, this project uses the `ml-latest-small` version of the dataset.
## Usage
1. Place the ratings.csv and movies.csv files in the project directory
2. Run the code
## How It Works
1. Load the Dataset: The `ratings.csv` and `movies.csv` files are loaded into pandas DataFrames.

2. Data Preprocessing: A user-item matrix is created where rows represent users and columns represent movies. The matrix is filled with user ratings, and NaN values are replaced with 0.

3. Calculate Similarity: Cosine similarity is calculated between users to create a user similarity matrix.

4. Generate Recommendations: For a given user, the system finds the most similar users and recommends movies based on the average ratings given by these similar users.
## License
This project is licensed under the MIT License.
## Acknowledgements
This project uses the MovieLens dataset provided by GroupLens.
## Author
Mohamed Benhasan
