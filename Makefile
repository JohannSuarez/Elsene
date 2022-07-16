run:
	uvicorn app.main:app --reload

clean:
	rm *.mp3

.PHONY: run clean
