test:
	python3 -m doctest textstats.py

run:
	python3 textstats.py

clean:
	rm -rf __pycache__
