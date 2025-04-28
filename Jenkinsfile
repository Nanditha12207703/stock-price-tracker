pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t stock-prediction-app .'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Run the Docker container
                    sh 'docker run -d -p 8501:8501 stock-prediction-app'
                }
            }
        }
    }
}
