# Makefile minimo para el curso

.PHONY: help install jupyter audit execute clean

VENV = .venv
BIN = $(VENV)/bin
VALIDATOR = .agents/skills/notebook-workflow/scripts/validate_notebooks.py

help:
	@echo "Comandos disponibles:"
	@echo "  make install   - Crear entorno virtual e instalar dependencias"
	@echo "  make jupyter   - Iniciar Jupyter Lab"
	@echo "  make audit     - Auditar reglas pedagogicas y tecnicas en los 11 notebooks"
	@echo "  make execute   - Re-ejecutar todos los notebooks en .venv y auditar"
	@echo "  make clean     - Limpiar archivos temporales"

install:
	python3 -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

jupyter:
	$(BIN)/jupyter lab

audit:
	$(BIN)/python $(VALIDATOR) --audit

execute:
	$(BIN)/python $(VALIDATOR) --execute --audit

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type d -name "catboost_info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
