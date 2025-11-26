from django.core.exceptions import ValidationError
from ..models import Raca

class RacaService:
    @staticmethod
    def listar_racas(nome = None):
        racas = Raca.objects.all()
        if nome:
            return racas.filter(nome__icontains=nome)
        return racas

    @staticmethod
    def cadastrar_raca(Nome):
        raca = Raca(
            nome = Nome
        )
        try:
            raca.full_clean()
        except ValidationError as e:
            raise e
        raca.save()
        return raca

    @staticmethod
    def atualizar_raca(nome, newnome):
        raca = (nome)
        raca.nome = newnome
        return raca

    @staticmethod
    def excluir_raca(nome):
        raca = RacaService.listar_racas(nome).first()
        if raca:
            raca.delete()
        return True
