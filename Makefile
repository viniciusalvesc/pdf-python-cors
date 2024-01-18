VENV = venv
PYTHON = $(VENV)/bin/python
FAST_API_MAIN = app/main.py
FAST_API_APP = app.main:main
UVICORN_CMD = $(PYTHON) -m uvicorn $(FAST_API_APP) --host localhost --port 3334 --reload

$(VENV):
	@echo "Criando ambiente virtual .."
	python3 -m venv $(VENV)

install: $(VENV)
	@echo "Iniciando a instalação de dependências .."
	$(VENV)/bin/pip install -r requirements.txt

run:
	@echo "Subindo servidor ASGI Uvicorn para desenvolvimento .."
	chmod +x $(FAST_API_MAIN)
	$(UVICORN_CMD)

clean:
	@echo "Removendo ambiente virtual .."
	rm -rf $(VENV)