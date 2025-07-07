## 📝 Sistema de Geração de Documentos de Admissão

Este sistema em Python permite **gerar automaticamente documentos personalizados de admissão de funcionários**, utilizando **modelos `.docx`** e a biblioteca `MailMerge`.

> ⚙️ Ideal para empresas que precisam gerar documentos como termos, autorizações e políticas internas de forma rápida e padronizada.

---

### 📌 Funcionalidades

- Menu com seleção da empresa (No meu caso, essa funcionalidade se dá ao fato da empresa possuir 2 CNPJ e documentos diferentes para cada uma delas)
- Preenchimento automático de:
  - Nome
  - Cargo
  - CPF
  - Data de admissão
- Geração de diversos documentos `.docx` com base em modelos
- Criação de pasta específica com os documentos gerados para cada funcionário

---

### 🧩 Pré-requisitos

- Python 3.7 ou superior
- Biblioteca [python-docx-mailmerge](https://pypi.org/project/python-docx-mailmerge/)

Instale com:

```bash
pip install docx-mailmerge
```


---

### 🗂 Estrutura esperada de pastas

```
projeto/
│
├── modelos/
│   ├── SeuDocumento.docx
│   ├── SeuDocumento2.docx
│   ├── ...
│
├── gerar_documentos.py
```

---

### ▶️ Como usar

1. Execute o script com:

```bash
python gerar_documentos.py
```

2. Escolha a empresa (Se for o seu caso).
3. Insira os dados do funcionário.
4. O sistema criará uma pasta com o nome do funcionário (ex: `Gustavo_Henrique/`) e gerará os documentos personalizados dentro dela.

---

### 🛠 Como personalizar para sua empresa

#### 1. Adicione seus próprios modelos

- Crie seus modelos `.docx` e adicione-os na pasta `modelos/`.
- No seu `.docx` use **chaves de mesclagem** como:  
  `{ MERGEFIELD NOME }`, `{ MERGEFIELD CARGO }`, `{ MERGEFIELD CPF }`, `{ MERGEFIELD DATA }` (esses são os nomes usados no código).
- Para criar as chaves de mesclagem, utilize o comando: CTRL + F9, que o campo `{ }` será criado. (Você deve utilizar o comando, para que o `.'docx` entenda que se trata de um campo de mesclagem)

#### 2. Adapte a lista de documentos

No trecho abaixo, adicione ou remova documentos conforme necessário:

```python
if opcao == "1":
    return ['SeuDocumento1.docx', 'SeuDocumento2.docx']
```

#### 3. Adicione campos extras

Se quiser adicionar mais informações (ex: RG, endereço etc.):

- Edite a função `pegar_dados_funcionario()` para incluir mais `input()`
- Atualize os modelos `.docx` com as novas chaves, como `{ MERGEFIELD RG }`
- Garanta que o `dict` retornado por `pegar_dados_funcionario()` contenha esses novos campos

---

### ❓ Exemplo de modelo `.docx`

```text
Declaro que { MERGEFIELD NOME }, CPF { MERGEFIELD CPF }, foi admitido(a) no cargo de { MERGEFIELD CARGO } na data { MERGEFIELD DATA }.
```

---

### 📩 Suporte

Em caso de dúvidas ou sugestões, sinta-se à vontade para abrir uma *issue* ou contribuir com o projeto. Ou caso prefira, mande um e-mail para `gustavohvieir4@gmail.com`
