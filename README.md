
# YourJarvis

A API YourJarvis cria uma interação por áudio com uma inteligência artificial. Envie comandos de voz para obter respostas da mesma forma, proporcionando uma comunicação prática.


## Documentação da API

#### Recebe um arquivo de aúdio

```http
  POST /your_jarvis
```

| Tipo       | Descrição                           |
| :--------- | :---------------------------------- |
|`file` | Arquivo de aúdio (**.wav**). |

#### Retorna um item

| Tipo       | Descrição                                   |
| :--------- | :------------------------------------------ |
| `file` |  Arquivo de aúdio (**.mp3**). |



## Uso/Exemplos

```python
import requests
import os

url = "http://127.0.0.1:8000/your_jarvis/"
file = {"file": open("output.wav", "rb")}

response = requests.post(url, files=file)

with open("File.mp3", "wb") as file:
    file.write(response.content)

os.system("File.mp3")
```


## Roadmap

- Adicionar interação com tarefas.

