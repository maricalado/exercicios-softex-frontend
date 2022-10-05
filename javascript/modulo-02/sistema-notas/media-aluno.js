const n1 = parseFloat(prompt("Informe a primeira nota: "));
const n2 = parseFloat(prompt("Informe a segunda nota: "));
const n3 = parseFloat(prompt("Informe a terceira nota: "));

const media = (n1 + n2 + n3) / 3;
const result = (media >= 7.0) ? "Aprovado. Parabéns!" : "Reprovado. Que pena!";
alert(result)