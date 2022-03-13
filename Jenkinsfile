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
                sh "docker-compose up -d"
            }
        }
        stage('Build report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'report']]
                ])
            }
        }
        stage('Rm containers') {
            steps {
                sh "docker-compose stop"
            }
        }
    }
}
