import webbrowser
import os

def open_html_report(report_path="D:/AutomationInfrastructures/phoneDo/selenium_Python/utils/report.html"):
    try:
        # Open the HTML report in the default web browser
        webbrowser.open("file://" + os.path.abspath(report_path))
    except Exception as e:
        print(f"Error opening HTML report: {e}")

if __name__ == "__main__":
    open_html_report()
