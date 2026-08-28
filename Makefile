# Makefile minimo para el curso

.PHONY: help install jupyter clean

VENV = .venv
BIN = $(VENV)/bin

help:
	@echo "Comandos disponibles:"
	@echo "  make install   - Crear entorno virtual e instalar dependencias"
	@echo "  make jupyter   - Iniciar Jupyter Lab"
	@echo "  make clean     - Limpiar archivos temporales"

install:
	python3 -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

jupyter:
	$(BIN)/jupyter lab

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type d -name "catboost_info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
