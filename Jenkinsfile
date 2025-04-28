/*pipeline {
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
                        bat 'python --version'
                        bat 'python -m pip install --upgrade pip'
                        bat 'python -m pip install -r requirements.txt'
                    } else {
                        echo "No requirements.txt found, skipping dependency installation."
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting the Python application...'
                bat 'python app.py'
            }
        }
    }
}
*/

pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the Git repository...'
                git 'https://github.com/Nanditha12207703/stock-price-tracker.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing project dependencies...'
                script {
                    bat "\"${env.PYTHON_PATH}\" -m pip install -r requirements.txt"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                echo 'Starting Python app...'
                bat 'start /B C:\\Python311\\python.exe app.py'
                // Add any deployment steps here, e.g., running the app or Docker container
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
