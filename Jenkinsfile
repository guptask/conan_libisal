pipeline {
    agent any

    environment {
        PROJECT = 'libisal'
        CONAN_CHANNEL = 'stable'
        CONAN_USER = 'bincrafters'
        CONAN_PASS = credentials('CONAN_PASS')
    }

    stages {
        stage('Build') {
            steps {
                sh "docker build --rm --build-arg CONAN_USER=${CONAN_USER} --build-arg CONAN_PASS=${CONAN_PASS} --build-arg CONAN_CHANNEL=${CONAN_CHANNEL} -t ${PROJECT} ."
            }
        }

        stage('Test') {
            steps {
                echo "Tests go here"
            }
        }

        stage('Deploy') {
            when {
                branch "${CONAN_CHANNEL}/*"
            }
            steps {
                sh "docker run --rm ${PROJECT}"
            }
        }
    }
    post {
        always {
            sh "docker rmi -f ${PROJECT}"
        }
    }
}
