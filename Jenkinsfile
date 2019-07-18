pipeline {
  environment {
    registry = 'tejunlee007/screening-test-backend'
    registryCredential = 'dockerhub'
    backendImage = ''
  }
  agent none
  stages {
    stage('build') {
      agent {
        docker {
          image 'python:3.6.5'
        }
      }
      environment {
        PYTHONUNBUFFERED = '1'
        PATH = '$PATH:/backend'
        PYTHONPATH = '$PYTHONPATH:/:/backend'
      }
      steps {
        sh 'pip install --trusted-host pypi.python.org -r ./backend/requirements.txt'
      }
    }
    stage('test') {
      environment {
        CI = 'true'
      }
      steps {
        sh 'pip install --trusted-host pypi.python.org -r ./backend/requirements.txt'
        sh 'pytest ./backend'
      }
    }
    stage('push') {
      agent {
        docker {
          image 'docker:latest'
        }
      }
      steps {
        sh  './push.sh'
      }
    }
  }
}
