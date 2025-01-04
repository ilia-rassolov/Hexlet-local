test:
	PYTHONPATH=src:implementations FUNCTION_VERSION=user_implementation suppressor pass pytest tests
	PYTHONPATH=src:implementations FUNCTION_VERSION=right suppressor pass pytest tests
	PYTHONPATH=src:implementations FUNCTION_VERSION=wrong1 suppressor fail pytest tests
	PYTHONPATH=src:implementations FUNCTION_VERSION=wrong2 suppressor fail pytest tests
	PYTHONPATH=src:implementations FUNCTION_VERSION=wrong3 suppressor fail pytest tests

.PHONY: test
