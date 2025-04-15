import requests
import os

# URL do arquivo contadores.txt no GitHub
URL = "https://raw.githubusercontent.com/pereira-gabe/e_o_chat_em/main/contadores.txt"
FILE_PATH = "contadores.txt"

def baixar_arquivo():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        with open(FILE_PATH, 'w') as f:
            f.write(response.text)
        return True
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        return False

def carregar_contadores():
    try:
        with open(FILE_PATH, 'r') as f:
            linhas = f.readlines()
            contadores = [int(linha.strip()) for linha in linhas if linha.strip()]
        return contadores
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def salvar_contadores(contadores):
    try:
        with open(FILE_PATH, 'w') as f:
            for contador in contadores:
                f.write(f"{contador}\n\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
        return False

def enviar_para_github():
    # Esta função seria para enviar as mudanças de volta para o GitHub
    # Mas isso requer autenticação e configuração do Git
    # Como isso é complexo e requer credenciais, vou apenas informar o usuário
    print("\nATENÇÃO: O arquivo local foi atualizado, mas as mudanças não foram enviadas para o GitHub.")
    print("Você precisará fazer manualmente o commit e push das alterações.")

def main():
    print("Atualizador de Contadores")
    print("1 - Contador GPT")
    print("2 - Contador Robo do Tigrinho")
    print("3 - Contador de Virus")
    print("0 - Sair")

    if not baixar_arquivo():
        return

    contadores = carregar_contadores()
    if contadores is None or len(contadores) < 3:
        print("Erro: O arquivo não contém os 3 contadores esperados.")
        return

    while True:
        try:
            opcao = int(input("\nEscolha uma opção (1-3) ou 0 para sair: "))
            if opcao == 0:
                break
            elif opcao in [1, 2, 3]:
                indice = opcao - 1
                contadores[indice] += 1
                print(f"Contador {opcao} atualizado para {contadores[indice]}")
            else:
                print("Opção inválida. Escolha 1, 2, 3 ou 0 para sair.")
        except ValueError:
            print("Por favor, digite um número válido.")

    if salvar_contadores(contadores):
        print("\nContadores salvos com sucesso no arquivo local!")
        enviar_para_github()

if __name__ == "__main__":
    main()