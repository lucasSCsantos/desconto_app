from src.app.entities.pedido import Pedido
from src.app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.dtos.criar_pedido_input_dto import CriarPedidoDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO

class CriarPedido:
		def __init__ (self, pedido_gateway: IPedidoGateway):
				self.pedido_gateway = pedido_gateway

		def executar(self, input_dto: CriarPedidoDTO) -> Pedido:
				tipo_desconto = input_dto.tipo_desconto.lower().strip()
				if tipo_desconto.lower() == "normal":
						desconto = DescontoNormal()
				elif tipo_desconto.lower() == "vip":
						desconto = DescontoVIP()
				elif tipo_desconto.lower() == "premium":
						desconto = DescontoPremium()
				else:
						raise ValueError("Tipo de desconto inválido, Use 'normal', 'vip' ou 'premium'.")
				
				pedido = Pedido(input_dto.cliente, input_dto.valor_original, desconto)
				self.pedido_gateway.salvar(pedido, tipo_desconto)
			
				return CriarPedidoOutputDTO(
						cliente=pedido.cliente,
						valor_original=pedido.valor_original,
						valor_desconto=pedido.valor_desconto(),
						valor_final=pedido.valor_final(pedido.valor_original),
						tipo_desconto=input_dto.tipo_desconto
				)

		def listar_pedidos(self) -> list[Pedido]:
				pedidos = self.pedido_gateway.listar()
				
				lista_dto = []

				for registro in pedidos:
						pedido = registro["pedido"]
						dto = CriarPedidoOutputDTO(
								cliente=pedido.cliente,
								valor_original=pedido.valor_original,
								valor_desconto=pedido.valor_desconto(),
								valor_final=pedido.valor_final(pedido.valor_original),
								tipo_desconto=registro["tipo_desconto"]
						)
						lista_dto.append(dto)

				return lista_dto
				