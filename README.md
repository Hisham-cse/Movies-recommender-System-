# Movies-recommender-System-


Welcome to the Movies Recommender System repository! This project leverages machine learning and Streamlit to create a user-friendly movie recommendation system.

## Features

- **Movie Recommendations**: Get personalized movie recommendations based on your favorite movie.
- **Movie Posters**: View posters of the recommended movies for a better user experience.
- **Interactive UI**: Built with Streamlit, providing an intuitive and interactive user interface.

## How It Works

1. **Select a Movie**: Choose a movie from the dropdown list.
2. **Get Recommendations**: Click the "Recommend" button to receive a list of similar movies along with their posters.
3. **View Results**: The recommended movies and their posters are displayed side by side for easy viewing.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Movies-recommender-System.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    streamlit run app.py
    ```

## Dependencies

- Streamlit
- Pandas
- Requests
- Pickle

## Usage

1. Start the Streamlit server by running the command:
    ```bash
    streamlit run app.py
    ```
2. Open the web browser and navigate to the provided local URL.
3. Select your favorite movie from the dropdown menu and click the "Recommend" button to see the recommended movies and their posters.

## Data

The movie data and similarity scores are precomputed and stored in `movies_dict.pkl` and `similarity.pkl` files. These files are loaded at runtime to provide quick recommendations.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests for any features, bug fixes, or improvements.

## License

This project is licensed under the MIT License.

---

Feel free to update this README to better fit your project's specific details and requirements.
