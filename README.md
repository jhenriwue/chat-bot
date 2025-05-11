# Chatbot - Assistente para Loja de Esportes

Este projeto é um chatbot interativo em terminal, utilizando o modelo `meta-llama/Llama-3.2-3B-Instruct` da Meta AI via Hugging Face. Ele funciona como um assistente de linguagem natural e pode ser facilmente personalizado para atender clientes em uma loja de artigos esportivos.

---

## Propósito

O objetivo é oferecer um assistente automatizado capaz de:
- Responder perguntas sobre produtos esportivos
- Ajudar clientes com dúvidas comuns (entrega, troca, recomendação)
- Ser executado localmente, com histórico de conversa e comportamento configurável

---

## Requisitos

- Conta no [Hugging Face](https://huggingface.co/)
- Token com acesso ao modelo `meta-llama/Llama-3.2-3B-Instruct`

---

## Configurando o token de acesso

1. Acesse: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Gere um token com:
   - `Read access`
   - `Access to gated models`
3. Crie um arquivo `.env` com o seguinte conteúdo:

```env
HUGGINGFACE_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Como rodar o chatbot

Para rodar o assistente virtual de uma loja de artigos de esportes, siga as instruções abaixo:

---

### 1. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Instale as dependências

```bash
pip install -r requirements.txt
```

## 3. Configurando o token de acesso

1. Acesse: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Gere um token com:
   - `Read access`
   - `Access to gated models`
3. Crie um arquivo `.env` com o seguinte conteúdo:

```env
HUGGINGFACE_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## 4. Execute o Chat Bot

```bash
export $(cat .env | xargs)
python chatbot.py
```


## ✅ Exemplo de uso

    Chatbot (digite 'sair' para encerrar)

    Você: Olá, vocês têm tênis de corrida para pisada neutra?
    Assistente: Claro! Temos diversas opções para pisada neutra...


---