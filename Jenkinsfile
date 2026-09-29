// Jenkins automatic polling test
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                    "C:\\Users\\SATHANA JEEVA\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version
                    "C:\\Users\\SATHANA JEEVA\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install --upgrade pip
                    "C:\\Users\\SATHANA JEEVA\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    "C:\\Users\\SATHANA JEEVA\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                bat '''
                    "C:\\Users\\SATHANA JEEVA\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" version
                    "C:\\Users\\SATHANA JEEVA\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t linux-command-explorer:latest .
                '''
            }
        }

        stage('Ansible Deploy') {
            steps {
                bat '''
                    wsl -d Ubuntu -- bash -c "cd '/mnt/c/Users/SATHANA JEEVA/OneDrive/Desktop/linux-command-explorer' && ansible-playbook -i ansible/inventory.ini ansible/deploy.yml"
                '''
            }
        }
    }

    post {
        success {
            echo 'Linux Command Explorer CI/CD Pipeline Passed!'
        }

        failure {
            echo 'Linux Command Explorer CI/CD Pipeline Failed!'
        }
    }
}

// Automatic polling verified