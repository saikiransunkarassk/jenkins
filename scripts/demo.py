import subprocess
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--changeVar",nargs=2)

args=parser.parse_args()

print(args)
if(args.changeVar[0] in os.environ.keys()):
    # os.environ[args.changeVar[0]]=args.changeVar[1] #temp change
    subprocess.run(f"export ${args.changeVar[0]}=${args.changeVar[1]}",shell=True)
    print("environment varable successfully changed")

# os.environ["NEW_VAR"]="Hello World!" #temp storage

subprocess.run(f"export ${args.changeVar[0]}=${args.changeVar[1]}")

print("new environment variable is created")

commandList1=["conftest","verify", "--policy" ,"./policies/policy1", "--output=table"]

commandList2=["conftest","verify", "--policy" ,"./policies/policy1", "--output=table"]

val=subprocess.run(commandList1,capture_output=True,text=True)



output=val.stdout

print(output)

if(val.returncode==0):
    print("successfully runned")
else:
    print("unsuccessful")