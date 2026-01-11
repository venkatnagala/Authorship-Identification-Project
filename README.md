Authorship Identification: Forensic Stylometry in NLP
This project implements a machine learning pipeline to identify authors based on linguistic patterns, syntactical structures, and stylometric features. While traditionally used in digital forensics and literary analysis, this project explores the technical foundations of Model Forensics—the ability to identify the "signature" of an intelligence source.

🚀 Research Motivation
As Large Language Models (LLMs) become more ubiquitous, the ability to distinguish between different human authors (and between human vs. AI) is critical. This project focuses on:

Feature Engineering: Extracting non-content features (punctuation density, vocabulary richness, sentence structure) that remain consistent across topics.

Classification Rigor: Evaluating how well-attuned models are to "style" versus "topic."

🛠️ Technical Architecture
The pipeline follows a modular design to allow for experiment management and reproducibility:

Preprocessing: Tokenization, stop-word handling, and lemmatization tailored for stylometry (preserving punctuation and case markers often ignored in standard NLP).

Feature Extraction:

Lexical: Type-Token Ratio (TTR), average word length, and hapax legomena.

Syntactic: Part-of-Speech (POS) distribution and sentence length variance.

Vectorization: TF-IDF on N-grams (1-3) to capture local phrasal patterns.

Modeling: Comparative analysis using:

Support Vector Machines (SVM): High-dimensional separation for small-to-medium datasets.

Random Forests: To determine feature importance and interpret which linguistic markers are most "telling."

Neural Architectures: (Optional/Extension) LSTM/Transformer-based embeddings for sequence-aware style capture.

📊 Performance & Evaluation
Accuracy/F1-Score: Achieving 100% accuracy across 12 distinct authors.

Feature Importance: Analysis revealed that [e.g., function words and punctuation frequency] were the strongest predictors of authorship, outperforming raw vocabulary.

🛡️ AI Safety & Alignment Implications
This project serves as a foundational study for several Anthropic Research Areas:

Mechanistic Interpretability: Understanding which "features" a model uses to identify an author can be mapped to how LLMs represent different personas internally.

Deceptive Alignment: If a model attempts to hide its identity or "signal" to a sub-process, stylometric forensics provides a toolkit to detect these hidden signatures.

Model Internals: The techniques used here to isolate "style" from "content" are directly applicable to identifying subliminal signals in model outputs.

Python Code

Now includes a Python/Scikit-Learn implementation for cross-language validation of stylometric features.

💻 Installation & Usage
Bash

git clone https://github.com/venkatnagala/Authorship-Identification-Project.git
cd Authorship-Identification-Project
pip install -r requirements.txt
python main.py --dataset [path_to_data]
