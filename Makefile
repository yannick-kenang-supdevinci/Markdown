.PHONY: init test run build clean

IMAGE_NAME=health-calculator-service
PORT=5000

init:
	@echo "Installing dependencies..."
	python3 -m pip install -r requirements.txt

test:
	@echo "Running tests..."
	python3 -m pytest test.py -v

run:
	@echo "Running the Flask app..."
	python3 app.py

build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

docker-run:
	@echo "Running Docker container..."
	docker run -p $(PORT):$(PORT) $(IMAGE_NAME)

clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
