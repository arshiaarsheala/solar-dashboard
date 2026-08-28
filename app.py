import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- پیکربندی اولیه صفحه ---
st.set_page_config(
    page_title="داشبورد مدیریت سبد نیروگاه‌های خورشیدی",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- استایل‌های اختصاصی و فونت وزیرمتن ---
st.markdown("""
<link href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css" rel="stylesheet" type="text/css" />
<style>
    html, body, [class*="css"], .stMarkdown, .stText, h1, h2, h3, h4, h5, h6, p, div, span {
        font-family: 'Vazirmatn', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 12px;
        padding: 20px;
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid #334155;
        border-top: 4px solid #f59e0b;
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-title {
        font-size: 13px;
        color: #94a3b8;
        font-weight: 500;
        margin-bottom: 8px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -0.5px;
    }
    .metric-unit {
        font-size: 12px;
        color: #f59e0b;
        font-weight: 400;
        margin-right: 4px;
    }

    .info-box {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 10px;
        padding: 16px;
        border-right: 4px solid #3b82f6;
        margin-bottom: 15px;
        border: 1px solid #334155;
    }
    .success-box {
        background: rgba(16, 185, 129, 0.08);
        border-radius: 10px;
        padding: 14px;
        border-right: 4px solid #10b981;
        margin-bottom: 12px;
        border: 1px solid rgba(16, 185, 129, 0.2);
    }
    .strategy-box {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(30, 41, 59, 0.6) 100%);
        border-radius: 10px;
        padding: 18px;
        border-right: 4px solid #f59e0b;
        margin-top: 15px;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        direction: rtl;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Vazirmatn' !important;
        font-weight: 600;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- هدر داشبورد ---
col_logo, col_header = st.columns([1, 6])
with col_header:
    st.title("☀️ داشبورد مدیریت سبد نیروگاه‌های خورشیدی")
    st.caption("سامانه پایش فنی، مانیتورینگ O&M، تحلیل مالی بورس انرژی و توسعه پروژه‌ها")

# --- تب‌های اصلی ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 نمای کلی سبد",
    "📝 برنامه هفتگی و Action Plan",
    "📈 تحلیل مالی و استراتژی بورس",
    "🔧 پایش O&M و تولید",
    "🏗️ پروژه‌های احداث و توسعه"
])

# ==========================================
# تب اول: نمای کلی سبد
# ==========================================
with tab1:
    st.subheader("📌 خلاصه وضعیت تجمیعی سبد نیروگاه‌ها")
    
    kpi_cols = st.columns(4)
    with kpi_cols[0]:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">ظرفیت کل نامی سبد</div>
                <div class="metric-value">۱۹.۰ <span class="metric-unit">MW</span></div>
            </div>
        """, unsafe_allow_html=True)
    with kpi_cols[1]:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">ظرفیت در حال بهره‌برداری (مدار)</div>
                <div class="metric-value">۱۱.۰ <span class="metric-unit">MW</span></div>
            </div>
        """, unsafe_allow_html=True)
    with kpi_cols[2]:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">ظرفیت در حال احداث و تکمیل</div>
                <div class="metric-value">۸.۰ <span class="metric-unit">MW</span></div>
            </div>
        """, unsafe_allow_html=True)
    with kpi_cols[3]:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-title">درآمد وصولی تجمیعی (۶ ماهه)</div>
                <div class="metric-value">۸,۴۲۹ <span class="metric-unit">میلیون تومان</span></div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    col_t1_left, col_t1_right = st.columns([1, 1])
    with col_t1_left:
        st.markdown("#### ⚡ تفکیک ظرفیت پروژه‌ها")
        df_plants = pd.DataFrame({
            "plant_name": ["نواندیشان ۱ (انارک)", "نواندیشان ۲ (شهرک علمی)", "نواندیشان ۳ (انارک)", "نواندیشان ۴ (اردکان)"],
            "capacity_mw": [10.0, 1.0, 4.0, 4.0]
        })
        fig_pie = px.pie(
            df_plants, 
            values="capacity_mw", 
            names="plant_name", 
            hole=0.45,
            color_discrete_sequence=["#10b981", "#3b82f6", "#f59e0b", "#ef4444"]
        )
        fig_pie.update_layout(font_family="Vazirmatn", margin=dict(t=20, b=20, l=20, r=20), height=320)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_t1_right:
        st.markdown("#### 📋 وضعیت پروژه‌ها در یک نگاه")
        st.markdown("""
        * **نواندیشان ۱ (۱۰ مگاوات):** در مدار، متصل به شبکه سراسری، وضعیت عملکرد کاملاً پایدار.
        * **نواندیشان ۲ (۱ مگاوات):** در مدار، فروش برق سبز در بورس انرژی، پایش مستمر راندمان.
        * **نواندیشان ۳ (۴ مگاوات):** پیشرفت ۸۰٪ - پیگیری تست کوبیکل و کنتور جهت اتصال سریع به شبکه.
        * **نواندیشان ۴ (۴ مگاوات):** پیشرفت ۲۰٪ - پیگیری تمدید مجوز و انشعاب برق کارگاهی.
        """)

