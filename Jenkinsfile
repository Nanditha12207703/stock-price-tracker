pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the Git repository...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                bat 'docker build -t stock-price-tracker .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Running the Docker container...'
                bat '''
                    docker stop stock-price-tracker-container || exit 0
                    docker rm stock-price-tracker-container || exit 0
                    docker run -d -p 8501:8501 --name stock-price-tracker-container stock-price-tracker
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}

