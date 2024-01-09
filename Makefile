VENV = venv
PYTHON = $(VENV)/bin/python
FLASK_APP = app/main.py

$(VENV):
	@echo "Criando ambiente virtual .."
	python3 -m venv $(VENV)

install: $(VENV)
	@echo "Iniciando a instalação de dependências .."
	$(VENV)/bin/pip install -r requirements.txt

run:
	@echo "Subindo servidor WSGI para desenvolvimento .."
	chmod +x $(FLASK_APP)
	$(VENV)/bin/python $(FLASK_APP)

clean:
	@echo "Removendo ambiente virtual .."
	rm -rf $(VENV)