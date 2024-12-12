# Acessivel+ 👨‍🦽👩‍🦯🦻🧩🩼

## 📑 Descrição do Projeto
Projeto Final do Curso da Escola da Nuvem Dev Phython com IA Generativa
Este documento tem como objetivo detalhar os requisitos para o desenvolvimento do projeto "Acessível+", uma plataforma que visa facilitar o acesso à informação sobre acessibilidade em estabelecimentos, utilizando recursos do AWS Bedrock para análise de feedback e promovendo inclusão social.

## 🧮 Conceitos Iniciais:
O Acessível+ promove uma rede colaborativa de PCDs que avaliam locais e ajudam na construção de um ecossistema inclusivo. 
A utilização de IA e APIs externas possibilita não apenas encontrar locais acessíveis, mas também oferecer sugestões baseadas em dados reais e feedbacks personalizados.

## 💻 Tecnologias Utilizadas:
- Utilizar Python 3.8 ou superior para a integração inicial com o modelo Claude Sonnet 3.5 v2 da Anthropic.
- AWS CLI configurado com as credenciais do perfil _iaedn.
- Git para versionamento do código e colaboração.
- Conexão com a internet para instalação de dependências e acesso ao AWS Bedrock.
- Todos os links a serem analisados serão previamente validados e confiáveis.
- ferramenta de gerenciamento de projeto Trello

<img height="25px" alt="Static Badge" src="https://img.shields.io/badge/Phython-E34F26?logo=python&logoColor=ffffff&labelColor=40b93c&color=40b93c&text_size=15&style=for-the-badge"> <img height="25px" alt="Static Badge" src="https://img.shields.io/badge/AWS_-_BadRock_e_CLI-1572B6?logo=AWS&logoColor=ffffff&labelColor=F7DF1E&color=F7DF1E&text_size=15&style=for-the-badge"> <img height="25" alt="Static Badge" src="https://img.shields.io/badge/GitHub-F7DF1E?logo=github&logoColor=ffffff&labelColor=e7191f&color=e7191f&text_size=15&style=for-the-badge"> <img height="25" alt="Static Badge" src="https://img.shields.io/badge/Trello-F7DF1E?logo=trello&logoColor=ffffff&labelColor=1082ce&color=1082ce&text_size=15&style=for-the-badge">

## 🏗️ Arquitetura Inicail
**Linguagem:** Python

**Frameworks:** Flask ou FastAPI (backend), React ou Angular (frontend). (Evolução Futura)

**IA:** Amazon Bedrock (modelos de IA generativa)

**Banco de dados:** DynamoDB ou PostgreSQL. (Evolução Futura)

**Infraestrutura:** AWS Lambda, S3, e API Gateway.(Evolução Futura)

<br>
<img align="center" alt="arquitetura" height="350" src="https://github.com/user-attachments/assets/5fd0c0b8-8b0c-458b-9632-7927d821d677">


## 🎖️ Requerimentos, Extenções e Frameworks
- venv
- streamlit
- streamlit-authenticator
- requests
- pandas
- boto3

# Tutorial de Configuração do Projeto

Este tutorial irá guiá-lo através das etapas para clonar um repositório Git, instalar dependências com `requirements.txt` e logar na AWS Bedrock usando suas chaves de acesso.

## Passos para Configuração

### 1. Clonar o Repositório

Primeiro, clone o repositório desejado em sua máquina local. Use o comando abaixo no seu terminal:

git clone https://github.com/usuario/repo.git
cd repo

### 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)

Para isolar as dependências do projeto, crie e ative um ambiente virtual:

No Windows:
python -m venv venv
venv\Scripts\activate

No macOS/Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o arquivo `requirements.txt`:

pip install -r requirements.txt

### 4. Configurar a AWS CLI

Se você ainda não configurou a AWS CLI, execute o comando abaixo para configurá-la:

aws configure

Insira suas chaves de acesso AWS, região padrão e formato de saída padrão.

### 5. Logar no AWS Bedrock

Para logar no AWS Bedrock, você precisará definir suas chaves de acesso como variáveis de ambiente:

No Windows:
setx AWS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID"
setx AWS_SECRET_ACCESS_KEY "YOUR_SECRET_ACCESS_KEY"

No macOS/Linux:
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"

Certifique-se de substituir `"YOUR_ACCESS_KEY_ID"` e `"YOUR_SECRET_ACCESS_KEY"` pelas suas chaves de acesso reais.

## Pronto!
