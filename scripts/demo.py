import subprocess

subprocess.run("conftest verify --policy ../policies/policy1 --output=table",shell=True)