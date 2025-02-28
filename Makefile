.PHONY: typing

typing:
	docker build -t types .
	docker run --rm types mypy test_basic/ test_intermediate/