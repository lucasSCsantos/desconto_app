from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

class PedidoController:
	"""Controlador para gerenciar a interação entre a interface e o serviço de pedidos."""

	def __init__(self, service: PedidoService):
		self.service = service

	def adicionar_pedido(self, pedido: Pedido):
		self.service.adicionar_pedidos(pedido)	
		

	def processar_pedidos(self):
		self.service.processar_pedidos()