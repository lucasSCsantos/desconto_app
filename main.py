from app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from app.frameworks.database.memory_database import MemoryDatabase
from app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from app.entities.pedido import Pedido
from app.use_cases.criar_pedido import CriarPedido
from app.adapters.controllers.pedido_controller import PedidoController

def main() -> None:
		database = MemoryDatabase()
		repo = MemoryPedidoRepository(database=database)
		criar_pedido_use_case = CriarPedido(repository=repo)
		controller = PedidoController(criar_pedido_use_case=criar_pedido_use_case)
		
		pedido1 = controller.criar_pedido(cliente="Cliente A", valor=100.0, tipo_desconto="normal")
		pedido2 = controller.criar_pedido(cliente="Cliente B", valor=200.0, tipo_desconto="vip")
		pedido3 = controller.criar_pedido(cliente="Cliente C", valor=300.0, tipo_desconto="premium")

		print("Pedidos Criados:")
		print(f"Cliente: {pedido1.cliente}, Valor Original: {pedido1.valor_original}, Desconto: {pedido1.valor_desconto()}, Valor Final: {pedido1.valor_final(pedido1.valor_original)}")
		print(f"Cliente: {pedido2.cliente}, Valor Original: {pedido2.valor_original}, Desconto: {pedido2.valor_desconto()}, Valor Final: {pedido2.valor_final(pedido2.valor_original)}")
		print(f"Cliente: {pedido3.cliente}, Valor Original: {pedido3.valor_original}, Desconto: {pedido3.valor_desconto()}, Valor Final: {pedido3.valor_final(pedido3.valor_original)}")

if __name__ == "__main__":
		main()