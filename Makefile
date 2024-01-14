VENV = venv
PYTHON = $(VENV)/bin/python
FAST_API_APP = app/main.py

$(VENV):
	@echo "Criando ambiente virtual .."
	python3 -m venv $(VENV)

install: $(VENV)
	@echo "Iniciando a instalação de dependências .."
	$(VENV)/bin/pip install -r requirements.txt

run:
	@echo "Subindo servidor ASGI Uvicorn para desenvolvimento .."
	chmod +x $(FAST_API_APP)
	$(VENV)/bin/python $(FAST_API_APP)

clean:
	@echo "Removendo ambiente virtual .."
	rm -rf $(VENV)