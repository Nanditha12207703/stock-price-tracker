
pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], 
                    userRemoteConfigs: [[url: 'https://github.com/Nanditha12207703/stock-price-tracker.git']]
                ])
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }
}
