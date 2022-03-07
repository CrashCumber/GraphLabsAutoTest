all: tests

tests_selenoid:
	bash run_selenoid.sh && pytest --selenoid=True

test:
	pytest -s -l -v -m CLICK tests/tests_ui/test_ui_module18_page.py --alluredir=allure_results


tests_run_selenoid_allure:
	bash run_selenoid.sh && pytest -m CLICK --selenoid=True --alluredir=allure_results


tests_allure:
	pytest -m CLICK --selenoid=True --alluredir=allure_results


info:
	 git log --author="" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'
