run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

clean:
	rm *.mp3

.PHONY: run clean
