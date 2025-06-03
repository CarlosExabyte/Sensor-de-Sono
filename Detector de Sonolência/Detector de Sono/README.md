
💤 Detecção de Sonolência ao Dirigir
Este projeto foi desenvolvido como parte do curso de Análise e Desenvolvimento de Sistemas, com foco em aplicações práticas de visão computacional. Ele detecta sinais de sonolência analisando, por meio da webcam, por quanto tempo os olhos de uma pessoa permanecem fechados. Caso o tempo ultrapasse um limite pré-definido, um alarme sonoro é acionado para alertar o usuário.

📁 Estrutura do Projeto
O projeto está organizado em scripts modulares:

Detecção em Imagem Estática.py: Detecta rostos e olhos em uma imagem única.

TesteDeWebcam.py: Detecta rostos e olhos em tempo real via webcam.

Detector_de_Sonolencia.py: Script principal para monitoramento de sonolência usando a webcam.

requirements.txt: Lista de dependências do projeto.

pyproject.toml: Utilizado como gerenciador moderno de dependências e configuração do ambiente.

📸 Demonstração Visual
Detecção em imagem estática:

Imagem Teste	Resultado
test.jpeg	✔️ Detecção facial e ocular

Detecção em tempo real:

📷 Webcam ao vivo com alertas sonoros em caso de sonolência detectada.

🎓 Projeto de Conclusão de Curso (TCC)
Este projeto também serviu como base para o Trabalho de Conclusão de Curso (TCC), no qual foram exploradas técnicas de detecção facial, análise temporal de expressões e uso de bibliotecas especializadas para visão computacional. Testes foram realizados em diferentes ambientes e com usuários diversos.

🧰 Requisitos
🔹 Instalação das dependências
Utilize o gerenciador de pacotes padrão:

bash
Copiar
Editar
pip install -r requirements.txt
🔹 Arquivo necessário
Baixe e extraia o preditor facial da dlib:

bash
Copiar
Editar
bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2
Coloque o arquivo .dat extraído na pasta do projeto.

🧠 Principais bibliotecas utilizadas:
OpenCV – Processamento de imagem em tempo real

dlib – Detecção facial e landmarks

pygame – Emissão de alertas sonoros

numpy – Manipulação de arrays e cálculos matriciais

🚀 Como Executar
📷 Detecção em Imagem
Coloque sua imagem em images/ com o nome test.jpeg (ou modifique o caminho no código).

Execute:

bash
Copiar
Editar
python "Detecção em Imagem Estática.py"
🔴 Detecção em Tempo Real
bash
Copiar
Editar
python TesteDeWebcam.py
⏰ Detecção de Sonolência com Alerta
bash
Copiar
Editar
python Detector_de_Sonolencia.py
🛡️ Contribuindo para a Segurança
Este projeto combina tecnologia acessível e técnicas de visão computacional para contribuir com a segurança no trânsito, ajudando na prevenção de acidentes causados por fadiga e sonolência ao volante.

