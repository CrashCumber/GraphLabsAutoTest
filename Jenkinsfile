pipeline {
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    agent any
    stages {
        stage('Подготовка окружения для тестирования') {
            steps {
                sh "docker-compose build"
            }
        }
        stage('Тестирование модуля') {
            steps {
                sh "docker-compose up -d"
                sh 'docker attach $(docker-compose ps | grep tests | tr -s " " | cut -f 1 -d " ") || true'
            }
        }
        stage('Создание отчета о тестировании') {
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
        stage('Деактивация окружения') {
            steps {
                sh "docker-compose stop"
            }
        }
    }
}
