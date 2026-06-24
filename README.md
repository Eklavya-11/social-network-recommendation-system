# social-network-recommendation-system
A mini social network recommendation system in Python

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

Recommendation system built to simulate how modern social networks suggest connections and content. 
Modular Python package with similarity scoring algorithms, automated testing, dynamic data generation, and an interactive Streamlit dashboard.

## Key Technical Features

- **Mathematical Similarity Scoring**: Utilizes **Jaccard Similarity** to calculate intersection-over-union of mutual friends and shared skills, providing a highly accurate user-to-user similarity metric.
- **Weighted Recommendation Algorithm**: Ranks potential friends based on a multi-factor weighting system 
  - 40% Mutual Connections
  - 40% Shared Skills,
  - 20% Location Proximity
- **Collaborative Filtering**: Recommends pages and content by identifying what statistically similar users interact with.
- **Dynamic Data Generation**: Includes a procedural generator (`data_generator.py`) capable of synthesizing thousands of realistic user profiles, skills, geographic locations, and networked relationships.
- **Interactive Web Interface**: A sleek frontend built with Streamlit allowing real-time exploration of user profiles, relationship networks, and live algorithm outputs.
- **Test-Driven Design**: Core algorithmic logic is validated against edge cases using `pytest`.
  
### 1. "People You May Know" (User Similarity)
Instead of simply counting mutual friends, the engine calculates a continuous similarity score `[0.0, 1.0]` between a target user and all non-connected users in the network:
```text
Similarity Score = (Jaccard(Friends) * 0.4) + (Jaccard(Skills) * 0.4) + (LocationMatch * 0.2)
```
Users are then ranked dynamically in descending order.

### 2. "Pages You Might Like" (Collaborative Filtering)
To recommend pages the user hasn't seen yet, the system aggregates the "likes" of all other users in the network, weighted by how similar those users are to the target. If a highly similar user likes a page, that page receives a massive score boost.

## Screenshots
<img width="1919" height="865" alt="image" src="img" />
