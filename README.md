# Streaming at Scale - MLOps

![Architecture Diagram](docs/images/streamingatscale.png)

## Introduction

Streaming at Scale - MLOps is a project focused on deploying machine learning models at scale while addressing operational challenges such as dead letter queues, autoscaling, right fitting, and FILEIO issues. It provides a robust architecture for deploying and managing machine learning pipelines in production environments.

## Purpose of the Project

In the rapidly evolving landscape of AI, the advent of platforms like OpenAI has significantly democratized the process of building machine learning models. However, despite the accessibility of model development, the true litmus test lies in the seamless deployment and management of these models in real-world production environments.

The core objective of this project transcends mere model creation; it is fundamentally about navigating the intricate challenges of deploying machine learning solutions at scale. By strategically focusing on addressing operational hurdles and meticulously sculpting architectural blueprints, the aim is to forge a robust and adaptable framework. This framework not only ensures the reliable deployment of machine learning models but also fosters scalability and sustainability in the face of evolving business demands.

The commitment extends beyond the realm of theoretical prowess; the aspiration is to deliver a pragmatic solution that empowers individuals and organizations to harness the full potential of machine learning technology. Through relentless dedication to innovation and a keen understanding of industry best practices, the goal is to redefine the paradigm of machine learning deployment and usher in a new era of transformative capabilities.

## Technical Details

### Dead Letter Queues (Lost Streaming Data)

- Utilizes dead letter queues to capture and handle lost streaming data. Messages that fail to be processed are sent to a dead letter queue for analysis and troubleshooting.

### Autoscaling (Vertical and Horizontal)

- Implements both vertical and horizontal autoscaling techniques to dynamically adjust computing resources based on workload demand. Vertical autoscaling involves increasing or decreasing EC2 instance sizes, while horizontal autoscaling adds or removes EC2 instances from the deployment.

### Right Fitting (Optimizing Resource Allocation)

- Applies the concept of right fitting to optimize resource allocation at each step of the machine learning pipeline. By dynamically allocating resources based on workload characteristics, it ensures optimal performance and cost efficiency.

### FILEIO (Handling Large Data Streams)

- Proactively addresses FILEIO issues by monitoring data size and raising alerts when data exceeds predefined thresholds. This helps prevent performance degradation and runtime failures due to data size limitations.

### Model Persistence and Portability
- **Artifact Storage**: Save both the preprocessor and trained model as pickle files, ensuring the encapsulation of the entire model pipeline for easy storage and retrieval.
- **Portable Artifacts**: Dockerize the model artifacts along with the Flask web service, facilitating consistent deployment across different environments and platforms.

### Scalable Deployment with Docker and Elastic Beanstalk
- **Containerization**: Utilize Docker containers for packaging the Flask web service and associated model artifacts, ensuring consistent runtime environments and streamlined deployment processes.
- **Elastic Beanstalk Integration**: Deploy the Dockerized application on AWS Elastic Beanstalk, enabling seamless scaling and management of resources based on demand.

### Real-Time Prediction and Result Display
- **Predictive Analytics**: Enable users to receive real-time predictions from the machine learning model based on their submitted data, providing valuable insights and decision support.
- **Result Visualization**: Display predicted results to users in an easily interpretable format, fostering user engagement and enhancing the utility of the application.

### Continuous Integration and Deployment (CI/CD)
- **Automated Pipelines**: Implement CI/CD pipelines to automate the testing, building, and deployment processes, ensuring rapid iteration and delivery of updates to the production environment.
- **Version Control**: Utilize version control systems such as Git to track changes and manage collaborative development efforts, promoting code quality and reliability.



## Features

- **User-friendly Interface**: The frontend provides a simple and intuitive user interface for interacting with the machine learning model.
  
- **Backend Web Service**: The backend is built with Flask and is responsible for handling user requests, processing data, and returning predictions from the machine learning model.
  
- **Integration with Machine Learning Model**: The backend integrates with a machine learning model to provide predictions based on user input.
  
- **Form Submission**: Users can submit entries through a form on the frontend, and the backend returns predictions based on the input data.

## Project Structure

