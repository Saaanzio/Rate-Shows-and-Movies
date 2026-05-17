# Showrater

Um projeto desenvolvido em Python usando Streamlit e SQLlite.

## Como rodar o projeto

### 1. Criar e ativar o ambiente virtual (Recomendado)

Criar um ambiente virtual (`venv`) para este projeto. 

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Linux/macOS/WSL)
source venv/bin/activate

# Ative o ambiente virtual (Windows)
venv\Scripts\activate
```

### 2. Instalar as dependências

Com o ambiente virtual ativado, você precisará instalar as bibliotecas em `requirements.txt`. 

Se você estiver em um ambiente Unix/Linux/WSL ou tiver a ferramenta `make` instalada, pode usar o comando:
```bash
make install
```

Alternativamente, use o gerenciador de pacotes `pip` diretamente:
```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

Para rodar a aplicação localmente e abrir a interface web, execute:
```bash
make run
```

Ou execute o Streamlit manualmente:
```bash
streamlit run showrater/app.py
```

A aplicação deverá abrir automaticamente no seu navegador. Caso não abra, o Streamlit fornecerá um link com a `URL` no terminal.

<img width="838" height="464" alt="image" src="https://github.com/user-attachments/assets/537b7aa7-1662-48b1-9fa8-460b2280b004" />

<img width="840" height="569" alt="image" src="https://github.com/user-attachments/assets/403427a7-ea26-4f70-b3fd-aa42bda9d13f" />

<img width="866" height="556" alt="image" src="https://github.com/user-attachments/assets/d5f26cae-ae1a-47a1-b5ce-6d34bdf741c1" />



