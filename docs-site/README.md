# docs-site — Workshop MCP (GitHub Pages)

Sitio estático con las instrucciones del workshop, generado con Jekyll.

## Estructura

```
docs-site/
├── _config.yml              ← Tema (cayman) y navegación
├── index.md                 ← Landing
├── 01-setup.md              ← Fase 0 (CloudFormation)
├── 02-conceptos.md          ← Lecciones 1-3 (conceptual + acceso)
├── 03-tools-server.md       ← Lección 4
├── 04-inspector.md          ← Lección 5
├── 05-cliente.md            ← Lección 6
├── 06-resources-server.md   ← Lección 7
├── 07-cliente-resources.md  ← Lección 8
├── 08-prompts-server.md     ← Lección 9
├── 09-cliente-prompts.md    ← Lección 10
├── 10-demos.md              ← Lecciones 11-13
└── troubleshooting.md
```

## Publicar en GitHub Pages

### Opción A — GitHub Pages desde carpeta `/docs-site`

GitHub Pages espera por defecto `/docs` o la raíz. Dos caminos:

**A.1 — Renombrar la carpeta a `docs/` (recomendado si no colisiona con el `docs/` del workshop):**

En este repo ya existe `docs/` con los insumos del workshop (proposal, talent, templates). Para no romper eso, usa la opción B.

**A.2 — Dejar como `docs-site/` y usar Actions:**

Crea `.github/workflows/pages.yml`:

```yaml
name: Deploy GitHub Pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.2'
      - run: |
          cd docs-site
          bundle init
          bundle add jekyll
          bundle add jekyll-theme-cayman
          bundle exec jekyll build -d ../_site
      - uses: actions/upload-pages-artifact@v3
        with:
          path: _site
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

Luego en **Settings → Pages** configura **Source: GitHub Actions**.

### Opción B — Branch `gh-pages`

```bash
git subtree push --prefix docs-site origin gh-pages
```

Luego en **Settings → Pages → Source: Deploy from a branch → `gh-pages` / root**.

### Opción C — Publicar desde `main` + `/docs-site`

GitHub Pages permite ahora elegir cualquier carpeta:

**Settings → Pages → Source: Deploy from a branch → `main` / `/docs-site`**

Es la opción más simple si no quieres Actions.

## Preview local

```bash
cd docs-site
bundle init
bundle add jekyll jekyll-theme-cayman
bundle exec jekyll serve
# → http://localhost:4000
```

## Cambiar el tema

Edita `_config.yml`:

```yaml
theme: jekyll-theme-minimal   # o cayman, slate, architect, hacker, midnight, etc.
```

Para algo tipo navegación lateral, usa `just-the-docs` (requiere más setup pero es el estándar para docs técnicas).
