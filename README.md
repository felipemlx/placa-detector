# placa-detector
Algoritmo simples utilizando visão computacional (opencv) pra ler a placa de veículos, seguindo alguns passos:<br/>
1º Ler a imagem em escala de cinza
![image](https://github.com/felipemlx/placa-detector/assets/120753841/ea7dc88b-2ded-4520-ab6c-c15fea61a17d)<br/>
2° Identificar a posição da placa pelos contornos, e recortar a imagem original
Imagem após corte:
![image](https://github.com/felipemlx/placa-detector/assets/120753841/ca5671a8-f9e9-4031-9717-dceb78b0a2ab)<br/>
3° Aplicar filtros necessários na imagem cortada (Limiarização/Erosão)
Imagem após aplicação:
![image](https://github.com/felipemlx/placa-detector/assets/120753841/826c4124-9723-4dd3-ae77-417f6e6bbc7a)<br/>
4º Extrair texto utilizando o OCR Tesseract:<br/>
Saída: Placa sem filtro:  “POX4G21<br/>
5º Utilizar REGEX para filtrar somente o texto que seguir as regras definidas. Para placas brasileiras, segue o padrão 3 letras -> 1 número -> 1 letra -> 2 números<br/>
Saída após REGEX: Placa: POX4G21
