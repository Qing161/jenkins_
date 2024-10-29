pipeline {
    agent any // 指定任何可用的agent来执行此任务

    environment { // 定义环境变量
        PYTHON_VERSION = '3.8' // Python版本可以根据需要更改
    }

    stages { // 定义构建的不同阶段
        stage('Checkout') { // 检出代码
            steps {
                git branch: 'main', credentialsId: 'github-creds', url: 'https://github.com/your-repo/repo.git'
            }
        }

        stage('Install dependencies') { // 安装依赖
            steps {
                script {
                    sh 'python -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') { // 运行测试
            steps {
                sh 'pytest --junitxml=/tmp/test-results.xml'
            }
        }

        stage('Package') { // 打包应用
            steps {
                sh 'python setup.py sdist'
            }
        }

        stage('Deploy') { // 部署应用
            steps {
                sh 'scp dist/*.tar.gz user@yourserver:/path/to/deploy'
            }
        }
    }

    post { // 构建后执行的操作
        always {
            junit 'test-results.xml' // 发布JUnit测试报告
        }
    }
}