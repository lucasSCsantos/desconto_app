import abc

class IDesconto(abc.ABC):
		@abc.abstractmethod
		def calcular(self, valor: float) -> float:
				pass
		
class DescontoNormal(IDesconto):
		def calcular(self, valor: float) -> float:
				return valor * 0.1  # Exemplo de desconto de 10%
		
class DescontoVIP(IDesconto):
		def calcular(self, valor: float) -> float:
				return valor * 0.2  # Exemplo de desconto de 20%
		
class DescontoPremium(IDesconto):
		def calcular(self, valor: float) -> float:
				return valor * 0.3  # Exemplo de desconto de 30%