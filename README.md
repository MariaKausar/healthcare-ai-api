# AI-Powered Healthcare API System (Prototype)

## Overview
This project demonstrates a lightweight AI-enabled healthcare system designed to simulate real-time clinical decision support using API-based architecture.

The system processes patient input data and returns a risk classification, showcasing how machine learning logic can be integrated into a scalable backend service.



## Key Features
- FastAPI-based backend for high-performance API development
- RESTful API endpoints for real-time prediction
- AI-based classification logic for healthcare risk assessment
- Modular and scalable system design
- Interactive API testing via Swagger UI



## Technologies Used
- Python
- FastAPI
- Uvicorn



## System Architecture
User Input → API Endpoint → AI Processing Logic → Risk Classification Output



## How to Run

1. Clone the repository: https://github.com/MariaKausar/healthcare-ai-api.git
2. Install dependencies: python -m pip install -r requirements.txt
3. Run the API: python -m uvicorn main:app --reload
4. Open in browser:  http://127.0.0.1:8000/docs
5.  Example
       Input: Patient has tumor and fever
       Output: High Risk



## Future Improvements
- Integration with real medical datasets
- Deployment on cloud platforms (Azure/AWS)
- Advanced ML model integration (deep learning/NLP)
- Authentication and security layers



## Author
Maria Kausar
