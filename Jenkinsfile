pipeline {
    agent any

    environment {
        PROJECT_DIR = '/opt/crisis_relief'
        VENV_PATH = "${PROJECT_DIR}/venv/bin/activate"
    }
    
    triggers {
        githubPush()
    }

    stages {
        stage('Deploy') {
            steps {
                sh '''
                    git config --global --add safe.directory /opt/crisis_relief
                    cd /opt/crisis_relief
                    git pull
                    bash -c "source ${VENV_PATH} && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput"
                    sudo systemctl restart crisis_relief
                '''
            }
        }
    }
}
