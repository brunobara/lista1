## Python para Modelagem Baseada em Agentes
#### ABM - Projeto

Professor: `Furtado, Bernardo Alves`

Mestrando: `Cardoso, Bruno Baranda`

Pergunta: Quais os **determinantes** da evasão dos cursos EaD?

Hipótese:  É possível inferir, ou aprender, o comportamento do aluno a partir da **experiência observada**.

Entre as características dos cursos destacam-se: 1. tema, carga horária, data de lançamento, época da oferta.

Entre as características dos alunos destacam-se: 1. idade, gênero, escolaridade, UF, data de inscrição. a. idade = random.uniforme(18, 45) b. genero = random.choice(['male', 'female']) c. uf = random.randint(0, 26) d. data = random... 2. https://github.com/BAFurtado/censo2010

Outputs:

1. Evasão (passada/histórico)
2. Resultados/notas
3. Avaliação qualitativa (curso)

Processo:
Cria alunos, Cria cursos, Cria interação. Processo de calibragem no intuito os de descobrir quais são os determinantes.

Uma vez identificado o padrão, você pode ver qual alteração é mais benéfica...

Comentários: qual é a diferença entre essa proposta e econometria. Essa proposta é mais flexível, você foge do formato y = ax + b + erro. Não é diferente de uma análise de dados exploratória (dados existentes). Para ser diferente, é avançar de forma prospectiva. Testar padrões para replicar cenários -- buscando identificar os mecanismos subjacentes (processo gerador de dados).

#### How to run

1. Para rodar a simulação uma vez:
`python modelo.py`
