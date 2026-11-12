fimport streamlit as st
import sympy as sp
import plotly.graph_objects as go
import numpy as np

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Kalkulator Limit (Kalkulus)",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS untuk Tampilan Modern (Dark Glassmorphism & Typography)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Header Gradient Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4c1d95 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(49, 46, 129, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-banner h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(to right, #e0e7ff, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-banner p {
        margin: 0.5rem 0 0 0;
        color: #cbd5e1;
        font-size: 1.05rem;
    }

    /* Kartu Hasil Utama */
    .result-card {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        border-left: 6px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        margin-bottom: 1.2rem;
    }
    .result-card-error {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        border-left: 6px solid #ef4444;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        margin-bottom: 1.2rem;
    }
    .result-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: #94a3b8;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }

    /* Styling Tombol Submit */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        padding: 0.65rem 1.5rem;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.35);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.55);
    }
</style>
""", unsafe_allow_html=True)

# Hero Banner
st.markdown("""
<div class="hero-banner">
    <h1>⚙️ Kalkulus - Kalkulator Limit</h1>
    <p>Evaluasi limit tingkat lanjut dengan iterasi otomatis Aturan L'Hôpital, analisis deret Taylor, uji kontinuitas, dan grafik.</p>
    <p>Created BY:</p>
    <p>Nama: Angger Jiwa Sembada</p>
    <p>Nim: 261011400131</p>
    <p>Kelas: 01 TPLM 001</p>
