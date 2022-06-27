pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                git branch: 'HomePage', url: 'https://github.com/AsadS95x/volunteerfundamentals.git'
                sh '''#/bi/bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m create.py'''
            }
        }
        stage('PyTest') { 
            steps {
                git branch: 'HomePage', url: 'https://github.com/AsadS95x/volunteerfundamentals.git'
                sh '''#/bi/bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m Pytest.py'''
            }
        }
    }
}