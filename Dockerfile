FROM python:3.8.12

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

VOLUME /Users/mac/Desktop/GraphLabsAutoTesting/allure_results allure_results

RUN make test
