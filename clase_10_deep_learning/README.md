# Clase 10: Introducción al Deep Learning

## Objetivos
- Comprender los fundamentos de las redes neuronales
- Implementar redes neuronales con TensorFlow/Keras y PyTorch
- Conocer diferentes arquitecturas (CNN, RNN, LSTM)
- Aplicar Transfer Learning

## Contenidos

### 1. Fundamentos de Redes Neuronales
- Perceptrón
- Función de activación
- Forward propagation
- Backpropagation
- Gradient descent

### 2. Deep Neural Networks (DNN)
- Arquitecturas multicapa
- Funciones de activación (ReLU, Sigmoid, Tanh, Softmax)
- Inicialización de pesos
- Optimizadores (SGD, Adam, RMSprop)

### 3. Convolutional Neural Networks (CNN)
- Capas convolucionales
- Pooling layers
- Arquitecturas clásicas (LeNet, AlexNet, VGG, ResNet)
- Aplicaciones en visión por computadora

### 4. Recurrent Neural Networks (RNN)
- Procesamiento de secuencias
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)
- Aplicaciones en NLP y series temporales

### 5. Técnicas de Regularización
- Dropout
- Batch Normalization
- Early Stopping
- Data Augmentation

### 6. Transfer Learning
- Concepto y aplicaciones
- Fine-tuning
- Feature extraction
- Modelos pre-entrenados (ImageNet)

## Notebooks

1. **01_perceptron_basico.ipynb**: Implementación desde cero
2. **02_keras_introduccion.ipynb**: Primeros pasos con Keras
3. **03_pytorch_introduccion.ipynb**: Primeros pasos con PyTorch
4. **04_cnn_clasificacion_imagenes.ipynb**: CNN para MNIST/CIFAR
5. **05_rnn_series_temporales.ipynb**: RNN para predicción
6. **06_transfer_learning.ipynb**: Transfer learning con modelos pre-entrenados
7. **07_comparacion_frameworks.ipynb**: Keras vs PyTorch

## Scripts

- `neural_network.py`: Implementación básica desde cero
- `keras_utils.py`: Utilidades para Keras
- `pytorch_utils.py`: Utilidades para PyTorch
- `model_architectures.py`: Arquitecturas de modelos

## Datasets

- `mnist/`: Dígitos escritos a mano
- `cifar10/`: Imágenes de objetos
- `fashion_mnist/`: Prendas de vestir
- `imdb_reviews/`: Críticas de películas

## Frameworks

### TensorFlow/Keras
```python
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
```

### PyTorch
```python
import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(784, 10)

    def forward(self, x):
        return self.linear(x)
```

## Ejercicios

1. Implementar perceptrón desde cero
2. Crear red neuronal para clasificación de MNIST
3. Construir CNN para CIFAR-10
4. Implementar RNN para predicción de series
5. Aplicar transfer learning con ResNet
6. Comparar rendimiento de diferentes arquitecturas

## Recursos

### Cursos
- [Deep Learning Specialization - Coursera](https://www.coursera.org/specializations/deep-learning)
- [Fast.ai Practical Deep Learning](https://course.fast.ai/)

### Libros
- "Deep Learning" - Ian Goodfellow
- "Neural Networks and Deep Learning" - Michael Nielsen

### Tutoriales
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

### Papers
- [ImageNet Classification with Deep CNNs](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

## Tips

- Usar GPU para entrenar modelos grandes
- Empezar con arquitecturas simples
- Monitorear overfitting con validation loss
- Usar callbacks (EarlyStopping, ModelCheckpoint)
- Normalizar inputs entre 0 y 1
- Usar data augmentation para mejorar generalización
