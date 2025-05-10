package service;
import model.Aluno;
import java.util.ArrayList;
import java.util.List;

public class AlunoService {

    private List<Aluno> alunos = new ArrayList<>();
    public void cadastrarAluno(Aluno aluno) {
        alunos.add(aluno);
    }

    public List<Aluno> listarAlunos() {
        return alunos;
    }

    public void atualizarAluno(String nome, String novoNome) {
        for (Aluno aluno : alunos) { if
        (aluno.getNome().equalsIgnoreCase(nome)) {
            aluno.setNome(novoNome);
            System.out.println("Aluno atualizado com sucesso!");
            return;
        }
        }
        System.out.println("Aluno não encontrado.");
    }

    public void deletarAluno(String nome){
        for (int i = 0, i < alunos.size(); i++) {
            if (alunos.get(i).getNome().equalsIgnoreCase(nome)){
                alunos.remove(i);
                System.out.println("Aluno deletado com sucesso!");
                return;
            }
        }
        System.out.println("Aluno não encontrado.2");
    }

}
