docker run -i  -P --link selenoid:selenoid --name tests_container --network tests_network tests_image \
    pytest tests/tests_ui/test_ui_module18_page.py \
    --selenoid=True --browser="firefox" --browser_ver="latest"
