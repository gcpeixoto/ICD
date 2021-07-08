html:
	jupyter-book build .

push:
	ghp-import -n -p -f _build/html

latex:
	jupyter-book build . --builder pdflatex

lecture:
	conda env create -f _environment.yml

lecture-on:
	conda activate lecture

lecture-off:
	conda deactivate

# How to update book (see https://jupyterbook.org/publish/gh-pages.html)
# 1. Make changes to the master branch
# 2. Re-build the book
# 3. Push changes to master
# 4. Use ghp-import -n -p -f _build/html to update 
