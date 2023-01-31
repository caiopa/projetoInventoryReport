from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "ovo",
        "mantiqueira",
        "13/08/2022",
        "13/08/2023",
        "123456789",
        "xxxxx"
        )

    assert produto.id == 1
    assert produto.nome_do_produto == "ovo"
    assert produto.nome_da_empresa == "mantiqueira"
    assert produto.data_de_fabricacao == "13/08/2022"
    assert produto.data_de_validade == "13/08/2023"
    assert produto.numero_de_serie == "123456789"
    assert produto.instrucoes_de_armazenamento == "xxxxx"
