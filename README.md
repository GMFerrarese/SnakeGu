🐍 Snake Game — Python & Pygame
Um mini‑game clássico desenvolvido em Python utilizando Pygame, estruturado de forma profissional para portfólio.
O projeto demonstra organização de código, modularização, lógica de jogo e boas práticas de desenvolvimento.

📸 Demonstração
(Adicione aqui um GIF ou imagem do jogo rodando)  
Exemplo:

Código
assets/demo.gif
🚀 Funcionalidades
Movimento fluido da cobra

Sistema de colisão com comida

Crescimento da cobra

Grid baseado em células

Velocidade configurável

Código modular (game, snake, food, settings)

Fácil de expandir (menu, sons, skins, pontuação etc.)

🧱 Estrutura do Projeto
Código
snake-game/
│
├── src/
│   ├── game.py
│   ├── snake.py
│   ├── food.py
│   └── settings.py
│
├── assets/
│   └── demo.gif (opcional)
│
├── tests/
│   └── test_snake.py (opcional)
│
├── requirements.txt
└── README.md

🛠 Tecnologias Utilizadas
Python 3.10+

Pygame

(Opcional) PyScript para rodar no navegador

(Opcional) GitHub Actions para testes automáticos

📦 Instalação
1. Clone o repositório
bash
git clone https://github.com/SEU_USUARIO/snake-game.git
cd snake-game
2. Instale as dependências
bash
pip install -r requirements.txt
▶️ Como Rodar
Execute o arquivo principal:

bash
python src/game.py
A janela do jogo abrirá automaticamente.

⚙️ Configurações
Todas as configurações estão no arquivo:

Código
src/settings.py
Você pode ajustar:

Tamanho da tela

Tamanho das células

FPS

Cores da cobra e da comida

📌 Roadmap (Melhorias Futuras)
Sistema de pontuação

Tela de menu

Tela de game over

Sons e efeitos

Skins para a cobra

Obstáculos

Versão jogável no navegador (PyScript)

📝 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e distribuir.

👤 Autor
Gustavo Marchini Ferrarese
Projeto criado com apoio do Microsoft Copilot.
