
pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip3 install pytest'
            }
        }

        stage('Descarga') {
            steps {
                git url: 'https://github.com/TuPapiJorgito/AgentesJenkins.git',
                    branch: 'main'
            }
        }

        stage('Ejecutar') {
            steps {
                sh 'python3 Conversion.py'
            }
        }

        stage('Probar') {
            steps {
                sh 'mkdir -p reports'
                sh 'python3 -m pytest -v --junitxml=reports/results.xml'
            }

            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}
