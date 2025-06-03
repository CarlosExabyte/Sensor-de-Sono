Detecção de Sonolência ao Dirigir

Este projeto foi desenvolvido como parte do meu curso de Análise e Desenvolvimento de Sistemas, com foco em aplicações de visão computacional. O sistema detecta quando uma pessoa está com sono analisando por quanto tempo seus olhos permanecem fechados. Se os olhos ficarem fechados por um período prolongado (além de um limite pré-definido), um alarme sonoro é acionado para alertar o usuário.

Arquivos do Projeto
O projeto contém os seguintes arquivos principais:

detector_face_olhos_imagem.py - Detecta rostos e olhos em uma única imagem.

Imagem de Teste	Resultado da Detecção
Imagem Teste	Resultado
detector_face_olhos_webcam.py - Detecta rostos e olhos em tempo real usando a webcam.
Detecção em Webcam

detector_sonolencia.py - Script principal que identifica se a pessoa está com sono usando o vídeo da webcam.

Demonstração:

Imagem Demonstrativa 

TCC - Aplicação em Detecção de Sonolência
Este projeto também serviu como base para meu Trabalho de Conclusão de Curso (TCC), onde explorei técnicas avançadas de visão computacional. O sistema foi testado em diferentes condições de iluminação e com diversos usuários para validar sua eficácia.

Requisitos

Importante:

Baixe o arquivo shape_predictor_68_face_landmarks.dat.bz2 em Shape Predictor 68 features e extraia-o na pasta do projeto com o comando:

bash
bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2  

Instale as dependências usando:

bash
pip install -r requirements.txt  
As principais bibliotecas utilizadas são:

OpenCV

dlib

pygame

numpy

Como Usar
Detecção em Imagem Estática.py
Coloque a imagem desejada na pasta images com o nome test.jpeg ou altere o caminho no código. Execute com:

bash
Soninho.py
Detecção em Tempo Real via Webcam
Execute:

bash
TesteDeWebcam.py
Detecção de Sonolência
Para iniciar o monitoramento contínuo:
Este projeto combina técnicas de processamento de imagem para contribuir com a segurança no trânsito, especialmente na prevenção de acidentes causados por sonolência.