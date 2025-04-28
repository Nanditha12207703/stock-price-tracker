pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'stock-prediction-app'
    }

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
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy your Docker container
                    // (If you need to deploy, use docker run or docker-compose)
                    sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE'
                }
            }
        }
    }
    post {
        always {
            // Clean up, stop container or any final tasks
            cleanWs()
        }
    }
}
