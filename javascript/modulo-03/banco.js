const banco = {
    conta: "98765",
    saldo: 500,
    tipoConta: "corrente",
    agencia: "45678-3",

    buscarSaldo: function () {
        return this.saldo;
    },

    deposito: function () {
        this.saldo += valor;
    },

    saque: function (valor) {
        this.saldo -= valor;
    },

    numeroConta: function () {
        return this.conta;
    }
};