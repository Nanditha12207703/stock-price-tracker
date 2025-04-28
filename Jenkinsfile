pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning Repository...'
                // In Pipeline from SCM, Jenkins clones automatically. So no git clone needed here.
                // We can just print working directory.
                bat 'cd'
                bat 'dir'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing project dependencies...'
                script {
                    if (fileExists('requirements.txt')) {
                        bat 'C:\\Python311\\python.exe -m pip install -r requirements.txt'
                    } else {
                            echo "No requirements.txt found, skipping dependency installation."
                    }
                }
            }
        }


        stage('Deploy') {
            steps {
                echo 'Starting the Python application...'
                bat 'start /B C:\\Python311\\python.exe app.py'
            }
        }

    }
}
