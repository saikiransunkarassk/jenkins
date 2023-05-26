import subprocess
import os

os.environ["NEW_ENV1"]="new environmental variable is set"

commandList=["conftest","verify", "--policy" ,"./policies/policy1", "--output=table"]
print(os.environ)
subprocess.run(commandList)