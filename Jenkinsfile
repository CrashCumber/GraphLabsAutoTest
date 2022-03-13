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
        stage('Up tests') {
            steps {
                sh "docker-compose up"
            }
        }
        stage('Stop containers') {
            steps {
                sh "docker-compose stop"
            }
        }
        stage('Rm containers') {
            steps {
                sh "docker-compose rm"
            }
        }
    }
}