# ==========================================
# تب دوم: برنامه هفتگی و Action Plan
# ==========================================
with tab2:
    st.subheader("📝 برنامه هفتگی و پیگیری اقدامات اجرایی (Action Plan)")
    st.caption("پیگیری تسک‌های اولویت‌دار و مسئولین اجرایی به تفکیک پروژه‌ها")
    
    col_ap1, col_ap2 = st.columns(2)
    
    with col_ap1:
        st.markdown("### ⚡ نواندیشان ۴ (اردکان)")
        st.checkbox("پیگیری تمدید مجوز احداث از توزیع برق یزد", value=False)
        st.checkbox("پیگیری برق موقت کارگاهی و هماهنگی پیمانکار از اداره برق اردکان", value=False)
        
        st.markdown("### ⚡ نواندیشان ۳ (انارک)")
        st.checkbox("پیگیری تست کوبیکل‌ها توسط شرکت تستا", value=False)
        st.checkbox("پیگیری و راه‌اندازی مودم RTU دیسپاچینگ (مهندس جوان)", value=False)
        st.checkbox("پیگیری تخصیص و ثبت کد PGDS (مهندس کفایت)", value=False)
        st.checkbox("پیگیری نصب و پلمپ کنتور اندازه‌گیری توسط شرکت اختربرق", value=False)
        
    with col_ap2:
        st.markdown("### ⚡ نواندیشان ۲ (شهرک علمی و تحقیقاتی اصفهان)")
        st.checkbox("پیگیری و نظارت بر نصب غلاف‌ها توسط شرکت فرااندیش", value=False)
        
        st.markdown("### ⚡ نواندیشان ۱ (انارک)")
        st.checkbox("پیگیری و برقراری خط تلفن ثابت نیروگاه توسط شرکت الماس شرق", value=False)
        
        st.markdown("### 🌐 فاز توسعه و ساختگاه‌های جدید")
        st.checkbox("پیگیری موافقت اصولی و تخصیص ساختگاه‌های جدید خورشیدی در استان یزد (استانداری و برق منطقه‌ای یزد)", value=False)

