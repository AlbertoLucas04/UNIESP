package controller;
import service.AlunoService;
import java.util.List;
import model.Aluno;


public class AlunoController {

    private AlunoService alunoService = new AlunoService();

    public void cadastrarAluno(Aluno aluno) {
        alunoService.cadastrarAluno(aluno);
    }

    public List<Aluno> listarAlunos() {
        return alunoService.listarAlunos();
    }

    public void atualizarAluno(String nome, String novoNome){
        alunoService.atualizarAlunos(nome, novoNome);
    }

    public void deletarAluno(String nome){
        alunoService.deletarAlunos(nome);
    }

}
