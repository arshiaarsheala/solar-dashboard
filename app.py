import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# تنظیمات اولیه صفحه
st.set_page_config(
    page_title="داشبورد فرماندهی سبد خورشیدی",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# اعمال استایل‌های سفارشی بدون آسیب به ساختار رندر استریم‌لیت
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700;900&display=swap');
    
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, div {
        font-family: 'Vazirmatn', sans-serif !important;
    }
    
    .block-container {
        direction: rtl;
        text-align: right;
    }
    
    [data-testid="stMetric"] {
        background-color: #1E293B;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #334155;
        border-top: 4px solid #FBBF24;
    }
    
    [data-testid="stMetricValue"] {
        color: #FBBF24 !important;
        font-weight: 700 !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# عنوان اصلی داشبورد
st.title("☀️ داشبورد فرماندهی مدیریت سبد نیروگاه‌های خورشیدی")
st.caption("سیستم پایش فنی، پیشرفت پروژه‌ها و استراتژی بورس انرژی")

# تعریف تب‌ها
tab_overview, tab_tasks, tab_finance, tab_om, tab_dev = st.tabs([
    "📊 نمای کلی سبد",
    "📝 برنامه هفتگی و Action Plan",
    "📈 تحلیل مالی و استراتژی بورس",
    "🔧 پایش O&M و تولید",
    "🏗️ پروژه‌های احداث و توسعه",
])

# ==========================================
# تب ۱: نمای کلی سبد
# ==========================================
with tab_overview:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("ظرفیت کل پرتفو", "۴.۰ MWp")
    col2.metric("ظرفیت در حال بهره‌برداری", "۱.۰ MWp")
    col3.metric("ظرفیت در دست احداث", "۳.۰ MWp")
    col4.metric("مجموع درآمد ۶ ماهه", "۹.۵۳ میلیارد تومان")

    st.markdown("---")
    st.subheader("وضعیت نیروگاه‌های چهارگانه نواندیشان")

    plants_data = pd.DataFrame({
        "نام نیروگاه": [
            "نواندیشان ۱ (بهره‌برداری)",
            "نواندیشان ۲",
            "نواندیشان ۳",
            "نواندیشان ۴",
        ],
        "ظرفیت (kW)": [1000, 1000, 1000, 1000],
        "وضعیت": ["درحال تولید", "تجهیز کارگاه", "تست کوبیکل", "پیگیری زمین"],
        "پیشرفت فیزیکی (%)": [100, 45, 80, 20],
    })
    st.dataframe(plants_data, hide_index=True)

# ==========================================
# تب ۲: برنامه هفتگی
# ==========================================
with tab_tasks:
    st.subheader("📋 تسک‌ها و اکشن‌پلن عملیاتی هفته")

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("#### 🔴 اولویت بالا و حیاتی")
        st.checkbox("پیگیری تاییدیه نهایی کوبیکل‌های نواندیشان ۳ از توزیع برق")
        st.checkbox("ارسال جدول عرضه پله‌ای مهر ماه به کارگزاری بورس")
        st.checkbox("تسویه مالی و ثبت فاکتورهای شهریور ماه")

    with col_t2:
        st.markdown("#### 🟡 تسک‌های روتین و O&M")
        st.checkbox("برنامه شستشوی دوره‌ای پنل‌های نواندیشان ۱")
        st.checkbox("گزارش بازرسی ترموگرافی اینورترها")
        st.checkbox("پیگیری مجوز زمین توسعه نواندیشان ۴")

# ==========================================
# تب ۳: تحلیل مالی و استراتژی بورس
# ==========================================
with tab_finance:
    st.subheader("📊 تحلیل عملکرد ۶ ماهه و شبیه‌ساز فروش مهر ماه")

    historical_data = pd.DataFrame({
        "ماه": ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"],
        "حجم_MWh": [166.0, 166.0, 148.0, 163.68, 174.84, 178.56],
        "نرخ_تومان": [3500, 4777, 7500, 9500, 14269, 7475],
        "درآمد_میلیون": [581.0, 793.0, 1110.0, 1554.96, 2494.85, 1334.73],
    })

    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    f_col1.metric(
        "مجموع عرضه ۶ ماهه", f"{historical_data['حجم_MWh'].sum():,.1f} MWh"
    )
    f_col2.metric("مجموع درآمد", "۹,۵۳۴ میلیون تومان")
    f_col3.metric("میانگین موزون نرخ", "۷,۸۶۰ تومان")
    f_col4.metric("بالاترین نرخ معامله", "۱۴,۵۰۰ تومان")

    col_ch1, col_ch2 = st.columns(2)
    with col_ch1:
        fig_price = px.line(
            historical_data,
            x="ماه",
            y="نرخ_تومان",
            markers=True,
            title="روند کشف نرخ در بورس سبز (تومان/kWh)",
            color_discrete_sequence=["#FBBF24"],
        )
        fig_price.update_layout(template="plotly_dark")
        st.plotly_chart(fig_price)

    with col_ch2:
        fig_rev = px.bar(
            historical_data,
            x="ماه",
            y="درآمد_میلیون",
            title="درآمد وصولی ماهانه (میلیون تومان)",
            color="درآمد_میلیون",
            color_continuous_scale="Viridis",
        )
        fig_rev.update_layout(template="plotly_dark")
        st.plotly_chart(fig_rev)

    st.markdown("---")
    st.markdown("### 🎯 شبیه‌ساز و استراتژی قیمت‌گذاری مهر ماه")

    sim_c1, sim_c2 = st.columns([1, 2])
    with sim_c1:
        est_vol = st.slider(
            "پیش‌بینی تولید مهر (MWh):", 100.0, 160.0, 138.0, step=1.0
        )
        strat = st.selectbox(
            "استراتژی نرخ‌گذاری:",
            [
                "متعادل / منطقی (۶,۸۰۰ تومان)",
                "محافظه‌کارانه / فروش فوری (۵,۸۰۰ تومان)",
                "تهاجمی / سود حداکثری (۸,۲۰۰ تومان)",
                "دستی",
            ],
        )

        if "متعادل" in strat:
            target_p = 6800
        elif "محافظه‌کارانه" in strat:
            target_p = 5800
        elif "تهاجمی" in strat:
            target_p = 8200
        else:
            target_p = st.number_input("نرخ دستی (تومان):", value=7000)

    with sim_c2:
        total_est = (est_vol * 1000 * target_p) / 1_000_000
        st.info(f"""
        **خلاصه پیش‌بینی درآمد مهر ماه:**
        * حجم عرضه: **{est_vol:,.1f} MWh**
        * نرخ مفروض: **{target_p:,.0f} تومان**
        * درآمد برآوردی: **{total_est:,.1f} میلیون تومان** ({total_est / 1000:,.2f} میلیارد تومان)
        """)

        st.markdown("#### 💡 سناریوی پیشنهادی عرضه پلکانی به کارگزار:")
        st.write(
            f"🔹 **پله ۱ (۵۰٪ حجم - پایه):** `{est_vol * 0.5:.1f} MWh` با نرخ **۶,۲۰۰ تومان**"
        )
        st.write(
            f"🔹 **پله ۲ (۳۰٪ حجم - رقابتی):** `{est_vol * 0.3:.1f} MWh` با نرخ **۷,۱۰۰ تومان**"
        )
        st.write(
            f"🔹 **پله ۳ (۲۰٪ حجم - حداکثری):** `{est_vol * 0.2:.1f} MWh` با نرخ **۸,۲۰۰ تومان**"
        )

# ==========================================
# تب ۴: O&M و پایش فنی
# ==========================================
with tab_om:
    st.subheader("🔧 پایش عملکرد فنی و نگهداری نواندیشان ۱")
    om1, om2, om3 = st.columns(3)
    om1.metric("ضریب آماده‌به‌کاری (Availability)", "۹۹.۲ ٪")
    om2.metric("ضریب عملکرد (PR)", "۸۱.۵ ٪")
    om3.metric("تولید تجمعی دوره", "۹۹۴.۶ MWh")
    st.success("✅ کلیه استرینگ‌ها و اینورترها در وضعیت نرمال قرار دارند.")

# ==========================================
# تب ۵: پروژه‌های احداث
# ==========================================
with tab_dev:
    st.subheader("🏗️ وضعیت پیشرفت پروژه‌های فاز توسعه")
    st.progress(0.45, text="نواندیشان ۲: پیشرفت ۴۵٪")
    st.progress(0.80, text="نواندیشان ۳: پیشرفت ۸۰٪")
    st.progress(0.20, text="نواندیشان ۴: پیشرفت ۲۰٪")
