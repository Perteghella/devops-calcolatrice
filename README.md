# README

Questo codice contiene una semplice calcolatrice che esegue l'operazione di:
- somma tra due numeri
- sottrazione tra due numeri

Include anche test unitari per verificare il corretto funzionamento della funzione di somma.

## Requisiti

- Aver installato UV da https://github.com/astral-sh/uv

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

python3 calcolatrice.py

## Esecuzione dei test

pytest -v


## Github upload

- git init
- git add .
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/Perteghella/devops-calcolatrice.git
- git push -u origin main