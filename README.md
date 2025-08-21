# Finna API Haku

Python-ohjelma joka hakee kirjoja Finna.fi API:sta ISBN-numerolla.

## Asennus

1. Kloonaa tai lataa projekti

2. Luo virtuaaliympäristö:
   
   **Mac/Linux:**
   ```bash
   python3 -m venv finna_venv
   ```
   
   **Windows:**
   ```cmd
   python -m venv finna_venv
   ```

3. Aktivoi virtuaaliympäristö:
   
   **Mac/Linux:**
   ```bash
   source finna_venv/bin/activate
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   finna_venv\Scripts\activate
   ```
   
   **Windows (PowerShell):**
   ```powershell
   finna_venv\Scripts\Activate.ps1
   ```

4. Asenna riippuvuudet:
   ```bash
   pip install -r requirements.txt
   ```

## Käyttö

1. Varmista että virtuaaliympäristö on aktivoitu:
   
   **Mac/Linux:**
   ```bash
   source finna_venv/bin/activate
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   finna_venv\Scripts\activate
   ```
   
   **Windows (PowerShell):**
   ```powershell
   finna_venv\Scripts\Activate.ps1
   ```

2. Aja ohjelma:
   
   **Mac/Linux:**
   ```bash
   python3 finna.py
   ```
   
   **Windows:**
   ```cmd
   python finna.py
   ```

3. Syötä ISBN-numero kun ohjelma pyytää sitä

## Huomioita

- Ohjelma tarkistaa että ISBN ei ole tyhjä ennen haun tekemistä
- Virtuaaliympäristö on aktivoitava aina ennen ohjelman ajamista
- Ohjelma palauttaa JSON-muotoista dataa Finna API:sta
- Windows PowerShell saattaa vaatia execution policy -muutoksen: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` 