# Importando as bibliotecas necessárias
from datetime import datetime
from dataclasses import dataclass

# Definindo a classe Transacao usando dataclass para representar transações
@dataclass
class Transacao:
    tipo: str
    valor: float
    data_hora: datetime
    descricao: str

# Definindo a classe ContaBancaria para representar uma conta bancária
class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial, limite_diario):
        # Inicializando os atributos da conta
        self._nome_titular = nome_titular
        self._saldo = saldo_inicial
        self._transacoes = []  # Lista para armazenar o histórico de transações
        self._limite_diario = limite_diario
        self._limite_diario_utilizado = 0

    @property
    def saldo(self):
        return self._saldo

    @property
    def nome_titular(self):
        return self._nome_titular

    # Método para exibir o saldo atual
    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    # Método para realizar um depósito na conta
    def depositar(self, valor_deposito):
        try:
            if valor_deposito <= 0:
                raise ValueError("O valor do depósito deve ser positivo.")

            # Atualizando o saldo, o limite diário utilizado e registrando a transação
            self._saldo += valor_deposito
            self._limite_diario_utilizado += valor_deposito
            self._registrar_transacao("Depósito", valor_deposito)

            # Exibindo mensagem de sucesso e o saldo atual
            print(f"Valor R$ {valor_deposito:.2f} foi depositado!")
            self.exibir_saldo()

        except ValueError as e:
            # Tratando exceções relacionadas ao depósito e exibindo mensagens de erro
            print(f"Erro: {e}")

    # Método para realizar um saque na conta
    def sacar(self, valor_saque):
        try:
            if valor_saque <= 0:
                raise ValueError("O valor do saque deve ser positivo.")

            # Verificando se o saque ultrapassa o limite diário
            if (self._limite_diario - self._limite_diario_utilizado) < valor_saque:
                raise ValueError("O limite diário de saque foi atingido.")

            # Verificando se há saldo suficiente para o saque
            if valor_saque > self._saldo:
                raise ValueError("Saldo insuficiente!")

            # Atualizando o saldo, o limite diário utilizado e registrando a transação
            self._saldo -= valor_saque
            self._limite_diario_utilizado += valor_saque
            self._registrar_transacao("Saque", valor_saque)

            # Exibindo mensagem de sucesso e o saldo atual
            print(f"Valor R$ {valor_saque:.2f} foi sacado!")
            self.exibir_saldo()

        except ValueError as e:
            # Tratando exceções relacionadas ao saque e exibindo mensagens de erro
            print(f"Erro: {e}")

    # Método privado para registrar uma transação na lista de transações
    def _registrar_transacao(self, tipo, valor):
        # Obtendo a data e hora atual
        data_hora = datetime.now()
        # Criando uma descrição para a transação
        descricao = f"{tipo} de R$ {valor:.2f} em {data_hora.strftime('%d/%m/%Y %H:%M:%S')}"
        # Criando uma instância de Transacao e adicionando à lista de transações
        transacao = Transacao(tipo, valor, data_hora, descricao)
        self._transacoes.append(transacao)

# Criando uma instância da classe ContaBancaria
conta1 = ContaBancaria("Wesney", 200, limite_diario=2000)

# Interagindo com a conta bancária
# Depositar na conta
conta1.depositar(500)

# Sacar da conta
conta1.sacar(100)

# Tentativa de saque que ultrapassa o limite diário
conta1.sacar(100)

# Exibir o histórico de transações
for transacao in conta1._transacoes:
    print(transacao)
