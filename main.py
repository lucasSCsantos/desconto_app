from src.database.connection import DatabaseConnection
from src.controllers.pedido_controller import PedidoController
from src.services.pedido_service import PedidoService
from src.models.desconto import DescontoVIP, DescontoPremium, DescontoNormal
from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository

if __name__ == "__main__":
		database = DatabaseConnection()
		repo = PedidoRepository(database=database)
		service = PedidoService(repository=repo)
		controller = PedidoController(service=service)
		
		pedido1 = Pedido(cliente="João", desconto=DescontoNormal())
		pedido1.valor_original = 100.0

		pedido2 = Pedido(cliente="Maria", desconto=DescontoVIP())
		pedido2.valor_original = 200.0

		pedido3 = Pedido(cliente="Carlos", desconto=DescontoPremium())
		pedido3.valor_original = 300.0

		controller.adicionar_pedido(pedido1)
		controller.adicionar_pedido(pedido2)
		controller.adicionar_pedido(pedido3)

		controller.processar_pedidos()