pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile
                    sh 'docker build -t stock-prediction-app .'
                }
            }
        }
        stage('Run Docker Image') {
            steps {
                script {
                    // Run the Docker container in detached mode
                    sh 'docker run -d -p 5000:5000 stock-prediction-app'
                }
            }
        }
    }
}
