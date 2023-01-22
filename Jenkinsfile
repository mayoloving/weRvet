pipeline {

    agent any

    environment {
        AWS_ACCOUNT_ID="644435390668"
        AWS_DEFAULT_REGION="eu-west-2"
        IMAGE_REPO_NAME="yotambenz"
        IMAGE_TAG="latest"
        REPOSITORY_URI="${AWS_ACOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }

    options { timestamps () }


    stages {

        stage ("checkout") {
            steps {
                deleteDir()
                checkout scm
            }
        }

        stage ("logging into AWS") {
            steps {
                script {
                    sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
            }
        }

        stage ("Build") {
            when {
                anyOf {
                    expression {env.BRANCH_NAME.contains("feature/")}
                    expression {env.BRANCH_NAME.contains("master")}
                }
            }
            steps {
                sh """
                    docker build -t wervet .
                """
            }
            
        }


        stage ("Unit test") {
            when {
                anyOf {
                    expression {env.BRANCH_NAME.contains("feature/")}
                    expression {env.BRANCH_NAME.contains("master")}
                }
            }
            steps {
                sh """
                    docker run --name wervettest -d -p 5000:5000 wervet
                    sleep 5
                    curl 18.133.246.205:5000
                    docker stop wervettest || echo "no wervettest"
                    docker rm -f wervettest || echo "no wervettest"
                """
            }
            
        }

        stage ("E2E") {
            when {
                anyOf {
                    expression {env.BRANCH_NAME.contains("feature/")}
                    expression {env.BRANCH_NAME.contains("master")}
                }
            }
            steps {
                sh """
                    pwd
                    ls -al
                    docker-compose up --build -d
                    cd test
                    docker build -t tester .
                    docker run --name testinge2e --network=portfolio-proj_master_default tester:latest
                """
            }
        }

        stage ("Calculate and set a 3-number version (for master)") {
            when {
                expression {
                    env.BRANCH_NAME.contains("master")
                }
            }
            steps {
                withCredentials([gitUsernamePassword(credentialsId: 'github_cred', gitToolName: 'Default')]){
                    sh "./calc_tag.sh"
                }
            } 
        }
                        
        // stage ("Clean/reset and tag") {
        //     when {
        //         expression {
        //             env.BRANCH_NAME.contains("master")
        //         }
        //     }
        //     steps {
        //         sh """
        //             val=\$(cat v.txt)
        //             git tag \$val HEAD
        //             git push http://root:Aa123456@gitlab.example.com/gitlab-instance-9450cc01/analytics.git \$val
        //             git clean -f
        //         """
        //     }
        // }

        stage ("Publish to ECR") {
            when {
                expression {
                    env.BRANCH_NAME == "master"
                }
            }
            steps {
                sh """
                    docker tag wervet:latest 644435390668.dkr.ecr.eu-west-2.amazonaws.com/yotambenz:latest
                    docker push 644435390668.dkr.ecr.eu-west-2.amazonaws.com/yotambenz:latest
                """
            }
        }


        // stage ("Deploy") {
        //      when {
        //         expression {
        //             env.BRANCH_NAME == "master"
        //         }
        //     }
        //     steps {
        //         withCredentials([sshUserPrivateKey(credentialsId: 'key-gen1', keyFileVariable: '', usernameVariable: 'key-gen1')]) {
        //             sh """
        //                 ssh ubuntu@10.30.0.209 "docker rm -f toxicon || true"
        //                 ssh ubuntu@10.30.0.209 "docker rmi -f toxic || true"

        //                 ssh ubuntu@10.30.0.209 "docker pull 644435390668.dkr.ecr.eu-west-2.amazonaws.com/yotambenz:latest"

        //                 ssh ubuntu@10.30.0.209 "docker run --name toxicon -d -p 8085:8080 644435390668.dkr.ecr.eu-west-2.amazonaws.com/yotambenz:latest"
        //             """
        //         }
                
        //     }
        // }

        

    }

    post { 
        success { 
            sh """ 
                docker stop wervettest || echo "no wervettest"
                docker rm -f wervettest || echo "no wervettest"
                docker rmi -f wervet || echo "no wervet"

                docker-compose down || echo "no compose"

                docker stop testinge2e || echo "no testinge2e"
                docker rm -f testinge2e || echo "no testinge2e"
                docker rmi -f tester || echo "no tester"
            """ 
             
        } 
        failure { 
            sh """ 
                docker stop wervettest || echo "no wervettest"
                docker rm -f wervettest || echo "no wervettest"
                docker rmi -f wervet || echo "no wervet"

                docker-compose down || echo "no compose"

                docker stop testinge2e || echo "no testinge2e"
                docker rm -f testinge2e || echo "no testinge2e"
                docker rmi -f tester || echo "no tester"
            """ 
            mail (to: "benz.yota@gmail.com", subject: "BUILD LOG", body: "the build was a failure");
        } 
    } 


}
