pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning Repository...'
                bat 'cd'
                bat 'dir'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing project dependencies...'
                script {
                    if (fileExists('requirements.txt')) {
                        bat 'pip install -r requirements.txt'
                    } else {
                        echo "No requirements.txt found, skipping dependency installation."
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting the Python application...'
                bat 'start /B python app.py'
            }
        }
    }
}
