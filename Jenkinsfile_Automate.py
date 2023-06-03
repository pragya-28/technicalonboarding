pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('setup') {
            steps {
                browserstack(credentialsId: '78e87401-8946-4e7e-9d5c-b9dccfbb8e52'){
                    sh 'python3 -m pip install --upgrade pip'
                    sh 'pip3 install -r AutomateDemo/requirements.txt'
                    sh 'python3 AutomateDemo/browserStack.py'
                    echo 'Hello....'}
            }
        }
    }
}
