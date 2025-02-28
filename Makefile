.PHONY: typing

typing:
	docker build -t types .
	docker run --rm types mypy basik/ intermediate/