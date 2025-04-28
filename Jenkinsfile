pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Nanditha12207703/stock-price-tracker.git'
            }
        }
        
        stage('Build') {
            steps {
                // Any build steps, such as installing dependencies, can go here.
                echo 'Build steps go here.'
            }
        }
        
        stage('Deploy') {
            steps {
                // Add the deployment steps here, such as pushing to a server, cloud, or container
                echo 'Deploy steps go here.'
            }
        }
    }
}
