# ✈️ AI Travel Planner with ChatGPT

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)
![OpenAI](https://img.shields.io/badge/API-OpenAI-412991)

An intelligent travel itinerary generator powered by ChatGPT API, featuring:

- **Personalized trip planning** based on budget and interests
- **AI-powered recommendations** for activities and dining
- **Secure API key management** using environment variables
- **Responsive web interface** built with Streamlit

## 🏗️ Architecture

```mermaid
%% AI Travel Planner Architecture
flowchart TD
    A[User] -->|Input Parameters| B[Streamlit UI]
    B -->|Trigger| C[TravelPlanner Class]
    C -->|Read API Key| D[.env File]
    C -->|Call API| E[OpenAI ChatGPT]
    E -->|Return Response| C
    C -->|Generate| F[Travel Itinerary]
    F -->|Display| B

    subgraph Frontend
        B
    end

    subgraph Backend
        C
        D
    end

    subgraph Cloud
        E
    end

    style A fill:#ff9,stroke:#333
    style B fill:#aaf,stroke:#333
    style C fill:#6f6,stroke:#333
    style D fill:#ff6,stroke:#333
    style E fill:#f66,stroke:#333
    style F fill:#6ff,stroke:#333
