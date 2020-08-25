## Python para Modelagem Baseada em Agentes
#### ABM - Projeto

Professor: `Furtado, Bernardo Alves`

Mestrando: `Cardoso, Bruno Baranda`

Pergunta: Quais os **determinantes** da evasão de alunos nos cursos EaD?

Hipótese: É possível inferir, ou aprender, o comportamento do aluno a partir da **experiência observada**.

Entre as características dos cursos destacam-se: tema, carga horária, data de lançamento, época da oferta.

Entre as características dos alunos destacam-se: idade, gênero, escolaridade, UF, data de inscrição e interesse.

Outputs:

1. Evasão (simulada)
2. Resultados/Aprovações (simulados)

Processo:
Cria alunos, Cria cursos, Cria interação. Processo de calibragem no intuito os de descobrir quais são os determinantes.

Uma vez identificado o padrão, será possível ver qual alteração é mais benéfica (gera melhor resultado)...

Comentários: Qual é a diferença entre essa proposta e econometria? Essa proposta é mais flexível, você foge do formato `y = ax + b + erro`. Não é diferente de uma análise de exploratória de dados (dados existentes). Para ser diferente, será necessário avançar de forma prospectiva. Testar padrões para replicar cenários buscando identificar os mecanismos subjacentes (processo gerador de dados).

Comentários(2): Nesta proprosta preliminar foram utilizados dados randomicos para testagem do modelo. Em seguida os dados históricos deverão ser aportados como base de dados para tentar buscar um padrão de comportamento. 

#### How to run

1. Para rodar a simulação uma vez:
`python modelo.py`
