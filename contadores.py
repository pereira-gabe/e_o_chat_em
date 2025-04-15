import requests
import os
from pathlib import Path

URL = "https://raw.githubusercontent.com/pereira-gabe/e_o_chat_em/main/contadores.txt"
FILE_NAME = "contadores.txt"
VSCODE_TERMINAL = True 

def configurar_ambiente():
    """Configura o ambiente para o VS Code"""
    if VSCODE_TERMINAL:
        script_dir = Path(__file__).parent
        contadores_dir = script_dir / "contadores"
        contadores_dir.mkdir(exist_ok=True)
        return contadores_dir / FILE_NAME
    return Path.home() / FILE_NAME

def baixar_arquivo(file_path):
    """Baixa o arquivo do GitHub"""
    try:
        response = requests.get(URL)
        response.raise_for_status()
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"✅ Arquivo baixado com sucesso para:\n{file_path}")
        return True
    except Exception as e:
        print(f"❌ Erro ao baixar o arquivo:\n{e}")
        return False

def carregar_contadores(file_path):
    """Carrega os contadores do arquivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
            return [int(linha) for linha in linhas[:3]]  # Pega apenas os 3 primeiros
    except Exception as e:
        print(f"❌ Erro ao ler contadores:\n{e}")
        return None

def salvar_contadores(file_path, contadores):
    """Salva os contadores no arquivo"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(map(str, contadores)) + "\n\n")
        return True
    except Exception as e:
        print(f"❌ Erro ao salvar contadores:\n{e}")
        return False

def exibir_menu(contadores):
    """Exibe o menu interativo"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🔄 ATUALIZADOR DE CONTADORES (VS Code Terminal)")
    print("═" * 50)
    print(f"1 - Contador GPT          [Atual: {contadores[0]}]")
    print(f"2 - Robô do Tigrinho      [Atual: {contadores[1]}]")
    print(f"3 - Contador de Vírus     [Atual: {contadores[2]}]")
    print("0 - Sair")
    print("═" * 50)
    print(f"📁 Arquivo: {file_path}\n")

def main():
    global file_path
    file_path = configurar_ambiente()

    if not baixar_arquivo(file_path):
        input("\nPressione Enter para sair...")
        return

    contadores = carregar_contadores(file_path)
    if not contadores or len(contadores) < 3:
        input("\nPressione Enter para sair...")
        return

    while True:
        exibir_menu(contadores)
        opcao = input("▶ Escolha uma opção (1-3) ou 0 para sair: ").strip()
        
        if opcao == '0':
            break
        
        if opcao in ('1', '2', '3'):
            idx = int(opcao) - 1
            contadores[idx] += 1
            if salvar_contadores(file_path, contadores):
                print(f"\n✔ Contador {opcao} atualizado para {contadores[idx]}!")
            else:
                print("\n✖ Falha ao atualizar contador!")
        else:
            print("\n⚠ Opção inválida! Use 1, 2, 3 ou 0.")
        
        input("\nPressione Enter para continuar...")

    print("\n🎯 Operação concluída!")
    print(f"📌 Arquivo atualizado em: {file_path}")
    print("⚠ Lembre-se de fazer commit/push das alterações para o GitHub!")

if __name__ == "__main__":
    file_path = None
    main()