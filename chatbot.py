from transformers import pipeline
import torch

# Carrega o modelo
pipe = pipeline(
    "text-generation",
    model="meta-llama/Llama-3.2-3B-Instruct",
    trust_remote_code=True,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    pad_token_id=128001
)

# Começa com uma instrução inicial
history = "<|system|>\nVocê é um assistente de uma loja de esportes chamada Esporte.\
    Seu objetivo é ajudar clientes a encontrar produtos, explicar diferenças entre itens e sugerir equipamentos conforme a necessidade do cliente. \
    Responda sempre de forma clara, amigável e profissional. \
    Se a pergunta for fora desse tema de esporte, avise com educação que não pode ajudar. \
    Se não souber responder algo, diga diretamente que não possui essa informação.\
    Lembre-se: seu foco é artigos de esporte e esportes em geral. \
    Não comente e nem dê sugestão sobre outros possíveis temas, mesmo que o usuário insista. \
    Retorne sempre sem caracteres diferentes como < | e derivados \
    se pedirem outro tema apenas diga que nao sabe e seu foco é esportes"

print("LLaMA Chatbot (digite 'sair' para encerrar)\n")

while True:
    user_input = input("Você: ")

    if user_input.strip().lower() in {"sair", "exit", "quit"}:
        break

    # Monta o prompt com histórico
    prompt = f"{history}<|user|>\n{user_input}\n<|assistant|>\n"

    # Gera resposta
    output = pipe(prompt, max_new_tokens=300, do_sample=True, temperature=0.7)[0]["generated_text"]

    # Extrai só a parte da resposta nova
    resposta = output.split("<|assistant|>")[-1].strip()

    print(f"Assistente: {resposta}\n")

    # Atualiza o histórico de instruções
    history += f"<|user|>\n{user_input}\n<|assistant|>\n{resposta}\n"
