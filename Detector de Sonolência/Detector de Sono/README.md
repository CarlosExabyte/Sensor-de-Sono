💤 Detecção de Sonolência ao Dirigir
Este projeto foi desenvolvido como parte do curso de Análise e Desenvolvimento de Sistemas, com foco em aplicações práticas de visão computacional. Ele detecta sinais de sonolência em motoristas ao analisar, em tempo real, por quanto tempo os olhos permanecem fechados. Se esse tempo ultrapassar um limite pré-definido, um alarme sonoro é ativado para alertar o usuário e prevenir possíveis acidentes.

📁 Estrutura do Projeto
O projeto está dividido em três scripts principais:

Detector_de_Sonolencia.py
Script principal que realiza a detecção de sonolência em tempo real com a webcam.

Detecção em Imagem Estática.py
Realiza a detecção de rostos e olhos em uma imagem estática.

TesteDeWebcam.py
Testa a detecção de olhos e rostos em tempo real, sem o sistema de alerta.

Também estão incluídos:

Arquivos de recursos como classificadores Haar, arquivos de áudio e imagens de demonstração.

shape_predictor_68_face_landmarks.dat.bz2: necessário para a detecção precisa de pontos faciais.

📷 Demonstração
O sistema pode ser testado tanto com imagens estáticas quanto com vídeo ao vivo da webcam. Abaixo um exemplo do funcionamento:


🎓 Aplicação no TCC
Este projeto foi utilizado como base para meu Trabalho de Conclusão de Curso (TCC), explorando técnicas de visão computacional, detecção facial e segurança veicular. Ele foi testado em diferentes ambientes e condições de iluminação, com bons resultados na detecção de sinais de fadiga ocular.

📦 Gerenciamento de Dependências com Flit
O projeto utiliza o Flit como gerenciador de pacotes e para empacotamento do projeto.

Requisitos:
Python 3.10+

Flit: instale com pip install flit

Instalando dependências:
bash
Copiar
Editar
flit install --deps production
Ou, se preferir usar o requirements.txt diretamente:

bash
Copiar
Editar
pip install -r requirements.txt
Bibliotecas principais:
opencv-python

dlib

pygame

numpy

▶️ Como Usar
📸 Para imagem estática:
Coloque sua imagem como test.jpeg na pasta correta.

Execute:

bash
Copiar
Editar
python "Detecção em Imagem Estática.py"
📹 Para webcam (teste):
bash
Copiar
Editar
python TesteDeWebcam.py
💤 Para monitoramento de sonolência:
bash
Copiar
Editar
python Detector_de_Sonolencia.py
Certifique-se de que o arquivo shape_predictor_68_face_landmarks.dat está extraído na pasta correta com:

bash
Copiar
Editar
bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2
🚗 Finalidade
Este projeto integra técnicas de visão computacional para promover segurança no trânsito, com foco na prevenção de acidentes por fadiga. Pode ser adaptado para carros inteligentes, aplicações em frotas corporativas e outras soluções em mobilidade.

