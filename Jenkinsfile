pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning Repository...'
                // In Pipeline from SCM, Jenkins clones automatically. So no git clone needed here.
                // We can just print working directory.
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing project dependencies...'
                // Install requirements if requirements.txt exists
                script {
                    if (fileExists('requirements.txt')) {
                        sh 'pip install -r requirements.txt'
                    } else {
                        echo "No requirements.txt found, skipping dependency installation."
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting the Python application...'
                // Run the stock_price_tracker.py script
                sh 'python stock_price_tracker.py &'
            }
        }
    }
}
