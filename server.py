from flask import Flask, request, jsonify
from flask_cors import CORS
import googleapiclient.discovery
from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Your YouTube API key
API_KEY = "AIzaSyDTqLWARQ2OlS4hBKucFWacXyh9tVjDrsY"

# Initialize the YouTube API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

def fetch_videos(query):
    """
    Fetches YouTube videos based on a search query.
    """
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=10  # You can adjust the number of results
    )
    response = request.execute()
    videos = []
    for item in response['items']:
        videos.append({
            'title': item['snippet']['title'],
            'description': item['snippet']['description']
        })
    return videos

def preprocess_text(text):
    """
    Preprocesses text for BM25 and cosine similarity.
    """
    # You can add more advanced text preprocessing steps here
    return text.lower().split()

def semantic_search(user_query, videos):
    """
    Performs semantic search using BM25 and cosine similarity.
    """
    # BM25 ranking
    corpus = [preprocess_text(video['description']) for video in videos]
    bm25 = BM25Okapi(corpus)

    # BM25 scores
    query = preprocess_text(user_query)
    scores = bm25.get_scores(query)

    # TF-IDF vectorization for cosine similarity
    count_vectorizer = CountVectorizer(stop_words='english', tokenizer=lambda x: x, lowercase=False)
    tfidf_transformer = TfidfTransformer()
    video_descriptions = [' '.join(preprocess_text(video['description'])) for video in videos]
    count_matrix = count_vectorizer.fit_transform(video_descriptions)
    tfidf_matrix = tfidf_transformer.fit_transform(count_matrix)
    query_vec = count_vectorizer.transform([query])
    query_tfidf = tfidf_transformer.transform(query_vec)
    similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

    # Combine scores
    combined_scores = 0.6 * scores + 0.4 * similarities  # Weighted sum

    # Sort videos by combined score
    sorted_indices = combined_scores.argsort()[::-1]

    # Return sorted videos based on combined score
    sorted_videos = [(videos[i]['title'], videos[i]['description'], combined_scores[i]) for i in sorted_indices]
    return sorted_videos

@app.route('/')
def index():
    """
    Serve the index.html file.
    """
    return app.send_static_file('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    """
    Endpoint to handle search requests.
    """
    data = request.get_json()
    query = data['query']
    
    try:
        videos = fetch_videos(query)
        results = semantic_search(query, videos)
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
