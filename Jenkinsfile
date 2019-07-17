pipeline {
  agent {
    dockerfile {
      filename 'backend/Dockerfile'
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