const livro = {
    nome: "Harry Potter e o Prisioneiro de Azkaban",
    autor: "J. K. Rowling",
    ano: "1999"
};

const cores = ["azul", "preto", "branco"];

function listarPropriedades(livro) {
    for (const propriedades in livro) {
        console.log(`${propriedades}: ${livro[propriedades]}`)
    }
}
console.log(listarPropriedades(livro))

function listarElementos(cores) {
    for (const elementos of cores) {
        console.log(`${elementos}`)
    }
}
console.log(listarElementos(cores))