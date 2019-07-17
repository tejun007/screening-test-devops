pipeline {
  agent {
    docker {
      image 'python:3.6.5'
      args '-p 5000:5000'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'pip install --trusted-host pypi.python.org -r requirements.txt'
      }
    }
  }
  environment {
    PYTHONUNBUFFERED = '1'
    PATH = '$PATH:/backend'
    PYTHONPATH = '$PYTHONPATH:/:/backend'
  }
}