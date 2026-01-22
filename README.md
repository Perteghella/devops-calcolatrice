# README

Questo codice contiene una semplice calcolatrice che esegue l'operazione di:
- somma tra due numeri
- sottrazione tra due numeri

Include anche test unitari per verificare il corretto funzionamento della funzione di somma.

Sono presenti anche i file per la creazione di un'immagine Docker, e le pipeline GitHub Actions per il build e il push dell'immagine su Docker Hub.

## Requisiti

- Installare `UV` da https://github.com/astral-sh/uv

- Creare un ambiente virtuale
    - python3 -m venv .venv

    - rm -rf .venv
	- uv venv

- Attivare l'ambiente virtuale
    - source .venv/bin/activate  (Linux/Mac)
    - .venv\Scripts\activate    (Windows)    

- verifica che l'interprete sia quello gisuto
    - which python3 ( Linux/Mac)
    - where python   (Windows)

- Installare le dipendenze
    - pip install -r requirements.txt

    - uv pip compile requirements.in -o requirements.txt
    - uv pip install -r requirements.txt

## Esecuzione normale

```shell
python3 calcolatrice.py
```

## Esecuzione dei test

```shell
pytest -v
```

## Github upload

```shell
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/XXX/devops-calcolatrice.git
git push -u origin main
```

## Docker build

```shell
docker build -f Dockerfile -t devops-calcolatrice:local .
docker run --rm -it devops-calcolatrice:local
```

## Docker Hub upload

### Crea un repository su Docker Hub

Esempio: docker.io/<DOCKERHUB_USERNAME>/devops-calcolatrice

### Aggiungi i secret su GitHub

Nel repo GitHub → Settings → Secrets and variables → Actions → New repository secret

- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN

👉 token generato da Docker Hub (Account Settings → Security → New Access Token)
