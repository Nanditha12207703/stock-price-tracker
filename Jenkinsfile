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
                git branch: 'main', url: 'https://github.com/Nanditha12207703/stock-price-tracker.git'
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
        echo 'Deploying the Docker container...'
        script {
            bat 'docker rm -f stock-price-tracker-container || exit 0'
            bat 'docker run -d -p 8501:8501 --name stock-price-tracker-container stock-price-tracker'
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
