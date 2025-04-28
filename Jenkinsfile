pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Nanditha12207703/real_time_price_tracker.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t stock-tracker-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8501:8501 stock-tracker-app'
            }
        }
    }
}
