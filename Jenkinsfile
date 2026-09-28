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
    }

    post {
        success {
            echo 'Linux Command Explorer CI Pipeline Passed!'
        }

        failure {
            echo 'Linux Command Explorer CI Pipeline Failed!'
        }
    }
}