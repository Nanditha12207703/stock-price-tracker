pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'stock-prediction-app'
        REPO_URL = 'https://github.com/Nanditha12207703/stock-price-tracker.git'
        BRANCH = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git url: "${REPO_URL}", branch: "${BRANCH}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    echo 'Building Docker Image...'
                    sh 'docker build -t ${DOCKER_IMAGE_NAME} .'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add your deployment steps here
                    echo 'Deploying the application...'
                    // For example, you can run the Docker container
                    // sh 'docker run -d -p 8080:8080 ${DOCKER_IMAGE_NAME}'
                }
            }
        }
    }
