import subprocess

subprocess.call("allure generate report/result -o report/allure_html --clean", shell=True)