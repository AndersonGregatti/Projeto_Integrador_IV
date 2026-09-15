# Abandono Escolar — Projeto Integrador

Estudo de caso sobre abandono escolar na rede municipal de Cubatão-SP, combinando dados oficiais do INEP (Censo Escolar e Taxas de Rendimento, 2024–2025) com um estudo de caso real de frequência escolar (2026), um índice de risco do abandono, uma prova de conceito de Machine Learning e um protótipo de registro digital de frequência.

**Universidade Virtual do Estado de São Paulo (UNIVESP)**
**Polo:** São José dos Campos - SP

## 🔗 Acesse online

- **[📊 Data App — Painel Interativo (Streamlit)](https://appcubatao-t7e2jepdyhxnsahkq8vmj2.streamlit.app/)**
  Painel com 6 abas: Contexto Oficial (INEP), Censo Escolar, Frequência 2026, Machine Learning, Panorama Regional (Brasil → SP → Cubatão) e Mapa das Escolas.

- **[📝 Registro de Frequência — Rede Municipal de Cubatão](./registro_frequencia_cubatao.html)**
  Protótipo web do sistema de chamada digital (baixe o arquivo e abra no navegador, ou visualize o código-fonte pelo link).

## Participantes

| Nome | RA |
|---|---|
| Anderson Gregatti Guimarães | 2212835 |
| Debora Aparecida Cruz da Silva | 2217614 |
| Fabricio Antonio de Souza | 2002383 |
| Marcela Caroline Targino de Oliveira | 2212813 |
| Maria Luiza Ribeiro de Araujo | 23219775 |
| Nicholas Alexandre | 2100534 |
| Paulo Henrique de Melo Freire | 23217869 |
| Rafael Massayoshi Itami | 2220270 |

## Estrutura do projeto

├── app.py # Data app interativo (Streamlit) — demo online acima
├── Texto_Final_PI_Abandono_Escolar.docx # Texto final do PI (capa, desenvolvimento, resultados, conclusão)
├── Relatorio_PI_Abandono_Escolar_Cubatao.docx # Relatório de metodologia, para aprovação do grupo
├── Relatorio_Registro_Frequencia.docx # Relatório explicativo do protótipo de registro
├── registro_frequencia_cubatao.html # Protótipo web (abre direto no navegador)
├── notebook_pi/
│ ├── PI_Abandono_Escolar_Cubatao.ipynb # Notebook principal: Censo, Taxas de Rendimento, estudo de caso, índice de risco
│ └── dados/ # CSVs usados pelo notebook principal
├── notebook_ml/
│ ├── PI_ML_Prova_de_Conceito_Evasao.ipynb # Notebook de Machine Learning
│ └── dados/ # Base UCI + dados da extensão de Cubatão
└── dados_escola_cubatao_completo/ # Pasta usada pelo app.py e pelos notebooks (mesmos dados)


## Como abrir

- **Data app (.py):** acesse direto pelo link acima, ou rode localmente com `pip install -r requirements.txt` e `streamlit run app.py`.
- **Notebooks (.ipynb):** abrir com Jupyter Notebook/JupyterLab, mantendo a pasta `dados/` (ou `dados_escola_cubatao_completo/`, conforme o notebook) ao lado do arquivo.
- **Protótipo (.html):** basta dar duplo clique — abre em qualquer navegador, sem instalar nada.
- **Relatórios (.docx):** abrir no Word ou similar (Google Docs, LibreOffice).

## Transparência dos dados

O projeto combina dados **reais** (Censo Escolar, Taxas de Rendimento do INEP, chamada digitalizada de 7º a 9º ano de uma escola municipal) com dados **fictícios/simulados** (6º ano do estudo de caso, turno da tarde, rótulo de resultado na extensão de Machine Learning). Cada fonte está identificada nos próprios arquivos (coluna `origem`) e detalhada na Seção 2 do `Texto_Final_PI_Evasao_Escolar.docx`.

## Principais fontes de dados

- INEP — Censo Escolar da Educação Básica, 2024 e 2025
- INEP — Taxas de Rendimento Escolar, 2024 e 2025
- Realinho, V. et al. (2021). *Predict Students' Dropout and Academic Success*. UCI Machine Learning Repository. DOI: 10.24432/C5MC89
- Dados Escola Municipal Cubatão - 7ª serie - 2026