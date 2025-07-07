from mailmerge import MailMerge
from datetime import datetime
import os

def menu():
    print("╔════════════════════════════════════════╗")
    print("║             *** EMPRESA ***            ║")
    print("╠════════════════════════════════════════╣")
    print("║  [1]  Opção 1: Fitoway                 ║")
    print("║  [2]  Opção 2: F Roiz                  ║")
    print("╚════════════════════════════════════════╝")

def pegar_documentos(opcao):
    if opcao == "1":
        return ['TermoEnquadramento.docx', 'CandidatoAprovado.docx', 'AvaliacaoExperiencia.docx', 
                'DeclaracaoRacial.docx', 'PoliticaInternet.docx', 'AutorizacaoImagemFitoway.docx',
                'TermoConfidencialidadeFitoway.docx', 'ManualConduta.docx', 'FichaEPIFitoway.docx']
    elif opcao == "2":
        return ['TermoEnquadramento.docx', 'CandidatoAprovado.docx', 'AvaliacaoExperiencia.docx', 
                'DeclaracaoRacial.docx', 'PoliticaInternet.docx', 'AutorizacaoImagemFRoiz.docx',
                'TermoConfidencialidadeFRoiz', 'ManualConduta.docx', 'FichaEPIFRoiz.docx']
    else:
        print("Opção inválida. Saindo do programa.")
        return []

def pegar_dados_funcionario():
    nome_funcionario = input("Insira o nome do funcionário: ")
    cargo_funcionario = input("Insira o cargo do funcionário: ")
    cpf_funcionario = input("Insira o CPF do funcionário: ")
    data_admissao = input("Insira a data de admissão do funcionário (dd/mm/yyyy): ")

    try:
        data_admissao = datetime.strptime(data_admissao, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Data inválida. Formato esperado: dd/mm/yyyy.")
        return None
    
    return {"NOME": nome_funcionario, "CARGO": cargo_funcionario, "DATA": data_admissao, "CPF": cpf_funcionario}

while True:
    menu()
    opcao = input("Escolha uma opção (1-2): ")

    if opcao in ["1", "2"]:
        documentos = pegar_documentos(opcao)
        if not documentos:
            break
        
        funcionario_data = pegar_dados_funcionario()
        if funcionario_data is None:
            continue

        nome_base = funcionario_data['NOME'].replace(' ', '_')
        if not os.path.exists(nome_base):
            os.makedirs(nome_base)

        os.chdir(nome_base)

        caminho_modelos = os.path.join('..', 'modelos')

        if not os.path.exists(caminho_modelos):
            print(f"Erro: A pasta 'modelos' não foi encontrada.")
            break

        for modelo_path in documentos:
            try:
                modelo_completo = os.path.join(caminho_modelos, modelo_path)
                if not os.path.exists(modelo_completo):
                    print(f"Erro: O modelo {modelo_path} não foi encontrado na pasta 'modelos'.")
                    continue

                doc = MailMerge(modelo_completo)
                doc.merge(**funcionario_data)

                nome_arquivo = f"{nome_base}_{os.path.splitext(modelo_path)[0]}.docx"
                doc.write(nome_arquivo)
                doc.close()
                print(f"Documento {nome_arquivo} gerado com sucesso!\n")

            except Exception as e:
                print(f"Erro ao processar o documento {modelo_path}: {e}")
        
    elif opcao == "3":
        print("Programa encerrado!")
        break
