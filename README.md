Hi! welcome to my task.
Firtly we need to install everything.
Please make sure you got python 3.x

Run the following command:
Please make sure you are at root folder and run:
"pip install -r requirements.txt"

Then please run the following command:
"python .\utils\download_chromedriver.py"

Then you got 2 choices:
Running: "pytest -v" would trigger the tests and you can see them run.

Running:
"pytest --html=./test_results/report.html"

Would generate an HTML report, this report can be find in test_result
If you would like to view the reports please run:
"start .\test_results\report.html"