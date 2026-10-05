import random
import streamlit as st

# Configurazione Pagina
st.set_page_config(
    page_title="FIPAV - Campionato Italiano Beach Volley 2026",
    page_icon="🏐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stile CSS Personalizzato Ufficiale FIPAV (Blu #003399 & Giallo #FFCC00)
st.markdown("""
<style>
    /* Background e Font */
    .stApp {
        background-color: #f4f6f9;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Header Ufficiale FIPAV */
    .fipav-header {
        background: linear-gradient(135deg, #003399 0%, #002266 100%);
        border-bottom: 5px solid #FFCC00;
        color: white;
        padding: 25px 30px;
        border-radius: 8px;
        margin-bottom: 30px;
        box-shadow: 0 4px 12px rgba(0, 51, 153, 0.2);
    }
    .fipav-badge {
        background-color: #FFCC00;
        color: #003399;
        font-weight: 900;
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .fipav-title {
        font-size: 26px;
        font-weight: 800;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .fipav-subtitle {
        font-size: 14px;
        color: #dbeafe;
        margin-top: 5px;
    }

    /* Schede Incontri */
    .fipav-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #003399;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .fipav-card-header {
        font-size: 12px;
        font-weight: 800;
        color: #003399;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 4px;
    }
    .team-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 6px 0;
        font-weight: 700;
        color: #1e293b;
        font-size: 14px;
    }
    .vs-badge {
        text-align: center;
        font-size: 10px;
        font-weight: 900;
        color: #003399;
        background: #eff6ff;
        padding: 2px 0;
        border-radius: 4px;
        margin: 4px 0;
    }
    .next-round {
        margin-top: 10px;
        padding-top: 8px;
        border-top: 1px dashed #cbd5e1;
        font-size: 12px;
        color: #003399;
        font-weight: 600;
    }

    /* Badge Gironi */
    .badge-girone {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 800;
        color: white;
    }
    .badge-A { background-color: #d97706; }
    .badge-B { background-color: #2563eb; }
    .badge-C { background-color: #059669; }
    .badge-D { background-color: #dc2626; }
</style>
""", unsafe_allow_html=True)

# Banner Istituzionale FIPAV
st.markdown("""
<div class="fipav-header">
    <div class="fipav-badge">FEDERAZIONE ITALIANA PALLAVOLO</div>
    <div class="fipav-title">CAMPIONATO ITALIANO ASSOLUTO BEACH VOLLEY 2026</div>
    <div class="fipav-subtitle">Gestione Main Draw 12 Squadre — Regolamento Ufficiale (Allegato 1)</div>
</div>
""", unsafe_allow_html=True)

# --- SEZIONE 1: INSERIMENTO SQUADRE ---
with st.expander("📌 1. FASE A GIRONI — Inserimento Coppie", expanded=True):
    col_a, col_b, col_c, col_d = st.columns(4)
    gironi_input = {}
    gironi_nomi = ['A', 'B', 'C', 'D']
    colonne = [col_a, col_b, col_c, col_d]

    for i, g in enumerate(gironi_nomi):
        with colonne[i]:
            st.markdown(f"#### GIRONE {g}")
            gironi_input[g] = []
            for pos in range(1, 5):
                default_val = f"Coppia {g}{pos}"
                nome = st.text_input(f"Posizione {g}{pos}:", value=default_val, key=f"sq_{g}_{pos}")
                gironi_input[g].append(nome)

# --- SEZIONE 2: CLASSIFICHE GIRONI ---
st.markdown("### 🏆 2. QUALIFICATE AL MAIN DRAW (PRIME 3 PER GIRONE)")
col_q1, col_q2, col_q3, col_q4 = st.columns(4)
col_q = [col_q1, col_q2, col_q3, col_q4]

prime = {}
seconde = []
terze = []

for i, g in enumerate(gironi_nomi):
    with col_q[i]:
        st.markdown(f"**Girone {g}**")
        p1 = st.selectbox(f"1ª Classificata ({g}1):", gironi_input[g], index=0, key=f"p1_{g}")
        rimanenti_p2 = [s for s in gironi_input[g] if s != p1]
        p2 = st.selectbox(f"2ª Classificata ({g}2):", rimanenti_p2, index=0, key=f"p2_{g}")
        rimanenti_p3 = [s for s in rimanenti_p2 if s != p2]
        p3 = st.selectbox(f"3ª Classificata ({g}3):", rimanenti_p3, index=0, key=f"p3_{g}")

        prime[g] = {'nome': p1, 'girone': g}
        seconde.append({'nome': p2, 'girone': g})
        terze.append({'nome': p3, 'girone': g})

st.markdown("---")

# --- SEZIONE 3: RANKING HEAD-TO-HEAD ---
st.markdown("### ⚖️ 3. HEAD-TO-HEAD RANKING (TESTE DI SERIE)")
col_head1, col_head2 = st.columns(2)

with col_head1:
    ab_choice = st.radio(
        "Miglior quoziente tra le vincenti A1 e B1 (Assegna Seed 1):",
        [f"A1: {prime['A']['nome']}", f"B1: {prime['B']['nome']}"]
    )

with col_head2:
    cd_choice = st.radio(
        "Miglior quoziente tra le vincenti C1 e D1 (Assegna Seed 3):",
        [f"C1: {prime['C']['nome']}", f"D1: {prime['D']['nome']}"]
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- SEZIONE 4: GENERAZIONE E RENDERING TABELLONE ---
if st.button("🏐 ES EGUI SORTEGGIO E GENERA TABELLONE MAIN DRAW", type="primary", use_container_width=True):
    s1_girone = 'A' if prime['A']['nome'] in ab_choice else 'B'
    s2_girone = 'B' if prime['A']['nome'] in ab_choice else 'A'
    s3_girone = 'C' if prime['C']['nome'] in cd_choice else 'D'
    s4_girone = 'D' if prime['C']['nome'] in cd_choice else 'C'

    seed1 = prime[s1_girone]
    seed2 = prime[s2_girone]
    seed3 = prime[s3_girone]
    seed4 = prime[s4_girone]

    tabellone_valido = None

    for _ in range(1000):
        d1 = seconde.copy()
        d2 = terze.copy()
        random.shuffle(d1)
        random.shuffle(d2)

        m17 = (d2[0], d1[0])
        m18 = (d2[1], d1[1])
        m19 = (d1[2], d2[2])
        m20 = (d1[3], d2[3])

        partite = [m17, m18, m19, m20]
        conflitto = False

        for sq_a, sq_b in partite:
            if sq_a['girone'] == sq_b['girone']:
                conflitto = True
                break

        if m17[0]['girone'] == s1_girone or m17[1]['girone'] == s1_girone: conflitto = True
        if m18[0]['girone'] == s4_girone or m18[1]['girone'] == s4_girone: conflitto = True
        if m19[0]['girone'] == s3_girone or m19[1]['girone'] == s3_girone: conflitto = True
        if m20[0]['girone'] == s2_girone or m20[1]['girone'] == s2_girone: conflitto = True

        if not conflitto:
            tabellone_valido = (m17, m18, m19, m20)
            break

    if tabellone_valido:
        m17, m18, m19, m20 = tabellone_valido

        st.success("Tabellone generato in conformità con l'Allegato 1 FIPAV 2026.")

        # TESTE DI SERIE
        st.markdown("## 🥇 TESTE DI SERIE — BYE QUARTI DI FINALE")
        c1, c2, c3, c4 = st.columns(4)
        
        seeds = [("SEED 1", seed1), ("SEED 2", seed2), ("SEED 3", seed3), ("SEED 4", seed4)]
        cols = [c1, c2, c3, c4]

        for idx, (label, seed) in enumerate(seeds):
            with cols[idx]:
                st.markdown(f"""
                <div style="background: white; border-radius: 8px; padding: 15px; border-top: 4px solid #FFCC00; border-bottom: 2px solid #003399; box-shadow: 0 2px 6px rgba(0,0,0,0.05); text-align: center;">
                    <span style="font-size: 11px; font-weight: 800; color: #003399; text-transform: uppercase;">{label}</span>
                    <div style="font-size: 16px; font-weight: 800; color: #0f172a; margin: 6px 0;">{seed['nome']}</div>
                    <span class="badge-girone badge-{seed['girone']}">GIRONE {seed['girone']}</span>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # MATCH ROUND OF 12
        st.markdown("## ⚔️ INCONTRI ROUND OF 12 (OTTAVI DI FINALE)")
        
        def render_match_card(match_num, sq1, sq2, seed_attesa, label_seed):
            return f"""
            <div class="fipav-card">
                <div class="fipav-card-header">MATCH #{match_num}</div>
                <div class="team-row">
                    <span>{sq1['nome']} <span style="font-size: 12px; color: #64748b;">(3°{sq1['girone']})</span></span>
                    <span class="badge-girone badge-{sq1['girone']}">G{sq1['girone']}</span>
                </div>
                <div class="vs-badge">VS</div>
                <div class="team-row">
                    <span>{sq2['nome']} <span style="font-size: 12px; color: #64748b;">(2°{sq2['girone']})</span></span>
                    <span class="badge-girone badge-{sq2['girone']}">G{sq2['girone']}</span>
                </div>
                <div class="next-round">
                    ➡️️ Vincente vs <b>{label_seed} ({seed_attesa['nome']})</b> nei Quarti
                </div>
            </div>
            """

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown(render_match_card(17, m17[0], m17[1], seed1, "Seed 1"), unsafe_allow_html=True)
            st.markdown(render_match_card(18, m18[0], m18[1], seed4, "Seed 4"), unsafe_allow_html=True)

        with col_m2:
            st.markdown(render_match_card(19, m19[0], m19[1], seed3, "Seed 3"), unsafe_allow_html=True)
            st.markdown(render_match_card(20, m20[0], m20[1], seed2, "Seed 2"), unsafe_allow_html=True)

    else:
        st.error("⚠️ Impossibile generare un tabellone privo di conflitti con l'attuale combinazione.")
