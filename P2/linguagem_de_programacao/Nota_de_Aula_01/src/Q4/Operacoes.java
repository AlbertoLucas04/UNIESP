package Q4;

public class Operacoes {

    double saldo = 0.00;
    double deposito, op_deposito;
    double saque, op_saque;
    double transferir, op_transferir;

    public double exibir_saldo(){
        return saldo;
    }

    public double depositar(){
        op_deposito = saldo + deposito;
        return op_deposito;
    }

    public double saque(){
        op_saque = saldo - saque;
        return saque;
    }

    public double transferir(){
        op_transferir = saldo - transferir;
        return transferir;
    }
}
