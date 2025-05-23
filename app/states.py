from aiogram.fsm.state import StatesGroup, State

class ConsultationStates(StatesGroup):
    waiting_symptoms = State()