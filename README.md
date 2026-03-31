
---

# Sistema de Confirmação Automatizada - Clínica Terapêutica

## 👥 Equipe Responsável
* [cite_start] **César Kayoma** [cite: 5]
* [cite_start] **Hágape Latan** [cite: 5]
* [cite_start] **Guilherme de Oliveira** [cite: 5]
* [cite_start] **Curso:** Análise e Desenvolvimento de Sistemas - 3º período [cite: 3, 5]
* **Data:** 30 de Março de 2026

---

## 📝 Proposta do Sistema
[cite_start] Este projeto visa solucionar o problema de confirmação manual de sessões em uma clínica terapêutica que utiliza o sistema **Amigo Tech**[cite: 12, 15]. [cite_start]Atualmente, o processo é repetitivo, suscetível a erros humanos e consome elevado tempo administrativo[cite: 31, 32, 33].

[cite_start]A solução proposta automatiza o envio de mensagens via **WhatsApp**, registra as respostas e organiza a agenda para os profissionais, garantindo maior eficiência operacional[cite: 42, 43].

---

## 🛠️ Tecnologias e Configuração do Ambiente
O projeto foi desenvolvido utilizando as seguintes tecnologias:
* [cite_start] **Linguagem:** Python (versátil e multiparadigma)[cite: 85].
* [cite_start] **Framework:** FastAPI (para criação da API REST com suporte a assincronia)[cite: 85].
* [cite_start] **Banco de Dados:** PostgreSQL (Camada de Persistência)[cite: 85].
* [cite_start] **Manipulação de Dados:** Pandas (Processamento da agenda importada)[cite: 85].
* [cite_start] **Interface:** Jinja2 para renderização do frontend[cite: 85].

### Como executar o projeto:
1. Instale as dependências: `pip install -r requirements.txt`.
2. Configure o arquivo `.env` com a sua `DATABASE_URL` do PostgreSQL.
3. Inicie o servidor: `uvicorn app.main:app --reload`.

---

## 🧠 Seção Técnica: Integração de Paradigmas
O sistema foi estruturado para demonstrar a convergência de diferentes paradigmas de programação, garantindo modularidade e escalabilidade:

### 1. Programação Orientada a Objetos (POO)
[cite_start]Aplicada na modelagem das entidades do domínio na pasta `/app/models`[cite: 88]. [cite_start]As classes **Paciente**, **Profissional** e **Sessão** utilizam herança e encapsulamento para representar fielmente as regras de negócio e a estrutura do banco de dados[cite: 89, 90, 92, 93].

### 2. Programação Assíncrona e Orientada a Eventos
[cite_start]Implementada na camada de serviços (`/app/services/whatsapp_service.py`)[cite: 96, 100]. [cite_start]O uso de `async/await` permite que o sistema processe o envio e recebimento de mensagens via API do WhatsApp em segundo plano, sem bloquear as demais tarefas da gestão[cite: 100].

### 3. Arquitetura REST
[cite_start]Utilizada na comunicação entre o frontend e o backend através do **FastAPI**[cite: 101]. [cite_start]Isso promove o desacoplamento entre os componentes, facilitando futuras integrações com o sistema Amigo Tech[cite: 102, 109].

---

## 🚀 Roadmap de Desenvolvimento (MVP)
* [x] Configuração do ambiente e arquitetura base.
* [x] Implementação da camada de persistência (Models e Database).
* [cite_start] [ ] Importação automatizada da agenda via Pandas[cite: 47].
* [cite_start] [ ] Integração com API Oficial do WhatsApp[cite: 48, 80].
* [cite_start] [ ] Painéis analíticos de presença e faltas[cite: 110].

---



