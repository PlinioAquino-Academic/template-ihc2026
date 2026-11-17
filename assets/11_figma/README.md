# Materiais da Entrega 11

- [`telas/`](telas/): capturas 1440 × 900 das telas e estados F01–F12, usadas no [catálogo da Entrega 11](../../docs/11_figma.md).
- [`prototipo/index.html`](prototipo/index.html): protótipo navegável em HTML (abre localmente no navegador). É a fonte das telas importadas no Figma.
- [`prototipo/gerar_prototipo.py`](prototipo/gerar_prototipo.py): gera `index.html` (`python3 assets/11_figma/prototipo/gerar_prototipo.py`) e a versão autocontida para importação (`--figma arquivo.html`).
- [`prototipo/base_tcc.css`](prototipo/base_tcc.css) e [`prototipo/fonts/`](prototipo/fonts/): CSS e fontes (Barlow, SIL OFL) copiados da interface de demonstração do TCC (`codigo/interface/static/`); [`prototipo/prototipo.css`](prototipo/prototipo.css) contém as revisões das Entregas 6, 9 e 10.
- [`prototipo/img/`](prototipo/img/): radiografia de teste do TCC e a mesma imagem com o mapa de atenção real do modelo de referência.
- `f01.svg`–`f09.svg`, `f10a.svg`–`f10d.svg`, `f11a.svg`, `f11b.svg` e `f12.svg`: pranchas vetoriais editáveis (1440 × 960) preparadas em 11/11/2026, com os mesmos IDs F. Serviram de especificação para as conexões do Figma.

Sobre as pranchas SVG: as radiografias incorporadas provêm dos arquivos `01_imagem_original.png` e `06_gradcam_overlay.png` do TCC da própria equipe, em `TCC-VisaoRaioxContainer/parteEscrita/images/`. O overlay é uma ilustração técnica já existente; seu uso nas pranchas não é uma nova inferência. Identificação, carga, conclusão e responsável são fictícios. Nenhuma precisão/calibração é inferida dessas imagens.

Material histórico, sem status de entrega atual:

- [Estados da Mesa de inspeção](estados_prototipo_pp01_pp06.svg) e [referência detalhada](referencia_mesa_inspecao.md), preservados da Entrega 6. Os códigos PP não substituem os identificadores F.
