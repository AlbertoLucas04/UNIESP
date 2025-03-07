package Q1;

public class Aluno {

    String nome;
    double nota1, nota2, media;

    public double media_aluno() {

        media = (nota1 + nota2) / 2;
        return media;

    }
}
