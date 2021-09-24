### Introdução

`README` do projeto `template-artigo-cdia` que contém os arquivos $\LaTeX$ necessários para compilar o modelo para artigos, resumos e relatórios submetidos para o _Cadernos de Introdução à Ciência de Dados_ para o site do [Bacharelado em CDIA da UFPB](http://cdia.ci.ufpb.br).  


### O mínimo que você precisa saber...


#### Adicionar o título

```
\title{seu título aqui}
``` 

#### Adicionar o nome dos autores

```
\author{
	\authorstyle{Prof. Augustus Norius, Dr., \textsuperscript{1,2}} \\ 
   \authorstyle{Prof. Julius Aminius, Ph.D, \textsuperscript{2}} \\ 
   \authorstyle{Tercius Ominis \textsuperscript{3}}
```

#### Adicionar informação institucional
```
	\textsuperscript{1}\institution{Departamento de Computação Científica}\\ 
	\textsuperscript{2}\institution{LX - Laboratório X}\\ 
    \textsuperscript{3}\institution{Bacharelado em Matemática Computacional}
}
```

#### Adicionar resumo 

```
\lettrineabstract{%
Este trabalho tem o objetivo de...
}
```

#### Adicionar conteúdo

##### Seções 

Use o comando `\section{...}`

##### Subseções 

Use o comando `\subsection{...}`

##### Equações 

Use o comando 

```
\begin{align}
z = x + y	
\end{align}
```

##### Listas

Use os comandos: `itemize` ou `enumerate`.

```
\begin{itemize}
	\item Item 1
	\item Item 2
	\item Item 3
\end{itemize}
```

Vide arquivo de exemplo `main.pdf` para mais comandos ou manuais do $\LaTeX$.

### Nota

Para correções e sugestões, contate o Dr. Gustavo OLIVEIRA:
[mailto](mailto:gustavo.oliveira@uerj.br)



