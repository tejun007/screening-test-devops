pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip install --trusted-host pypi.python.org -r ./backend/requirements.txt'
      }
    }
    stage('test') {
      environment {
        CI = 'true'
      }
      steps {
        sh 'pytest ./backend'
      }
    }
    stage('build image') {
      steps {
        script {
          backendImage = docker.build registry + ':$BUILD_NUMBER'
        }
      }
    }
    stage('push image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
  }
  environment {
    PYTHONUNBUFFERED = '1'
    PATH = '$PATH:/backend'
    PYTHONPATH = '$PYTHONPATH:/:/backend'

    registry = 'tejunlee007/screening-test-backend'
    registryCredential = 'dockerhub'
    backendImage = ''
  }
}
