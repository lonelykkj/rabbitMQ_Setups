# 🐇 Projeto Exemplo com RabbitMQ - Publisher & Consumer

Este é um projeto simples que demonstra o uso do **RabbitMQ** com **Python** utilizando a biblioteca `pika`.  
Ele possui dois arquivos principais:

- `publisher.py`: responsável por publicar mensagens.
- `consumer.py`: responsável por consumir mensagens de uma fila.


## 🧱 Estrutura do Projeto

```
.
├── consumer.py
├── publisher.py
└── README.md
```


## 📦 Requisitos

- Python 3.8+
- RabbitMQ rodando localmente (porta padrão `5672`)
- Instalar dependências com:

```bash
pip install pika
```


## 🚀 Como Usar

### 1. Inicie o RabbitMQ

Certifique-se de que o RabbitMQ está rodando localmente.

### 2. Execute o Consumer

Este script ficará escutando a fila chamada `data_queue`:

```bash
python consumer.py
```

### 3. Execute o Publisher

Este script enviará uma mensagem `{'Hello': 'World!'}` para o RabbitMQ:

```bash
python publisher.py
```

Você verá a mensagem sendo exibida no terminal do consumidor.


## 🧠 Observações Técnicas

- O `consumer.py` consome mensagens da fila `data_queue`.
- O `publisher.py` publica mensagens no exchange `data_exchange` com routing key vazio (`''`).
- Ambos usam credenciais padrão (`guest`/`guest`) e se conectam ao host `localhost`.


## 📄 Licença

Este projeto é apenas para fins de aprendizado e demonstração.

