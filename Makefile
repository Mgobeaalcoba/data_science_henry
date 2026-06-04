# Makefile para automatizar tareas comunes del proyecto

.PHONY: help install update clean test format lint jupyter lab notebook

VENV = .venv
BIN = $(VENV)/bin

help:
	@echo "Comandos disponibles:"
	@echo "  make install     - Crear venv e instalar dependencias con pip"
	@echo "  make update      - Actualizar dependencias del requirements.txt"
	@echo "  make clean       - Limpiar archivos temporales"
	@echo "  make test        - Ejecutar tests usando el venv"
	@echo "  make format      - Formatear código con Black e isort usando el venv"
	@echo "  make lint        - Verificar código con flake8 usando el venv"
	@echo "  make jupyter     - Iniciar Jupyter Lab usando el venv"
	@echo "  make lab         - Alias para jupyter"
	@echo "  make notebook    - Iniciar Jupyter Notebook clásico usando el venv"

install:
	python3 -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

update:
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install --upgrade -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".coverage" -delete
	find . -type f -name "*.log" -delete

test:
	$(BIN)/pytest tests/ -v --cov=utils

format:
	$(BIN)/black .
	$(BIN)/isort .

lint:
	$(BIN)/flake8 utils/ --max-line-length=88 --extend-ignore=E203

jupyter:
	$(BIN)/jupyter lab

lab: jupyter

notebook:
	$(BIN)/jupyter notebook
