all: tests

tests:
	pytest -s -l -v tests/tests_ui/test_ui_module18_page.py

tests_selenium:
	bash run_selenoid.sh && pytest --selenoid=True

tests_with_report:
	pytest -s -l -v tests/tests_ui/test_ui_module18_page.py > tests_result

info:
	 git log --author="" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }'
