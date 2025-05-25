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

        stage('Update Codebase') {
            steps {
                sh '''
                    git config --global --add safe.directory /opt/crisis_relief
                    cd /opt/crisis_relief
                    git pull
                '''
            }
        }

        stage('Install Requirements') {
            steps {
                sh """
                cd ${PROJECT_DIR}
                bash -c "source ${VENV_PATH} && pip install -r requirements.txt"
                """
            }
        }

        stage('Run Migrations & Collect Static') {
            steps {
                sh """
                cd ${PROJECT_DIR}
                bash -c "source ${VENV_PATH} && python manage.py migrate && python manage.py collectstatic --noinput"
                """
            }
        }

        stage('Restart Gunicorn') {
            steps {
                sh '''
                    sudo systemctl restart crisis_relief
                '''
            }
        }
    }
}
