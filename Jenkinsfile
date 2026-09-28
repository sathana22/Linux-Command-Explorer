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
                    python --version
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    pytest
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