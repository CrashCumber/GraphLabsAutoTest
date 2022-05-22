pipeline {
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    agent any
    stages {
        stage('Сборка окружений') {
            steps {
                sh "docker-compose build"
            }
        }
        stage('Автоматизированное тестирование модуля') {
            steps {
                sh "docker-compose up -d"
                sh 'docker attach $(docker-compose ps | grep tests | tr -s " " | cut -f 1 -d " ") || true'
            }
        }
        stage('Сбор результатов') {
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
        stage('Составление отчета') {
            steps {
                sh "docker-compose stop"
            }
        }
    }
}
