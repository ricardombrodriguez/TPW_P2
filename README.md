# Projeto de TPW

## Descrição:

Este projeto foi desenvolvido no âmbito da uc [Tecnologias e Programação Web]. O objetivo do projeto é desenvolver uma aplicação web em Django na qual aplicamos o que aprendemos ao longo das aulas.

O nosso projeto consiste num blog em que um grupo de pessoas pode publicar os seus pensamentos sobre vários temas.
O blog estará dividido em 4 tipos de utilizadores:

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

#### 

**Admin**:

- Tem acesso a todas as páginas da plataforma.
- Pode filtrar, visualizar e adicionar publicações. Além disso, este pode aprovar publicações 'Por Aprovar' e/ou arquivar publicações com estado 'Aprovado'. As publicações submetidas por Admins são automaticamente submetidas.
- Pode adicionar/remover uma publicação dos favoritos, bem como visualizar a lista da mesma.
- Tem acesso à página de publicações pendentes ('Por Aprovar'), podendo aprovar as publicações na página detalhada das mesmas.
- Tem acesso à página de publicações arquivadas ('Arquivado'), podendo aprovar as publicações na página detalhada das mesmas.
- Tem acesso à página de gestão de utilizadores. Uma vez que o 'Admin' é o grupo com maior nível de permissões, este pode alterar o grupo de outros utilizadores e guardar o novo estado.
- Pode inserir um novo tópico de publicação ou alterar um tópico já existente. Não é permitido inserir ou alterar um tópico para uma designação já existente.



**Gestor**:

- Tem acesso a todas as páginas da plataforma.
- A única diferença entre este e o administrador é que este não tem permissão para gerir utilizadores 'Admin', uma vez que este encontra-se abaixo deste na hierarquia de autorização.







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
