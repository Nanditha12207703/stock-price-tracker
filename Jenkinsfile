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
                sh 'docker build -t stock-price-tracker .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Running the Docker container...'
                sh '''
                    docker rm -f stock-price-tracker-container || true
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
