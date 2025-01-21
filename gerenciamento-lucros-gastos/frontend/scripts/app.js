let compras = [];
let vendas = [];

document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault();
    let tipo = document.getElementById('tipo').value;
    let descricao = document.getElementById('descricao').value;
    let valor = parseFloat(document.getElementById('valor').value);
    let quantidade = parseInt(document.getElementById('quantidade').value);

    if (tipo === 'compra') {
        adicionarCompra(descricao, valor, quantidade);
    } else if (tipo === 'venda') {
        adicionarVenda(descricao, valor, quantidade);
    }
});

function calcularLucro() {
    let totalGasto = compras.reduce((total, compra) => total + compra.preco * compra.quantidade, 0);
    let totalVendido = vendas.reduce((total, venda) => total + venda.preco * venda.quantidade, 0);
    let lucro = totalVendido - totalGasto;
    document.getElementById('lucro-total').innerText = `R$ ${lucro.toFixed(2)}`;
}

function adicionarCompra(descricao, preco, quantidade) {
    compras.push({ descricao, preco, quantidade });
    exibirItem('Compra', descricao, preco, quantidade, compras.length - 1, 'compra');
    calcularLucro();
}

function adicionarVenda(descricao, preco, quantidade) {
    vendas.push({ descricao, preco, quantidade });
    exibirItem('Venda', descricao, preco, quantidade, vendas.length - 1, 'venda');
    calcularLucro();
}

function exibirItem(tipo, descricao, preco, quantidade, index, itemType) {
    let lista = document.getElementById('lista-itens');
    let item = document.createElement('li');
    item.innerHTML = `
        <span>${tipo}: ${descricao} - R$ ${preco.toFixed(2)} x ${quantidade}</span>
        <button onclick="excluirItem(${index}, '${itemType}')">Excluir</button>
    `;
    lista.appendChild(item);
}

function excluirItem(index, itemType) {
    if (itemType === 'compra') {
        compras.splice(index, 1);
    } else if (itemType === 'venda') {
        vendas.splice(index, 1);
    }
    atualizarLista();
    calcularLucro();
}

function atualizarLista() {
    let lista = document.getElementById('lista-itens');
    lista.innerHTML = '';
    compras.forEach((compra, index) => {
        exibirItem('Compra', compra.descricao, compra.preco, compra.quantidade, index, 'compra');
    });
    vendas.forEach((venda, index) => {
        exibirItem('Venda', venda.descricao, venda.preco, venda.quantidade, index, 'venda');
    });
}

async function gerarPlanilha() {
    console.log('Gerando planilha...');
    try {
        let response = await fetch('http://localhost:5000/calcular_lucro');
        if (!response.ok) {
            throw new Error('Erro ao calcular lucro');
        }
        let data = await response.json();
        console.log('Dados recebidos:', data);
        let lucroTotal = data.lucro_total;

        let dados = [
            ["Tipo", "Descrição", "Valor", "Quantidade"],
            ...compras.map(compra => ["Compra", compra.descricao, compra.preco, compra.quantidade]),
            ...vendas.map(venda => ["Venda", venda.descricao, venda.preco, venda.quantidade]),
            [],
            ["Lucro Total", "", `R$ ${lucroTotal.toFixed(2)}`, ""]
        ];

        let ws = XLSX.utils.aoa_to_sheet(dados);
        let wb = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wb, ws, "Gastos e Lucros");

        XLSX.writeFile(wb, "gastos_e_lucros.xlsx");
        console.log('Planilha gerada com sucesso');
    } catch (error) {
        console.error('Erro ao gerar planilha:', error);
    }
}