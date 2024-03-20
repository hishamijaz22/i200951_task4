build:
	docker build -t iris-classifier .

run:
	docker run -p 5000:5000 iris-classifier
