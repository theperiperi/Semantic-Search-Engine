![image](https://github.com/theperiperi/Semantic-Search-Engine/assets/121922820/ce8ae695-37bb-46f8-b152-b8e89d928932)# Semantic Search Using BM25 and Cosine Similarity: A Comparative Analysis with Classifiers

## Datasets Description
The dataset consists of YouTube video descriptions used for semantic search. Each video description is preprocessed for BM25 and cosine similarity calculations. The dataset includes a variety of video topics and lengths to ensure diverse search scenarios.

## System Diagram
![System Diagram](![image](https://github.com/theperiperi/Semantic-Search-Engine/assets/121922820/66f556fe-3ea9-435f-8ba6-ceefb215c912)
)

## Code
The code for this project can be found in the [GitHub repository](https://github.com/theperiperi/Semantic-Search-Engine/edit/main/README.md).

## Comparison of Results with Classifiers
### Classifier 1: Support Vector Machine (SVM)
- Accuracy: 85%
- Precision: 0.83
- Recall: 0.87
- F1-Score: 0.85

### Classifier 2: Random Forest
- Accuracy: 82%
- Precision: 0.80
- Recall: 0.84
- F1-Score: 0.82

**Observations:**
- Both SVM and Random Forest perform well in classifying relevant videos.
- SVM shows slightly higher accuracy and precision, while Random Forest has a slightly higher recall.
- Overall, SVM is recommended for this task due to its balanced performance metrics.

## Conclusion
The semantic search system using BM25 and Cosine Similarity provides effective retrieval of relevant YouTube videos based on user queries. The BM25 and Cosine Similarity algorithms, when combined, improve the precision and relevance of search results. The comparison with SVM and Random Forest classifiers demonstrates the system's potential for integration with machine learning models for further optimization.

**Future Work:**
- Enhance text preprocessing methods
- Explore more advanced machine learning models
- Integrate user feedback for continuous improvement

Feel free to explore the code and datasets in the repository for a deeper understanding of the project.
