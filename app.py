import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="داشبورد نیروگاه‌های خورشیدی", page_icon="☀️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; direction: rtl; }
    .header-box { background: linear-gradient(90deg, #1f4037, #99f2c8); padding: 20px; border-radius: 12px; color: #0e1117; text-align: center; margin-bottom: 25px; }
    .metric-card { 
    background-color: #FBBF24; /* این یک رنگ زرد/طلایی خیلی شیک است */
    color: #000000; /* رنگ متن را مشکی می‌کنیم تا روی زرد خوانا باشد */
    padding: 15px; 
    border-radius: 10px; 
    border: 1px solid #D97706; /* یک حاشیه تیره‌تر برای جلوه بهتر */
    text-align: center; 
}

    </style>
    <div class="header-box">
        <h1 style="margin:0;">⚡ سامانه هوشمند مانیتورینگ پرتفوی نیروگاه‌های خورشیدی</h1>
        <h3 style="margin:5px 0 0 0;">گروه نیروگاهی نواندیشان |تابستان 1405</h3>
    </div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 نمای کلی سبد نیروگاهی", "⚡ بخش بهره‌برداری (O&M)", "🚧 بخش احداث و توسعه (EPC)"])

df_plants = pd.DataFrame({
    "نیروگاه": ["نواندیشان ۱", "نواندیشان ۲", "نواندیشان ۳", "نواندیشان ۴"],
    "موقعیت": ["انارک", "شهرک علمی اصفهان", "انارک", "اردکان"],
    "ظرفیت (MW)": [10, 1, 4, 4],
    "وضعیت": ["بهره‌برداری", "بهره‌برداری", "مراحل نهایی احداث", "پایه کوبی و نصب پنل"],
    "مدل درآمدی": ["فروش به شبکه", "بورس برق سبز", "بورس برق (آتی)", "فروش به شبکه"]
})

with tab1:
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="metric-card"><h4>ظرفیت کل پرتفوی</h4><h2>19 MW</h2></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h4>نیروگاه فعال</h4><h2>11 MW</h2></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h4>در حال احداث</h4><h2>8 MW</h2></div>', unsafe_allow_html=True)
    c4.markdown('<div class="metric-card"><h4>پیشرفت کل سبد</h4><h2>78%</h2></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    fig = px.bar(df_plants, x="نیروگاه", y="ظرفیت (MW)", color="وضعیت", template="plotly_dark", title="توزیع ظرفیت نیروگاه‌ها")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df_plants, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔋 نواندیشان ۱ (۱۰ مگاوات - انارک)")
        st.success("وضعیت: متصل به شبکه سراسری | در حال تولید پایدار")
        st.metric(label="راندمان ماهانه (PR)", value="94.2 %")
        st.write("📌 **اولویت O&M:** پایش نشست غبار کویری و برنامه‌ریزی دوره شستشوی پنل‌ها.")
    with col2:
        st.subheader("🌿 نواندیشان ۲ (۱ مگاوات - شهرک علمی)")
        st.success("وضعیت: متصل به بورس برق سبز | درآمد حداکثری")
        st.metric(label="پایداری خط تولید", value="98.1 %")
        st.write("📌 **اولویت O&M:** رصد معاملات نماد در بورس سبز و بهینه‌سازی اوج بار.")

with tab3:
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("⚡ نواندیشان ۳ (۴ مگاوات - انارک)")
        st.warning("وضعیت: مراحل نهایی تا بهره‌برداری و اتصال به بورس")
        st.progress(0.92)
        st.caption("پیشرفت پروژه: ۹۲٪ (در حال تست فیدر و اخذ مجوزهای نهایی)")
    with col4:
        st.subheader("☀️ نواندیشان ۴ (۴ مگاوات - اردکان)")
        st.info("وضعیت: عملیات سیویل، پایه کوبی و استقرار سازه‌ها")
        st.progress(0.55)
        st.caption("پیشرفت پروژه: ۵۵٪ (تأمین پنل‌ها و کوبش پایه‌ها)")
