# Makefile para automatizar tareas comunes del proyecto

.PHONY: help install update clean test format lint jupyter lab notebook

help:
	@echo "Comandos disponibles:"
	@echo "  make install     - Instalar dependencias con Poetry"
	@echo "  make update      - Actualizar dependencias"
	@echo "  make clean       - Limpiar archivos temporales"
	@echo "  make test        - Ejecutar tests"
	@echo "  make format      - Formatear código con Black e isort"
	@echo "  make lint        - Verificar código con flake8"
	@echo "  make jupyter     - Iniciar Jupyter Lab"
	@echo "  make lab         - Alias para jupyter"
	@echo "  make notebook    - Iniciar Jupyter Notebook clásico"

install:
	poetry install

update:
	poetry update

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
	poetry run pytest tests/ -v --cov=utils

format:
	poetry run black .
	poetry run isort .

lint:
	poetry run flake8 utils/ --max-line-length=88 --extend-ignore=E203

jupyter:
	poetry run jupyter lab

lab: jupyter

notebook:
	poetry run jupyter notebook
