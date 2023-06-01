pipeline{
    agent any
    environment{
        ENV_ONE=1
        ENV_TWO=2
        ENV_THREE=3
        ENV_VALUE="old value"
    }
    parameters{
         string(name:'newString',defaultValue:"hello",description:"")

         string(name:'MAIN_PY_LOC',defaultValue:"./scripts/main.py",description:"main.py file location")

         string(name:'POLICY_LOC',defaultValue:"./policies",description:"policy folder location")

         string(name:'POLICY_FOLDER_NAME',defaultValue:"policy1",description:"name of the policy folder")
    }
    stages{
        stage("inbuildEnvironmentVar")
        {
            steps{
          
                echo "JENKINS_URL : ${JENKINS_URL}"

            }
        }
        stage("pythonScript")
        {
            steps{
              echo "before running python script ENV_VALUE : ${ENV_VALUE}"
              sh "python -u ${MAIN_PY_LOC} --location ${POLICY_LOC} --folderName ${POLICY_FOLDER_NAME} --printEnvVarName ${ENV_THREE}"
              echo "after running python script ENV_VALUE : ${ENV_VALUE}"
              sh "export NEW_VAR=new"
              echo "new enviroment var NEW_VAR : ${NEW_VAR}"
              sh "python3 ./scripts/destroyEnvVars.py"
            }
        }
        stage("parameters")
        {
            steps{
               
                echo "parameters variable newString : ${params.newString}"
                
            }
        }
        stage("parallel stages")
        {
             when{

                 branch "main1"   
                }
            parallel{
               
                stage("p1"){
                    steps{
                        echo "parallel 1"
                    }
                }
                stage("p2"){
                    steps{
                        echo "parallel 2"
                    }
                }
                 stage("p3"){
                    steps{
                        echo "parallel 2"
                    }
                }
                }
        }
        stage("one")
        {
            steps{
                echo "one ${ENV_ONE}"
            }
              
        }

        stage("two")
        {
            steps{
                echo "tw ${ENV_TWO}"
            }
        }
        stage("three")
        {
            steps{
                echo "three ${ENV_THREE}"
            }
        }
    }
}
