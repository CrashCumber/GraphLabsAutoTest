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
        stage('Start tests') {
            steps {
                sh "docker-compose up -d"
                sh 'docker attach $(docker-compose ps | grep tests | tr -s " " | cut -f 1 -d " ")'
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
        stage('Stop system') {
            steps {
                sh "docker-compose stop"
            }
        }
    }
}
