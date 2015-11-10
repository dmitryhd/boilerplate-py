all:
	test

test:
	nosetests-3.4 --with-coverage --cover-package=web --cover-erase --cover-inclusive -vx tests;

deploy:
	./bin/deploy.sh;

install:
	./bin/install.sh;

doc:
	cd docs/sphinx && make html && sensible-browser _build/html/index.html

clean:
	find . -name '*.pyc' -exec rm -f {} +; find . -name '*~' -exec rm -f {} +

