const n1 = parseFloat(prompt("Informe a primeira nota: "));
const n2 = parseFloat(prompt("Informe a segunda nota: "));

const notaMin = 21.0 - n1 - n2;

alert("Nota mínima necessária para aprovação: " + notaMin);