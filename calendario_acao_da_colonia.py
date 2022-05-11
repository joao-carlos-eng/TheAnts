import datetime
from pytz import timezone

from conexao_sheets import acao_da_colonia
from vars import DIAS


class Acao:
    def __init__(self, indice_da_semana):
        self.timezone = timezone('America/Sao_Paulo')
        self.indice_da_semana = indice_da_semana
        self.dia_corrent = DIAS[self.indice_da_semana]
        self.plan = acao_da_colonia.worksheet(self.dia_corrent)
        self.warzone = None
        self.recomendad = False
        self.hours = datetime.datetime.now(tz=self.timezone).hour
        self.minute = datetime.datetime.now(tz=self.timezone).minute
        self._message = []
        self._acao_da_colonia = acao_da_colonia

        self.evento_warzone()

    def _get_acao_da_colonia(self):
        return self._acao_da_colonia

    def _set_acao_da_colonia(self, value):
        self._acao_da_colonia = value

    def _get_message(self):
        self.recomendar()
        msg = '\n'.join(self._message)

        return msg

    def _set_message(self, value):
        if value:
            self._message.append(value)
        else:
            self._message.append('')

    acao_da_colonia = property(fget=_get_acao_da_colonia, fset=_set_acao_da_colonia)
    message = property(fget=_get_message, fset=_set_message)

    def evento_warzone(self):
        self.warzone = self.plan.cell(1, 1).value
        self.message = self.warzone

    def recomendar(self):
        if self._message[3]:
            self.recomendad = self._message[3]

    def acao(self, next_day):
        if self.hours < 21:
            line = self.hours + 6
            if self.minute >= 5:
                # print(f'Açao da colônia em andamento, termina em {59 - self.minute}min')
                self.message = f'Açao da colônia em andamento.'
                # print(f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}')
                self.message = f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}'
                self.message = self.plan.cell(line, 3).value
            else:
                # print(f'Estamos na fase de intervalo, o proximo ação começa em {5 - self.minute}')
                self.message = f'Estamos na fase de intervalo, o proximo ação começa em {5 - self.minute} min'
                # print(f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}')
                self.message = f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}'
                self.message = self.plan.cell(line, 3).value

        elif self.hours >= 21:
            line = self.hours - 18
            if self.minute >= 5:
                # print(f'Açao da colônia em andamento, termina em {59 - prox_dia.minute}min')
                self.message = f'Açao da colônia em andamento.'
                # print(f'{prox_dia.plan.cell(line, 1).value} ==> {prox_dia.plan.cell(line, 2).value}')
                self.message = f'{next_day.plan.cell(line, 1).value} ==> {next_day.plan.cell(line, 2).value}'
                self.message = next_day.plan.cell(line, 3).value
            else:
                # print(f'Estamos na fase de intervalo, o proximo ação começa em {5 - prox_dia.minute}')
                self.message = f'Estamos na fase de intervalo, o proximo ação começa em {5 - next_day.minute} min'
                # print(f'{prox_dia.plan.cell(line, 1).value} ==> {prox_dia.plan.cell(line, 2).value}')
                self.message = f'{next_day.plan.cell(line, 1).value} ==> {next_day.plan.cell(line, 2).value}'
                self.message = next_day.plan.cell(line, 3).value

        self.acao_da_colonia = self._message[2]
        self.recomendar()


if __name__ == "__main__":
    now = datetime.datetime.now(tz=timezone('America/Sao_Paulo'))
    acao = Acao(now.weekday())

    if now.weekday() == 6:
        prox_dia = Acao(0)
    else:
        prox_dia = Acao(now.weekday() + 1)
    acao.acao(prox_dia)

    print(acao.message)
