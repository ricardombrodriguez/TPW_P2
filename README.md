# Projeto de TPW

## Descrição:

Este projeto foi desenvolvido no âmbito da uc [Tecnologias e Programação Web]. O objetivo do projeto é desenvolver uma aplicação web em Django na qual aplicamos o que aprendemos ao longo das aulas.

O nosso projeto consiste num blog em que um grupo de pessoas pode publicar os seus pensamentos sobre vários temas.
O blog estará dividido em 3 tipos de utilizador:

- Admin: tem a função de gerir toda a plataforma e rever o trabalho dos gestores
- Gestor: aprova as publicações e pode gerir os outros utilizadores e o seu grupo e pode eliminar comentários impróprios
- Autor: escreve as publicações e espera pela aprovação do gestor para que estas fiquem online
- Leitor: consegue apenas ler e comentar as publicações

No entanto, não será necessário ter uma conta de utilizador para ler. Só será necessário um utilizador criar uma conta se quiser comentar as publicações que lê.

As publicações estão associadas a um tópico e têm um estado. O tópico poderá ser variado, por exemplo: política ou desporto.
Os estados das publicações são mais restritos:

- Por Aprovar: à espera da aprovação de um gestor para ficar visível
- Aprovada: disponível para toda a gente ver
- Arquivada: já não está visível

Os estados poderão ser alterados ou poderão ser adicionados mais, do lado do django os valores dos id's dos estados estão guardados em constantes, para podermos utilizar o id do estado diretamente.

O template do projeto foi pensado em grupo e fizemos um esboço à mão do qe pretendíamos que acontecesse. Este esboço pode ser consultado [aqui](./Template_TPW.pdf)

## Funcionalidades:



Para aceder ao site: http://zer0sense.pythonanywhere.com/

### Logins:

- Admin: user: admin | pass: admin
- Gestor: user: bernas | pass: marega123
- Autor: user: reis | pass: ratisse123
- Leitor: user: bulastro | pass: porto123


## Autores:

| NMec | Name | Email |
|--:|---|---|
| 97505| Alexandre Serras | alexandreserras@ua.pt |
| 98008| Gonçalo Leal| goncalolealsilva@ua.pt|
| 98388| Ricardo Rodriguez| ricardombrodriguez@ua.pt|

### Notas:

Para este projeto utilizamos um template gratuito chamado [Admin LTE](https://adminlte.io/) na versão 3.1.0. Este template encontra-se na pasta static.
