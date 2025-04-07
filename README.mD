# 🐇 Projeto RabbitMQ - Publisher & Consumer em Python

Este é um projeto simples que demonstra o uso do RabbitMQ com Python utilizando a biblioteca `pika`.

## 📁 Estrutura do Projeto

```
rabbitmq_example/
├── app/
│   ├── __init__.py
│   ├── consumer.py
│   ├── publisher.py
│   └── config.py
├── main_consumer.py
├── main_publisher.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Como Usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Inicie o RabbitMQ

Certifique-se de que o RabbitMQ está rodando localmente na porta 5672.

### 3. Execute o consumer

```bash
python main_consumer.py
```

### 4. Execute o publisher

```bash
python main_publisher.py
```

## 🔧 Tecnologias Usadas

- Python 3.8+
- RabbitMQ
- Pika (cliente RabbitMQ para Python)

## 📄 Licença

Este projeto é apenas para fins de aprendizado.
