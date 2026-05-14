from app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from app.frameworks.database.memory_database import MemoryDatabase
from app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from app.entities.pedido import Pedido
from app.use_cases.criar_pedido import CriarPedido
from app.adapters.controllers.pedido_controller import PedidoController
from app.presenters.pedido_presenter import PedidoPresenter

def main() -> None:
		database = MemoryDatabase()
		pedido_gateway = MemoryPedidoRepository(database=database)
		criar_pedido_use_case = CriarPedido(pedido_gateway=pedido_gateway)
		presenter = PedidoPresenter()
		controller = PedidoController(criar_pedido_use_case=criar_pedido_use_case, presenter=presenter)

		pedido1 = controller.criar_pedido(cliente="Cliente A", valor=100.0, tipo_desconto="normal")
		pedido2 = controller.criar_pedido(cliente="Cliente B", valor=200.0, tipo_desconto="vip")
		pedido3 = controller.criar_pedido(cliente="Cliente C", valor=300.0, tipo_desconto="premium")

		print("Pedidos Criados:")
		print(pedido1)
		print(pedido2)
		print(pedido3)

		print("\Pedidos Salvos:")
		for pedido in controller.listar_pedidos():
				print(pedido)
				
if __name__ == "__main__":
		main()