# ==========================================
# تب سوم: تحلیل مالی و استراتژی بورس
# ==========================================
with tab3:
    st.subheader("📈 تحلیل مالی، عملکرد ۶ ماهه و استراتژی فروش مهر ماه")
    
    df_finance = pd.DataFrame({
        "month": ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"],
        "generation_mwh": [166.6, 166.6, 148.8, 163.6, 174.8, 178.5],
        "price_toman": [3500, 4777, 7500, 9500, 14269, 7475],
        "revenue_million": [640.0, 829.0, 1220.0, 1700.0, 2660.0, 1380.0]
    })
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.markdown("#### 💰 روند درآمد وصولی ماهانه (میلیون تومان)")
        fig_bar = px.bar(
            df_finance, 
            x="month", 
            y="revenue_million", 
            text="revenue_million",
            color="revenue_million",
            color_continuous_scale="Viridis",
            labels={"month": "ماه", "revenue_million": "درآمد (میلیون تومان)"}
        )
        fig_bar.update_traces(texttemplate='%{text:.0f}', textposition='outside')
        fig_bar.update_layout(font_family="Vazirmatn", height=350, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col_f2:
        st.markdown("#### 📈 روند کشف نرخ برق سبز در بورس انرژی (تومان / kWh)")
        fig_line = px.line(
            df_finance, 
            x="month", 
            y="price_toman", 
            markers=True,
            labels={"month": "ماه", "price_toman": "نرخ (تومان/kWh)"}
        )
        fig_line.update_traces(line_color="#f59e0b", marker=dict(size=8, color="#d97706"))
        fig_line.update_layout(font_family="Vazirmatn", height=350, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_line, use_container_width=True)
        
    st.markdown("---")
    st.subheader("🎯 شبیه‌ساز استراتژی تلفیقی مهر ماه (بورس سبز + بازار رک / دوجانبه)")
    
    sim_col1, sim_col2 = st.columns([1, 2])
    
    with sim_col1:
        prod_target = st.number_input("پیش‌بینی کل تولید مهر ماه (MWh):", min_value=100.0, max_value=350.0, value=250.0, step=5.0)
        bourse_cap = 220.0  # سقف ظرفیت عرضه بورس
        otc_volume = max(0.0, prod_target - bourse_cap)
        bourse_volume = min(prod_target, bourse_cap)
        
        st.info(f"⚡ **تخصیص کانال فروش:**\n- عرضه در تابلوی بورس سبز: **{bourse_volume:.1f} MWh**\n- مازاد عرضه در بازار دوج max_value=15000, value=7200, step=100)

    with sim_col2:
        p1_v = bourse_volume * 0.40
        p2_v = bourse_volume * 0.40
        p3_v = bourse_volume * 0.20
        p1_r = 6900
        p2
        p1_v = bourse_volume * 0.40
        p2_v = bourse_volume * 0.40
        p3_v = bourse_volume * 0.20
        p1_r = 6900
        p2_r = 7800
        p3_r = 9100
        
        bourse_rev = (p1_v * p1_r + p2_v * p2_r + p3_v * p3_r) / 1000.0
        otc_rev = (otc_volume * otc_price) / 1000.0
        total_rev = bourse_rev + otc_rev
        weighted_rate = (total_rev * 1000.0) / prod_target

        st.markdown(f"""
        <div class="strategy-box">
            <h4 style="color:#f59e0b; margin-top:0;">💡 سناریوی بهینه فروش و عرضه تلفیقی مهر ماه:</h4>
            <b>الف) تابلوی بورس سبز (حجم {bourse_volume:.1f} MWh):</b>
            <ul>
                <li><b>پله ۱ (۴۰٪ حجم بورس - پایه):</b> {p1_v:.1f} MWh با نرخ <b>{p1_r:,.0f} تومان</b> ➔ {(p1_v*p1_r)/1000:.1f} م.ت</li>
                <li><b>پله ۲ (۴۰٪ حجم بورس - رقابتی):</b> {p2_v:.1f} MWh با نرخ <b>{p2_r:,.0f} تومان</b> ➔ {(p2_v*p2_r)/1000:.1f} م.ت</li>
                <li><b>پله ۳ (۲۰٪ حجم بورس - تهاجمی/پیک):</b> {p3_v:.1f} MWh با نرخ <b>{p3_r:,.0f} تومان</b> ➔ {(p3_v*p3_r)/1000:.1f} م.ت</li>
            </ul>
            <b>ب) بازار دوجانبه / خارج از پایاپای (رک) (حجم {otc_volume:.1f} MWh):</b>
            <ul>
                <li>فروش مستقیم مازاد سقف مجوز: <b>{otc_volume:.1f} MWh</b> با نرخ <b>{otc_price:,.0f} تومان</b> ➔ {otc_rev:.1f} م.ت</li>
            </ul>
            <hr style="border-color: rgba(245, 158, 11, 0.2);">
            <div style="font-size: 17px; font-weight: bold; color: #10b981;">
                🎯 کل درآمد پیش‌بینی‌شده مهر ماه: {total_rev:,.1f} میلیون تومان ({(total_rev/1000):.2f} میلیارد تومان)
            </div>
            <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">
                میانگین وزنی نرخ کل سبد: {weighted_rate:,.0f} تومان به ازای هر کیلووات ساعت
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box" style="margin-top: 15px;">
        <b>🔍 تحلیل فنی و توجیه استراتژیک عرضه مهر ماه:</b><br>
        ۱. <b>راندمان عالی نیروگاه در مهر ماه:</b> با توجه به کاهش دمای محیطی و به تبع آن افت دمای کاری سلول‌های فتوولتائیک (کاهش ضریب تلفات دمایی ولتاژ) در کنار طول مناسب روز، نیروگاه در یکی از ایده‌آل‌ترین نقاط بازدهی فصلی قرار دارد و پتانسیل تولید بسیار بالا است.<br>
        ۲. <b>مدیری و بازار رک:</b> با توجه به سقف مجوز عرضه بورسی (۲۲۰ مگاوات‌ساعت)، حجم مجاز در قالب استراتژی پلکانی جهت حداکثرسازی نرخ عرضه می‌شود و مازاد تولید به صورت قراردادهای دوجانبه در <b>بازار رک</b> با صنایع متقاضی مبادله می‌گردد تا از ایجاد درآمد بالای ۱.۸ تا ۲ میلیارد تومان اطمینان حاصل شود.
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# تب چهارم: پایش O&M و تولید
# ==========================================
with tab4:
    st.subheader("🔧 پ.subheader("🔧 پ