</div>
""", unsafe_allow_html=True)

# Inisialisasi Session State untuk Contoh Cepat (Preset)
if "preset_expr" not in st.session_state:
    st.session_state.preset_expr = "(sin(x) - x) / x**3"
if "preset_point" not in st.session_state:
    st.session_state.preset_point = "0"

# Sidebar: Preset Contoh Soal & Panduan
with st.sidebar:
    st.header("⌛ Contoh Soal Cepat")
    st.caption("Klik salah satu tombol di bawah untuk langsung mencoba kasus limit populer:")
    
    if st.button("1. Bentuk 0/0: (sin(x) - x) / x³", use_container_width=True):
        st.session_state.preset_expr = "(sin(x) - x) / x**3"
        st.session_state.preset_point = "0"
    if st.button("2. Bilangan Euler: (1 + 1/x)ˣ", use_container_width=True):
        st.session_state.preset_expr = "(1 + 1/x)**x"
        st.session_state.preset_point = "oo"
    if st.button("3. Eksponensial: (exp(2*x) - 1)/sin(x)", use_container_width=True):
        st.session_state.preset_expr = "(exp(2*x) - 1) / sin(x)"
        st.session_state.preset_point = "0"
    if st.button("4. Diskontinu Loncat: abs(x)/x", use_container_width=True):
        st.session_state.preset_expr = "abs(x) / x"
        st.session_state.preset_point = "0"

    st.divider()
    st.header("📖 Panduan Sintaks 📖")
    st.markdown("""
    * **Pangkat:** `x**2` atau `x^2`
    * **Perkalian:** `2*x` *(wajib pakai `*`)*
    * **Akar:** `sqrt(x)`
    * **Trigonometri:** `sin(x)`, `cos(x)`, `tan(x)`
    * **Logaritma Natural:** `log(x)`
    * **Tak Hingga:** `oo` atau `-oo`
    """)

# Form Input Utama
with st.container(border=True):
    col1, col2, col3, col4 = st.columns([3, 1.3, 1.5, 1.4], vertical_alignment="bottom")
    
    with col1:
        expr_str = st.text_input("Fungsi Matematika f(x):", value=st.session_state.preset_expr)
    with col2:
        point_str = st.text_input("Titik Limit (x → a):", value=st.session_state.preset_point)
    with col3:
        direction_str = st.selectbox(
            "Arah Pendekatan:",
            ["Dua Arah (+-)", "Dari Kanan (+)", "Dari Kiri (-)"]
        )
    with col4:
        submit_btn = st.button("Hitung Limit 🚀", use_container_width=True)

# Logika Perhitungan & Step-by-step
def solve_limit_with_steps(expr, x, point, dir_val):
    steps = []
    dir_latex = "^+" if dir_val == '+' else ("^-" if dir_val == '-' else "")
        
    steps.append({
        "title": "Langkah 1 — Formulasi Awal Limit",
        "desc": f"Mengevaluasi nilai pendekatan fungsi terhadap $x \\to {sp.latex(point)}{dir_latex}$:",
        "latex": f"\\lim_{{x \\to {sp.latex(point)}{dir_latex}}} \\left( {sp.latex(expr)} \\right)"
    })

    if dir_val in ['+', '-']:
        res = sp.limit(expr, x, point, dir=dir_val)
        steps.append({
            "title": f"Langkah 2 — Evaluasi Satu Sisi ({'Kanan' if dir_val == '+' else 'Kiri'})",
            "desc": "Menghitung nilai limit dari arah spesifik:",
            "latex": f"\\lim_{{x \\to {sp.latex(point)}{dir_latex}}} {sp.latex(expr)} = {sp.latex(res)}"
        })
        return res, steps

    lim_left = sp.limit(expr, x, point, dir='-')
    lim_right = sp.limit(expr, x, point, dir='+')
    
    if lim_left != lim_right:
        steps.append({
            "title": "Langkah 2 — Uji Limit Kiri vs Limit Kanan",
            "desc": "Limit kiri dan limit kanan menghasilkan nilai berbeda, maka limit dua arah **tidak ada (DNE)**.",
            "latex": f"\\lim_{{x \\to {sp.latex(point)}^-}} f(x) = {sp.latex(lim_left)} \\neq \\lim_{{x \\to {sp.latex(point)}^+}} f(x) = {sp.latex(lim_right)}"
        })
        return sp.nan, steps

    curr_expr = expr
    num, den = curr_expr.as_numer_denom()
    
    if den != 1 and point.is_finite:
        iteration = 1
        while iteration <= 4:
            try:
                num_val = num.subs(x, point)
                den_val = den.subs(x, point)
                
                is_zero_zero = (num_val == 0 and den_val == 0)
                is_inf_inf = (sp.oo in (sp.Abs(num_val), sp.Abs(den_val)))
                
                if is_zero_zero or is_inf_inf:
                    indet_type = "\\frac{0}{0}" if is_zero_zero else "\\frac{\\infty}{\\infty}"
                    num_diff = sp.diff(num, x)
                    den_diff = sp.diff(den, x)
                    
                    steps.append({
                        "title": f"Langkah {iteration + 1} — Aturan L'Hôpital (Iterasi ke-{iteration})",
                        "desc": f"Substitusi langsung menghasilkan bentuk tak tentu ${indet_type}$. Turunkan pembilang dan penyebut terhadap $x$:",
                        "latex": f"\\lim_{{x \\to {sp.latex(point)}}} \\frac{{{sp.latex(num)}}}{{{sp.latex(den)}}} = \\lim_{{x \\to {sp.latex(point)}}} \\frac{{{sp.latex(num_diff)}}}{{{sp.latex(den_diff)}}}"
                    })
                    
                    num, den = num_diff, den_diff
                    iteration += 1
                else:
                    final_sub = sp.simplify(num_val / den_val)
                    steps.append({
                        "title": f"Langkah {iteration + 1} — Substitusi Akhir",
                        "desc": f"Ekspresi sudah terdefinisi. Substitusikan $x = {sp.latex(point)}$:",
                        "latex": f"\\frac{{{sp.latex(num_val)}}}{{{sp.latex(den_val)}}} = {sp.latex(final_sub)}"
                    })
                    break
            except Exception:
                break

    final_result = sp.limit(expr, x, point)
    return final_result, steps

# Eksekusi Utama (Langsung jalan saat pertama kali dibuka maupun saat tombol ditekan)
try:
    x = sp.Symbol('x', real=True)
    clean_expr_str = expr_str.replace("^", "**")
    expr = sp.sympify(clean_expr_str)
    
    if point_str.strip().lower() in ['oo', 'inf', '+oo']:
        point = sp.oo
    elif point_str.strip().lower() in ['-oo', '-inf']:
        point = -sp.S.Infinity
    else:
        point = sp.sympify(point_str.replace("^", "**"))
        
    dir_val = '+' if "Kanan" in direction_str else ('-' if "Kiri" in direction_str else '+-')
    limit_result, calculation_steps = solve_limit_with_steps(expr, x, point, dir_val)
    
    # Layout Utama: Kiri (Analisis & Steps), Kanan (Grafik Interaktif Plotly)
    left_col, right_col = st.columns([1.15, 1], gap="large")
    
    with left_col:
        if limit_result is sp.nan:
            st.markdown("""
            <div class="result-card-error">
                <div class="result-label">Status Hasil Perhitungan</div>
                <h2 style="color: #f87171; margin: 0;">Limit Tidak Ada (Does Not Exist)</h2>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-card">
                <div class="result-label">Nilai Limit Eksak</div>
            </div>
            """, unsafe_allow_html=True)
            st.latex(f"\\lim_{{x \\to {sp.latex(point)}}} \\left({sp.latex(expr)}\\right) = {sp.latex(limit_result)}")

        # Tab untuk memisahkan Langkah Penyelesaian dan Analisis Lanjutan
        tab1, tab2 = st.tabs(["📝 Langkah Penyelesaian", "🔬 Analisis & Deret Taylor"])
        
        with tab1:
            for step in calculation_steps:
                with st.expander(step["title"], expanded=True):
                    st.write(step["desc"])
                    st.latex(step["latex"])
                    
        with tab2:
            st.markdown("**1. Bentuk Aljabar Sederhana:**")
            st.latex(f"f(x) = {sp.latex(sp.simplify(expr))}")
            
            if point.is_finite:
                st.markdown("**2. Uji Kontinuitas Fungsi:**")
                try:
                    f_at_point = expr.subs(x, point)
                    if f_at_point == limit_result and limit_result.is_finite:
                        st.success(f"Kontinu di $x = {sp.latex(point)}$ karena $f({sp.latex(point)}) = {sp.latex(limit_result)}$.")
                    else:
                        st.warning(f"Diskontinu di $x = {sp.latex(point)}$ (nilai fungsi di titik tersebut tidak sama dengan nilai limit atau tak terdefinisi).")
                except Exception:
                    st.warning(f"Diskontinu di $x = {sp.latex(point)}$.")
                    
                st.markdown("**3. Ekspansi Deret Taylor (Orde 4):**")
                try:
                    taylor = sp.series(expr, x, point, n=4)
                    st.latex(sp.latex(taylor))
                except Exception:
                    st.caption("Ekspansi deret Taylor tidak tersedia untuk titik/fungsi ini.")

    with right_col:
        with st.container(border=True):
            st.subheader("📈 Grafik Fungsi")
            fig = go.Figure()
            f_num = sp.lambdify(x, expr, modules=['numpy'])
            
            if point.is_finite:
                pt_float = float(point)
                span = 4.0
                x_vals = np.linspace(pt_float - span, pt_float + span, 800)
                x_vals = x_vals[np.abs(x_vals - pt_float) > 1e-4]
                
                with np.errstate(all='ignore'):
                    y_vals = f_num(x_vals)
                y_vals = np.where(np.abs(y_vals) > 50, np.nan, y_vals)
                
                # Kurva Fungsi
                fig.add_trace(go.Scatter(
                    x=x_vals, y=y_vals, mode='lines',
                    name=f"f(x) = {expr_str}",
                    line=dict(color='#818cf8', width=3)
                ))
                
                # Garis Vertikal Titik Limit
                fig.add_vline(
                    x=pt_float, line_width=2, line_dash="dash", line_color="#f43f5e",
                    annotation_text=f"x = {point_str}", annotation_position="top right"
                )
                
                # Titik Limit (Lingkaran Hijau Menyala)
                if limit_result is not sp.nan and limit_result.is_finite:
                    lim_float = float(limit_result)
                    fig.add_trace(go.Scatter(
                        x=[pt_float], y=[lim_float], mode='markers',
                        name=f"Limit = {limit_result}",
                        marker=dict(color='#10b981', size=12, line=dict(color='white', width=2))
                    ))
            else:
                x_vals = np.linspace(1, 100, 600) if point == sp.oo else np.linspace(-100, -1, 600)
                with np.errstate(all='ignore'):
                    y_vals = f_num(x_vals)
                y_vals = np.where(np.abs(y_vals) > 50, np.nan, y_vals)
                
                fig.add_trace(go.Scatter(
                    x=x_vals, y=y_vals, mode='lines',
                    name=f"f(x) = {expr_str}",
                    line=dict(color='#818cf8', width=3)
                ))
                if limit_result is not sp.nan and limit_result.is_finite:
                    fig.add_hline(
                        y=float(limit_result), line_width=2, line_dash="dash", line_color="#10b981",
                        annotation_text=f"Asimtot y = {limit_result}"
                    )

            fig.update_layout(
                template="plotly_dark",
                height=430,
                margin=dict(l=20, r=20, t=30, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(15, 23, 42, 0.6)",
                hovermode="x unified",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
            st.caption("💡 Arahkan kursor ke garis grafik untuk melihat koordinat (x, y) secara presisi, atau drag untuk melakukan zoom.")

except Exception as e:
    st.error(f"❌ Terjadi kesalahan sintaks matematika: `{e}`. Cek kembali tanda kurung dan operator perkalian `*`.")
