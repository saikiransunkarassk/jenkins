import subprocess
import os
import argparse
import re

class NewClass:
    def __init__(self, location, policyName):

        self.location = location

        self.policyName = policyName

        self.returnCode = True

    def conftestCommand(self):

        output = subprocess.run(["conftest", "verify", "--policy", "./"+self.location +
                                "/"+self.policyName, "--output=table"], capture_output=True, text=True)

        if (output.returncode != 0):

            self.returnCode = False

        else:

            print(output.stdout)

    def opaCommand(self):

        output = subprocess.run(["opa", "test", "-c", "./"+self.location + "/"+self.policyName+"/"+self.policyName+".rego",
                                "./"+self.location + "/"+self.policyName+"/"+self.policyName+"_test.rego"], capture_output=True, text=True)

        if (output.returncode != 0):

            self.returnCode = False

        else:

            print(output.stdout)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--location")

    parser.add_argument("--policyName")

    inputs = parser.parse_args()

    newObject = NewClass(inputs.location, inputs.policyName,
                         inputs.printEnvVarName)

    if (inputs.location != None and inputs.policyName != None):

        newObject.conftestCommand()

        newObject.opaCommand()
  

    if (newObject.returnCode == True):
        print("successful")
    else:
        print("unsuccessful")


