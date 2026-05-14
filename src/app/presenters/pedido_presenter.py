from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO

class PedidoPresenter:
		def apresentar(pedido_dto: CriarPedidoOutputDTO) -> dict:
				return {
						"cliente": pedido_dto.cliente,
						"valor_original": pedido_dto.valor_original,
						"valor_desconto": pedido_dto.valor_desconto,
						"valor_final": pedido_dto.valor_final,
						"tipo_desconto": pedido_dto.tipo_desconto
				}
		
		def apresentar_lista(self, output_dtos: list[CriarPedidoOutputDTO]) -> list[dict]:
				lista_formatada = []

				for output_dto in output_dtos:
						pedido_formatado = self.apresentar(output_dto)
						lista_formatada.append(pedido_formatado)

				return lista_formatada