```
├─ README.md
└─ scaling-mlops
   ├─ .git
   ├─ .gitignore
   ├─ .gitmodules
   ├─ .pytest_cache
   ├─ backend
   │  ├─ .pytest_cache
   │  │  ├─ .gitignore
   │  │  ├─ CACHEDIR.TAG
   │  │  ├─ README.md
   │  ├─ classification
   │  │  ├─ code
   │  │  │  ├─ 14-explore-more.md
   │  │  │  ├─ notebook-scaling-ohe.ipynb
   │  │  │  └─ notebook.ipynb
   │  │  ├─ data
   │  │  │  ├─ meta.csv
   │  │  │  └─ meta.json
   │  │  └─ README.md
   │  ├─ deployment
   │  │  ├─ code
   │  │  │  ├─ .gitignore
   │  │  │  ├─ 05-train-churn-model.ipynb
   │  │  │  ├─ Dockerfile
   │  │  │  ├─ model_C=1.0.bin
   │  │  │  ├─ ping.py
   │  │  │  ├─ Pipfile
   │  │  │  ├─ Pipfile.lock
   │  │  │  ├─ plan.md
   │  │  │  ├─ predict-test.py
   │  │  │  ├─ predict.py
   │  │  │  └─ train.py
   │  │  ├─ data
   │  │  │  ├─ meta.csv
   │  │  │  └─ meta.json
   │  │  └─ README.md
   │  ├─ evaluation
   │  │  ├─ code
   │  │  │  └─ notebook.ipynb
   │  │  ├─ data
   │  │  │  ├─ meta.csv
   │  │  │  └─ meta.json
   │  │  └─ README.md
   │  └─ tests
   ├─ docs
   │  ├─ images
   │  │  └─ streamingatscale.png
   │  └─ streamingatscale.drawio
   ├─ LICENSE
   ├─ README.md
   ├─ requirements-test.txt
   ├─ requirements.txt
   └─ scaling-mlops-webapp
      ├─ .git
      ├─ .gitignore
      ├─ LICENSE
      ├─ package-lock.json
      ├─ package.json
      ├─ public
      ├─ README.md
      ├─ src
      │  ├─ App.css
      │  ├─ App.js
      │  ├─ App.test.js
      │  ├─ index.css
      │  ├─ index.js
      │  ├─ logo.svg
      │  ├─ MyComponent.css
      │  ├─ MyComponent.js
      │  ├─ ProjectInfo.js
      │  ├─ reportWebVitals.js
      │  └─ setupTests.js
      └─ tests
         └─ test.py
```

## Installation

To install and set up the project locally, follow these steps:

### Prerequisites

- Node.js (version X.X.X)
- Docker
- Python (version X.X.X)

### Installation Steps

1. **Clone the Repository**: Clone the project repository to your local machine:
   ```
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Install Frontend Dependencies**: Navigate to the `frontend` directory and install the required dependencies:
   ```
   cd frontend
   npm install
   ```

3. **Install Backend Dependencies**: Navigate to the `backend` directory and install the required Python dependencies:
   ```
   cd backend
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**: Set up any necessary environment variables required for the backend, such as API keys or database connection strings.

## Usage

To use the project, follow these steps:

1. **Start Frontend Development Server**: Navigate to the `frontend` directory and start the frontend development server:
   ```
   cd frontend
   npm start
   ```

2. **Start Backend Server**: Navigate to the `backend` directory and start the Flask server:
   ```
   cd backend
   python app.py
   ```

3. **Access the Application**: Open your web browser and navigate to `http://localhost:3000` to access the frontend application.

## Testing

To run tests for the project, follow these steps:

- **Frontend Tests**: Navigate to the `frontend` directory and run frontend tests:
  ```
  cd frontend
  npm test
  ```

- **Backend Tests**: Navigate to the `backend` directory and run backend tests:
  ```
  cd backend
  pytest
  ```

## Contributing

If you'd like to contribute to the project, please follow these guidelines:

- Report Bugs: If you encounter any bugs or issues, please open a new issue on GitHub.
  
- Suggest Improvements: If you have any suggestions for improvements or new features, please feel free to submit a pull request.
  
- Follow Coding Standards: Please ensure that your contributions adhere to the project's coding standards and style guidelines.

## License

This project is licensed under the MIT License.

## Author

Akshit Miglani: [Linkedin](https://www.linkedin.com/in/akshitmiglani/) | akshit.miglani09@gmail.com


