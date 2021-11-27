docker run -d --name selenoid -p 4444:4444 \
 -v /var/run/docker.sock:/var/run/docker.sock \
-v /Users/mac/Desktop/GraphLabsAutoTesting/config/:/etc/selenoid/:ro \
--net project_qa_default aerokube/selenoid:1.10.0 \
-conf /etc/selenoid/browsers.json -container-network project_qa_default
