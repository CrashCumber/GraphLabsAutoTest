pipeline {
    agent any
    stages {
        stage("Build image") {
            steps {
                catchError {
                    script {
                        docker.build("python-web-tests", "-f Dockerfile .")
                    }
                }
            }
        }
        stage('Pull browser') {
            steps {
                catchError {
                    script {
                        docker.image('selenoid/chrome:latest')
                    }
                }
            }
        }
        stage('Run tests') {
            steps {
                catchError {
                    script {
                        docker.image('aerokube/selenoid:1.10.0').withRun('-p 4444:4444 -v /run/docker.sock:/var/run/docker.sock -v /tests/conf:/etc/selenoid/', '-timeout 600s -limit 2') { c ->
                        docker.image('python-web-tests').inside("--link ${c.id}:selenoid") {sh "pytest --selenoid=True"}
                    }
                }
            }
        }
    }
}
}
