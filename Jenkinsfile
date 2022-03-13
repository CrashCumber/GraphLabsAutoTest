pipeline {
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    agent any
    stages {
        stage('Build image') {
            steps {
                sh "docker-compose build"
            }
        }
        stage('Pull browser') {
            steps {
                sh "docker-compose up"
            }
        }
    }
}
