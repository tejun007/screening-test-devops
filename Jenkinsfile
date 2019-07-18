pipeline {
  environment {
    registry = 'tejunlee007/screening-test-backend'
    registryCredential = 'dockerhub'
    backendImage = ''
  }
  agent none
  stages {
    stage('build & test') {
      agent {
        docker {
          image 'python:3.6.5'
        }
      }
      environment {
        PYTHONUNBUFFERED = '1'
        PATH = '$PATH:/backend'
        PYTHONPATH = '$PYTHONPATH:/:/backend'

        CI = 'true'
      }
      stages {
        stage('build') {
          steps {
            sh 'pip install --trusted-host pypi.python.org -r ./backend/requirements.txt'
          }
        }
        stage('test') {
          steps {
            sh 'pytest ./backend'
          }
        }
      }
    }
    stage('push') {
      agent none
      steps {
        sh  './push.sh'
      }
    }
  }
}
