<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>💻 hello-world</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      font-family: 'Segoe UI', Arial, sans-serif;
      background: #f8fafc;
      color: #212121;
      margin: 0;
      padding: 0 0 50px 0;
    }
    .container {
      max-width: 700px;
      margin: 40px auto 0 auto;
      padding: 32px 24px;
      background: #fff;
      border-radius: 18px;
      box-shadow: 0 4px 24px rgba(60,60,60,0.10);
    }
    h1 {
      font-size: 2.2em;
      margin: 0 0 10px 0;
      letter-spacing: 2px;
    }
    .desc {
      font-size: 1.15em;
      margin-bottom: 20px;
      color: #444;
    }
    .center {
      text-align: center;
      margin: 18px 0 26px 0;
    }
    .badges img {
      margin: 2px 8px;
      vertical-align: middle;
    }
    section {
      margin-bottom: 32px;
    }
    .section-title {
      font-size: 1.14em;
      font-weight: bold;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .checkbox-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .checkbox-list li {
      margin-bottom: 8px;
      font-size: 1.07em;
      display: flex;
      align-items: center;
      gap: 9px;
    }
    .cb-done {
      color: #4caf50;
      font-size: 1.2em;
    }
    .cb-todo {
      color: #ff6666;
      font-size: 1.2em;
    }
    .fake-link {
      border-radius: 4px;
      padding: 2px 8px;
      font-size: 0.92em;
      font-weight: bold;
      display: inline-block;
      margin-left: 7px;
      text-decoration: none;
      cursor: pointer;
      color: #fff;
      background: linear-gradient(90deg, #3366cc,#5599ff);
      box-shadow: 0 0 2px #3366cc44;
      transition: filter 0.18s;
      filter: brightness(1.0);
    }
    .fake-link.yellow { background: linear-gradient(90deg,#ffcc00,#ffd966); color: #212121; }
    .fake-link.red { background: linear-gradient(90deg,#ff6666,#ffb3b3);}
    pre, code {
      background: #222;
      color: #b5f5d0;
      font-size: 1em;
      border-radius: 6px;
      padding: 10px 15px;
      margin: 12px 0;
      white-space: pre;
      line-height: 1.6;
      overflow-x: auto;
      display: block;
    }
    .techs {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 10px;
    }
    .tech-badge {
      background: #3776ab;
      color: #fff;
      padding: 6px 14px;
      border-radius: 16px;
      font-size: 0.95em;
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 8px #3776ab22;
    }
    .sub {
      color: #888;
      font-size: 0.96em;
      margin-top: 4px;
    }
    .tree-view {
      background: #f4f4f4;
      color: #222;
      border-radius: 7px;
      font-family: 'Fira Mono', 'Consolas', monospace;
      padding: 10px 16px;
      font-size: 1em;
      margin-bottom: 8px;
      margin-top: 12px;
      overflow-x: auto;
    }
    .contact {
      margin-top: 12px;
    }
    .contact a {
      color: #3366cc;
      text-decoration: none;
      font-weight: bold;
      transition: color 0.13s;
    }
    .contact a:hover {
      text-decoration: underline;
      color: #254a8a;
    }
    .star {
      margin-top: 24px;
      text-align: center;
      font-size: 1.13em;
      color: #f9a825;
    }
    @media (max-width: 700px) {
      .container {padding: 10px;}
      .tree-view {font-size: 0.97em; padding: 7px 4px;}
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>💻 hello-world</h1>
    <div class="desc">i going to post some information and codes that may be useful for someone reason</div>
    <div class="center badges">
      <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue?style=for-the-badge"/>
      <img src="https://img.shields.io/badge/Linguagem-Python-yellow?style=for-the-badge"/>
      <img src="https://img.shields.io/badge/Contribuições-Bem-vindas-green?style=for-the-badge"/>
    </div>

    <section>
      <div class="section-title">📌 Funcionalidades</div>
      <ul class="checkbox-list">
        <li>
          <span class="cb-done">✔️</span> Compartilhamento de códigos úteis
          <span class="fake-link">Exemplos</span>
        </li>
        <li>
          <span class="cb-done">✔️</span> Informações relevantes para desenvolvedores
          <span class="fake-link yellow">Dicas</span>
        </li>
        <li>
          <span class="cb-todo">⏳</span> Documentação detalhada
          <span class="fake-link red">Em Breve</span>
        </li>
      </ul>
    </section>

    <section>
      <div class="section-title">🚀 Como executar o projeto</div>
      <pre>
# Clone este repositório
git clone https://github.com/yokino-dev/hello-world.git

# Acesse a pasta do projeto
cd hello-world

# Execute o(s) script(s) desejado(s)
python nome_do_arquivo.py
      </pre>
    </section>

    <section>
      <div class="section-title">🛠️ Tecnologias Utilizadas</div>
      <div class="techs">
        <div class="tech-badge">
          <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
          Python
        </div>
      </div>
    </section>

    <section>
      <div class="section-title">🧠 Contexto e Motivação</div>
      <p>
        Este repositório foi criado com o objetivo de compartilhar códigos, dicas e informações que possam ser úteis para outros desenvolvedores ou para quem está começando na área. 
        A ideia é centralizar soluções e aprendizados práticos, tornando o desenvolvimento mais acessível e colaborativo.
      </p>
    </section>

    <section>
      <div class="section-title">🙌 Como Contribuir</div>
      <ol>
        <li>Faça um fork deste repositório</li>
        <li>Crie uma branch com sua feature: <code>git checkout -b minha-feature</code></li>
        <li>Commit suas alterações: <code>git commit -m 'feat: Minha nova feature'</code></li>
        <li>Faça um push para a sua branch: <code>git push origin minha-feature</code></li>
        <li>Abra um Pull Request</li>
      </ol>
      <div class="sub">Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.</div>
    </section>

    <section>
      <div class="section-title">📁 Estrutura de Pastas</div>
      <div class="tree-view">
hello-world/
├── README.md         # Documentação principal do projeto
└── codes/            # Diretório com os códigos-fonte organizados por tema
    ├── Git/          # Exemplos e comandos relacionados ao Git
    ├── Python/       # Scripts e exercícios em Python
    └── Linux/        # Comandos e scripts úteis para ambientes Linux

      </div>
      <div class="sub">A estrutura acima é um exemplo organizado, adaptando conforme o projeto evoluir.</div>
    </section>

    <section>
      <div class="section-title">📢 Contato</div>
      <div class="contact">
        Entre em contato para sugestões, dúvidas ou parcerias:<br>
        <a href="https://github.com/yokino-dev" target="_blank">Perfil GitHub</a>
      </div>
    </section>

    <div class="star">
      ⭐ Se este projeto te ajudou, deixe uma estrela!
    </div>

  </div>
</body>
</html>
