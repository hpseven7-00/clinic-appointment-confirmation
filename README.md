# README — Sistema de Confirmação Automatizada para Clínica Terapêutica

Sistema web desenvolvido em Python para automatizar o processo de confirmação de sessões terapêuticas via WhatsApp, reduzindo tarefas manuais e melhorando a organização operacional da clínica.

O projeto está sendo desenvolvido como atividade acadêmica da disciplina de Paradigmas da Programação, aplicando conceitos de Programação Orientada a Objetos, programação assíncrona, arquitetura em camadas e APIs REST.

---

# Índice

1. [Visão Geral do Projeto](#1-visão-geral-do-projeto)
2. [Objetivos do Sistema](#2-objetivos-do-sistema)
3. [Tecnologias Utilizadas](#3-tecnologias-utilizadas)
4. [Configuração do Ambiente](#4-configuração-do-ambiente)
5. [Executando o Projeto](#5-executando-o-projeto)
6. [Arquitetura do Sistema](#6-arquitetura-do-sistema)
7. [Paradigmas Aplicados](#7-paradigmas-aplicados)
8. [Fluxo de Funcionamento](#8-fluxo-de-funcionamento)
9. [Funcionalidades](#9-funcionalidades)
10. [Equipe Responsável](#10-equipe-responsável)

---

# 1. Visão Geral do Projeto

O Sistema de Confirmação Automatizada para Clínica Terapêutica foi desenvolvido para automatizar o processo de confirmação de sessões realizadas por clínicas multidisciplinares.

Atualmente, muitas clínicas realizam esse processo manualmente:

* consultando agendas;
* enviando mensagens individualmente;
* registrando confirmações manualmente;
* organizando listas para profissionais.

O sistema proposto automatiza esse fluxo utilizando processamento de dados, APIs web e integração com serviços de mensagens.

---

# 2. Objetivos do Sistema

## Objetivo principal

Automatizar o envio e gerenciamento de confirmações de sessões terapêuticas.

## Objetivos específicos

* Reduzir o trabalho manual da gestão;
* Melhorar a organização da clínica;
* Centralizar informações de confirmação;
* Automatizar geração de relatórios;
* Aplicar conceitos de engenharia de software e paradigmas de programação.

---

# 3. Tecnologias Utilizadas

| Tecnologia     | Finalidade                          |
| -------------- | ----------------------------------- |
| **Python**     | Linguagem principal do projeto      |
| **FastAPI**    | Desenvolvimento da API REST         |
| **PostgreSQL** | Persistência de dados               |
| **SQLAlchemy** | ORM para comunicação com banco      |
| **Pandas**     | Processamento de agendas importadas |
| **Jinja2**     | Renderização do frontend            |
| **HTML/CSS**   | Interface web                       |
| **Git/GitHub** | Controle de versão                  |

---


# 4. Configuração do Ambiente

## Pré-requisitos

* Python 3.10+
* PostgreSQL instalado
* pip atualizado

Verificando versões:

```bash
python --version
pip --version
```

---

## Criando ambiente virtual

```bash
python -m venv venv
```

---

## Ativando ambiente virtual

### Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

### Windows (CMD)

```cmd
venv\Scripts\activate.bat
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Instalando dependências

```bash
pip install -r requirements.txt
```

---

# 5. Executando o Projeto

## Iniciando servidor

```bash
uvicorn app.main:app --reload
```

Servidor disponível em:

```txt
http://127.0.0.1:8000
```

---

# 6. Arquitetura do Sistema

O sistema foi estruturado utilizando arquitetura em camadas.

## Camada de Modelos

Responsável pela representação das entidades do domínio:

* pacientes;
* profissionais;
* sessões;
* confirmações.

---

## Camada de Serviços

Responsável pelas regras de negócio:

* processamento de agendas;
* envio de mensagens;
* geração de relatórios;
* manipulação de dados.

---

## Camada de Rotas

Responsável pela comunicação HTTP através da API REST.

---

## Camada de Interface

Responsável pela renderização das páginas web utilizando Jinja2.

---

# 7. Paradigmas Aplicados

## Programação Orientada a Objetos

Aplicada na modelagem das entidades do sistema:

* Paciente
* Sessão
* Profissional
* Confirmação

---

## Programação Assíncrona

Utilizada no FastAPI para:

* processamento concorrente;
* envio de mensagens;
* comunicação com APIs externas.

---

## Programação Modular

O sistema foi dividido em módulos independentes:

* models
* services
* routes
* database

Essa abordagem melhora:

* manutenção;
* reutilização;
* organização do código.

---

## Arquitetura Cliente-Servidor

A aplicação segue o modelo cliente-servidor:

* frontend acessa endpoints da API;
* backend processa regras;
* banco armazena os dados.

---

# 8. Fluxo de Funcionamento

## Fluxo principal do sistema

1. Importação da agenda de atendimentos;
2. Processamento dos dados utilizando Pandas;
3. Identificação das sessões do dia seguinte;
4. Geração automática de mensagens;
5. Envio das mensagens via WhatsApp;
6. Registro das respostas;
7. Organização das confirmações;
8. Geração de relatórios por profissional.

---

# 9. Funcionalidades

## Gestão de Agendas

* Importação de agendas;
* Processamento automático;
* Filtragem de sessões.

---

## Confirmação de Sessões

* Envio automático de mensagens;
* Registro de respostas;
* Classificação das confirmações.

---

## Interface Web

* Dashboard administrativo;
* Visualização de sessões;
* Acompanhamento das confirmações.

---

# 10. Equipe Responsável

## César Kayoma

### Líder da Equipe e Desenvolvedor Frontend

Responsável pela construção da interface web do sistema utilizando Jinja2, organização visual da aplicação e integração entre frontend e backend.

### Principais atividades

* Desenvolvimento da interface;
* Estruturação das páginas;
* Integração frontend-backend;
* Organização da experiência do usuário.
* Integração com PostgreSQL;

---

## Hágape Latan

### Desenvolvedor Backend

Responsável pela arquitetura backend do sistema, modelagem de dados e regras de negócio.

### Principais atividades

* Processamento de agendas utilizando Pandas;
* Implementação das regras de negócio;
* Estruturação da camada de serviços.

---

# Informações Acadêmicas

| Informação | Detalhes                              |
| ---------- | ------------------------------------- |
| Curso      | Análise e Desenvolvimento de Sistemas |
| Período    | 3º período                            |
| Disciplina | Paradigmas da Programação             |
| Ano        | 2026                                  |



