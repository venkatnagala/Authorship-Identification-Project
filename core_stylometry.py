import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

def train_authorship_model(texts, labels):
    """
    Demonstrates forensic stylometry: Using Character N-Grams to capture 
    author-specific punctuation and syntax patterns (Style over Content).
    """
    # We use char n-grams (2-5) to capture sub-word patterns and punctuation
    # which are more 'author-invariant' than word-choice alone.
    stylometry_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(2, 5), max_features=5000)),
        ('classifier', SVC(kernel='linear', probability=True))
    ])

    # Fit the model: Separating the 'stylistic manifold' of different authors
    model = stylometry_pipeline.fit(texts, labels)
    
    return model

# Example usage for a research demo
if __name__ == "__main__":
    sample_texts = ["The quick brown fox...", "It was the best of times..."]
    sample_labels = ["Author_A", "Author_B"]
    clf = train_authorship_model(sample_texts, sample_labels)
    print(f"Model trained with {len(clf.named_steps['tfidf'].get_feature_names_out())} stylistic features.")
