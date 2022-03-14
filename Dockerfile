FROM python:3.8.12

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
WORKDIR .
CMD ["pytest", "/tests/tests_ui/test_ui_module18_page.py", "-l", "-v", "-s"]
