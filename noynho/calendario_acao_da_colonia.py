import datetime
from pytz import timezone

from conexao_sheets import acao_da_colonia
from vars import DIAS


class Acao:
    def __init__(self, indice_da_semana):
        self.timezone = timezone('America/Sao_Paulo')
        self.indice_da_semana = indice_da_semana + 1
        self.dia_corrent = DIAS[self.indice_da_semana]
        self.plan = acao_da_colonia.worksheet(self.dia_corrent)
        self.warzone = None
        self.recomendad = False
        self.hours = datetime.datetime.now(tz=self.timezone).hour
        self.minute = datetime.datetime.now(tz=self.timezone).minute
        self.message = []
        self.acao_da_colonia = ''

        self.evento_warzone()

    def evento_warzone(self):
        self.warzone = self.plan.cell(2, 1).value

    def acao(self, next_day):
        line = 0
        if self.hours < 21:
            line = self.hours + 6
            if self.minute > 5:
                # print(f'Açao da colônia em andamento, termina em {59 - self.minute}min')
                self.message.append(f'Açao da colônia em andamento, termina em {59 - self.minute} min')
                # print(f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}')
                self.message.append(f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}')
            else:
                # print(f'Estamos na fase de intervalo, o proximo ação começa em {5 - self.minute}')
                self.message.append(f'Estamos na fase de intervalo, o proximo ação começa em {5 - self.minute} min')
                # print(f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}')
                self.message.append(f'{self.plan.cell(line, 1).value} ==> {self.plan.cell(line, 2).value}')
        elif self.hours >= 21:
            line = self.hours - 18
            if self.minute > 5:
                # print(f'Açao da colônia em andamento, termina em {59 - prox_dia.minute}min')
                self.message.append(f'Açao da colônia em andamento, termina em {59 - next_day.minute} min')
                # print(f'{prox_dia.plan.cell(line, 1).value} ==> {prox_dia.plan.cell(line, 2).value}')
                self.message.append(f'{next_day.plan.cell(line, 1).value} ==> {next_day.plan.cell(line, 2).value}')
            else:
                # print(f'Estamos na fase de intervalo, o proximo ação começa em {5 - prox_dia.minute}')
                self.message.append(f'Estamos na fase de intervalo, o proximo ação começa em {5 - next_day.minute} min')
                # print(f'{prox_dia.plan.cell(line, 1).value} ==> {prox_dia.plan.cell(line, 2).value}')
                self.message.append(f'{next_day.plan.cell(line, 1).value} ==> {next_day.plan.cell(line, 2).value}')

        self.acao_da_colonia = self.plan.cell(line, 2).value
        # print(self.message)
        return self.message


if __name__ == "__main__":
    now = datetime.datetime.now(tz=timezone('America/Sao_Paulo'))
    acao = Acao(now.weekday())

    print(DIAS[now.weekday()])
    print(datetime.datetime.now())

    if now.weekday() == 6:
        prox_dia = Acao(0)
    else:
        prox_dia = Acao(now.weekday() + 1)
    acao.acao(prox_dia)

    print(acao.message[1])