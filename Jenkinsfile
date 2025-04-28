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
        PYTHON_HOME = "C:\\Python311"
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone') {
            steps {
                echo 'Cloning Repository...'
                dir('C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\stock-price-tracker') {
                    bat 'dir'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Installing project dependencies...'
                script {
                    // Check if Python is available
                    if (!fileExists("${PYTHON_HOME}\\python.exe")) {
                        error "Python not found at ${PYTHON_HOME}. Please check your Python installation."
                    }

                    // Install dependencies
                    bat "${PYTHON_HOME}\\python.exe -m pip install -r requirements.txt"
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Python app...'
                bat 'start /B C:\\Python311\\python.exe app.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
