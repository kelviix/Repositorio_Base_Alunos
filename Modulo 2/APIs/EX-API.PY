
import requests
print("BEM VINHOS! \n" )
while True:
    Mesas_disponioveis=requests.get('https://68dd8c1ad7b591b4b78cc278.mockapi.io/Restaurante').json()
    option=input(' 0- Para ver o cardapio \n 1 Para ver as Mesas disponiveis  \n 2- Para fazer um pedido \n 3-Para Alterar um pedido \n 4-Para deletar o seu pedido \n 5-Para fechar o cardapio  ')

    if option =='0':
        print('1.Pão integral com ovo mexido e abacate \n 2.Tapioca com queijo branco e orégano \n 3.Iogurte natural com granola e frutas \n 4.Sanduíche natural de frango desfiado com cenoura ralada \n 5.Banana com pasta de amendoim \n 6.Panqueca de aveia com mel\n 7.Bolinho de batata-doce com frango\n 8.Wrap de alface com atum e cream cheese\n 9.Biscoito de arroz com cottage e tomate\n10.Mix de castanhas e frutas secas')
        print(' 1. Suco verde (couve, limão, maçã e gengibre)\n2. Água com gás e limão\n3. Chá gelado de hibisco com hortelã\n    4. Smoothie de morango com banana\n    5. Leite vegetal com cacau (sem açúcar)\n    6. Água de coco natural\n    7. Café preto sem açúcar \n   8. Suco de maracujá natural\n9. Vitamina de mamão com aveia\n 10. Chá de camomila com limão (quente ou gelado)')
    
    elif option == '1':
        print('Mesas Disponives Abaixo ')
        for item in Mesas_disponioveis:
           print(item.get('Mesa'))

    elif option == '2':

        Bebida=input("Digite sua Bebida")
        Prato=input("Digite seu prato ")
        Mesa=input('Digite sua mesa desejada ')
        print("pedido realizado com sucesso")
        Pedido={
            'Bebidas': Bebida,
            'Prato': Prato,
            'Mesa':Mesa
        }
        requests.post("https://68dd8c1ad7b591b4b78cc278.mockapi.io/Restaurante" ,Pedido)

    if option == "3": 
        Mesas_disponioveis=requests.get('https://68dd8c1ad7b591b4b78cc278.mockapi.io/Restaurante').json()
        for item in Mesas_disponioveis:
            print(item.get('id'))
        

        id=input("Digite numero do seu Id")
        Mesa=input("Digite a Mesa ")
        Bebida=input('Digite a bebida ')
        Prato=input("Digite o prato")

        print('Pedido alterado!')
        alteracao={
           'Mesa':Mesa,
           'Bebidas':Bebida,
           'Prato':Prato
        }
        requests.put(f"https://68dd8c1ad7b591b4b78cc278.mockapi.io/Restaurante/{id}",alteracao)
        


    if option == '4':
        print( 'Veja os Ids e veja qual e a sua')
        for item in Mesas_disponioveis:
             print(item.get('id'))

        id=input("Digite o id do pedido de para ser removido ")
        requests.delete(F"https://68dd8c1ad7b591b4b78cc278.mockapi.io/Restaurante/{id}")

        print('removido com sucesso ')
    

    if option == '5':
         print("Volte sempre!")
         break;


















    


