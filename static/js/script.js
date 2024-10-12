const formulario = document.getElementById('formularioEnvio');
const METHOD = 'POST';
const URL_ENVIA_EMAIL = '/enviaEmail';

formulario.addEventListener('submit', (event) => {

    const dadosFormulario = transformaFormulario(event);

    executarTarefas(dadosFormulario);
});

function base64Encode(username, password) {
    const encodedString = btoa(username + ':' + password);
    return encodedString;
}

function transformaFormulario(event) {

    event.preventDefault();

    let campo_nome = document.getElementById('nome').value;
    let campo_email = document.getElementById('email').value;
    let campo_telefone = document.getElementById('telefone').value;
    let campo_mensagem = document.getElementById('mensagem').value;
    let categoria = document.getElementById('categoria').value;

    if (!campo_nome) {
        alert('Por favor, preencha o campo nome.');
        return;
    }

    if (!campo_email) {
        alert('Por favor, preencha o campo Email.');
        return;
    }

    // Criar um objeto com os dados a serem enviados
    const dados = {
        assunto: "Contato Parnaíba Connect",
        nome: campo_nome,
        email: campo_email,
        telefone: campo_telefone,
        texto: campo_mensagem,
        tipo_contato: categoria
    };

    return dados
}

function constroeHeader(valor1, valor2) {
    console.log("valor1: " + valor1);
    console.log("valor2: " + valor2);

    let headers = new Headers();
    const encodedCredentials = base64Encode(valor1, valor2);
    headers.append('Authorization', 'Basic ' + encodedCredentials);
    headers.append('Content-Type', 'application/json');

    return headers

}

function getproperti() {
    fetch('/busca_prop')
        .then(response => response.json())
        .then(data => {

            return new Promise(resolve => {
                // Execução da tarefa
                setTimeout(() => {
                    let headerGerado = constroeHeader(data["valor1"], data["valor2"]);
                    console.log('Tarefa 1 concluída');
                    resolve(headerGerado);
                }, 2000);
            });
        })

}

function envia_email(url, header, method, dados) {
    fetch(url, {
        method: method,
        headers: header,
        body: JSON.stringify(dados)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao enviar a mensagem!');

            }
            return new Promise(resolve => {
                console.log('Tarefa 2 iniciada com resultado:');
                // Simulando outra tarefa assíncrona
                setTimeout(() => {
                    console.log('Tarefa 2 concluída');
                    resolve(response.json());
                }, 1000);
            });

        })
        .then(data => {
            console.log('Resposta da API:', data);
            // Exibir uma mensagem de sucesso ao usuário
            alert('Mensagem enviada com sucesso!');
        })
        .catch(error => {
            console.error('Erro:', error);
            // Exibir uma mensagem de erro ao usuário
            alert('Ocorreu um erro ao enviar a mensagem!');
        });

    return new Promise(resolve => {
        console.log('Tarefa 2 iniciada com resultado:');
        // Simulando outra tarefa assíncrona
        setTimeout(() => {
            console.log('Tarefa 2 concluída');
            resolve('Resultado da tarefa 2');
        }, 100);
    });
}

async function executarTarefas(dados) {
    const header = await getproperti();
    const envio = await envia_email(URL_ENVIA_EMAIL, header, METHOD, dados);
}