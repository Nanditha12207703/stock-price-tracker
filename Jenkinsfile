pipeline {
    agent any
    
    stages {
        stage('Clone') {
            steps {
                echo 'Code already cloned by Jenkins from SCM'
                // No need to manually checkout here
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the stock price tracker project...'
                // Add build commands if needed, like:
                // sh 'pip install -r requirements.txt'
                // sh 'python setup.py build'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying the stock price tracker project...'
                // Add deploy steps here, e.g.:
                // sh 'docker build -t stock-price-tracker .'
                // sh 'docker run -d -p 5000:5000 stock-price-tracker'
            }
        }
    }
