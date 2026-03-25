import streamlit as st
from datetime import datetime

# Configuracao da pagina
st.set_page_config(page_title="Minha Extensao", layout="centered")

st.title("Minha Extensao Pessoal")

# Logica de Horario em Tempo Real
agora = datetime.now()
hora_atual = agora.time()
dia_semana = agora.weekday() # 0=Segunda, 5=Sabado, 6=Domingo

st.subheader("Onde devo estar agora?")

if dia_semana < 5: # Segunda a Sexta
    if hora_atual < datetime.strptime("07:30", "%H:%M").time():
        st.info("Casa: Preparar para o trabalho. Pegar marmita.")
    elif hora_atual < datetime.strptime("17:00", "%H:%M").time():
        st.success("Trabalho: Foco total na Geracao Distribuida.")
    elif hora_atual < datetime.strptime("18:30", "%H:%M").time():
        st.warning("Academia: Janela de treino ate 18:30. Foco!")
    elif hora_atual < datetime.strptime("22:30", "%H:%M").time():
        st.error("Faculdade: Horario de aula e estudos.")
    else:
        st.write("Casa: Chegada e descanso.")

elif dia_semana == 5: # Sabado
    if hora_atual < datetime.strptime("11:10", "%H:%M").time():
        st.info("Aula: Sábado letivo ate 11:10.")
    elif hora_atual < datetime.strptime("13:00", "%H:%M").time():
        st.warning("Academia: Treino rapido pos-aula.")
    elif hora_atual < datetime.strptime("13:20", "%H:%M").time():
        st.success("Logistica: Indo buscar esposa (13:20).")
    else:
        st.write("Casa: Organizacao domestica e familia.")

else: # Domingo
    st.info("Domingo: Preparar marmitas e conferir financas.")

st.divider()

# Abas de Gestao
tab1, tab2 = st.tabs(["Estudos", "Financas"])

with tab1:
    st.write("Pendencias Academicas")
    st.checkbox("Revisar materia do dia")
    st.checkbox("Trabalho semestral")
    st.text_input("Adicionar novo estudo:")

with tab2:
    st.write("Registro de Gastos")
    valor = st.number_input("Valor R$:", min_value=0.0, step=1.0)
    if st.button("Salvar Gasto"):
        st.write(f"Registrado: R$ {valor}")

st.caption("Foco e disciplina. O resultado vem com a constancia.")
