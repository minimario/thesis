# MIT Thesis Template

This is a working LaTeX scaffold for Alexander F. Gu's MIT EECS PhD thesis.
It is based on Ivan Kuraj's 2024 thesis structure and uses the maintained
`mitthesis` class vendored in this directory.

## Build

```sh
make
```

or directly:

```sh
latexmk -pdf -interaction=nonstopmode main.tex
```

The output is `main.pdf`.

This repository defaults to `pdflatex` because the local Basic TeX install is
missing the `tagpdf` files needed for `\DocumentMetadata` and LuaLaTeX cannot
write its font cache from the sandbox. For the final archival build, install a
full TeX Live distribution and switch `Makefile`/`.latexmkrc` to LuaLaTeX if you
want tagged PDF output.

## Main Files

- `main.tex`: title page metadata, front matter, chapter order, bibliography
- `abstract.tex`: abstract body and supervisor block
- `acknowledgments.tex`: acknowledgments
- `biography.tex`: optional biographical sketch
- `chapters/`: main thesis chapters
- `appendices/`: appendices
- `references.bib`: BibTeX bibliography
- `doi.sty`: vendored DOI-link package required by `mitthesis` on this Basic
  TeX install
- `macros.tex`: shared theorem environments and macros

## Submission Fields To Verify

- thesis title
- advisor name, title, and department
- committee readers
- department acceptor and exact title
- degree month/year and thesis submission date
- copyright/license choice

The template currently uses June 2027 as a compiling placeholder.
