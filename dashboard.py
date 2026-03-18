import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="DAZI Paid Search Dashboard", page_icon="📊", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Roboto:wght@400;500;700&display=swap');
    .stApp {
        background-color: #f8f9fa !important;
        font-family: 'Roboto', 'Google Sans', sans-serif;
        color: #202124;
    }
    .google-ads-header {
        background: #1a73e8;
        padding: 16px 24px;
        border-radius: 0;
        margin: -1rem -1rem 24px -1rem;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .google-ads-logo {
        font-family: 'Google Sans', sans-serif;
        font-size: 20px;
        font-weight: 500;
        color: #ffffff;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .google-ads-subtitle {
        font-size: 13px;
        color: rgba(255,255,255,0.8);
        margin-left: auto;
    }
    .section-title {
        font-family: 'Google Sans', 'Roboto', sans-serif;
        font-size: 16px;
        font-weight: 500;
        color: #202124;
        margin: 20px 0 12px 0;
        padding-bottom: 8px;
        border-bottom: 2px solid #1a73e8;
        display: inline-block;
    }
    div[data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #dadce0;
        border-radius: 8px;
        padding: 16px 20px;
        box-shadow: none;
    }
    div[data-testid="stMetric"] label {
        color: #5f6368 !important;
        font-size: 11px !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-family: 'Roboto', sans-serif !important;
    }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #202124 !important;
        font-size: 24px !important;
        font-weight: 500 !important;
        font-family: 'Google Sans', 'Roboto', sans-serif !important;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 0px; border-bottom: 1px solid #dadce0; }
    .stTabs [data-baseweb="tab"] {
        color: #5f6368; font-family: 'Google Sans', 'Roboto', sans-serif;
        font-size: 14px; font-weight: 500; padding: 12px 24px;
        border-bottom: 3px solid transparent;
    }
    .stTabs [aria-selected="true"] { color: #1a73e8 !important; border-bottom: 3px solid #1a73e8 !important; }
    .stDataFrame { border: 1px solid #dadce0; border-radius: 8px; overflow: hidden; }
    section[data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #dadce0; }
    .stMarkdown, .stMarkdown p, .stCaption { color: #202124 !important; }
    a { color: #1a73e8 !important; }
    .stProgress > div > div { background-color: #1a73e8 !important; }
    .ad-copy-box { background: #ffffff; border-radius: 8px; padding: 16px 20px; margin-bottom: 16px; border: 1px solid #dadce0; }
    .ad-label { font-size: 11px; color: #202124; font-weight: 700; display: inline-block; background: #f1f3f4; padding: 2px 6px; border-radius: 3px; margin-right: 6px; border: 1px solid #dadce0; }
    .ad-url { font-size: 13px; color: #202124; }
    .ad-headline { font-size: 18px; color: #1a0dab; font-weight: 400; margin: 4px 0; line-height: 1.3; }
    .ad-description { font-size: 13px; color: #4d5156; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

COMP_REVERSE = {3: "High", 2: "Medium", 1: "Low"}

# ═══════════════════════════════════════════════════════
# DATA — percentages stored as actual % values (e.g., 94 not 0.94)
# ═══════════════════════════════════════════════════════

campaign_data = pd.DataFrame([
    {"Campaign": "Homepage", "Budget": 1000, "Impressions": 12133, "Top Imp. Rate": 94.0, "Clicks": 689, "Avg CPC": 0.63, "Total Cost": 434.07, "CTR": 5.7, "Conversions": 42, "Conv. Rate": 6.1, "Margin/Conv": 15, "CPA": 10.33, "POAS": 45.1},
    {"Campaign": "Floral tie", "Budget": 2000, "Impressions": 33485, "Top Imp. Rate": 88.0, "Clicks": 1110, "Avg CPC": 1.48, "Total Cost": 1642.80, "CTR": 3.3, "Conversions": 101, "Conv. Rate": 9.1, "Margin/Conv": 18, "CPA": 16.27, "POAS": 10.7},
    {"Campaign": "Classic tie", "Budget": 2000, "Impressions": 61263, "Top Imp. Rate": 57.0, "Clicks": 890, "Avg CPC": 1.70, "Total Cost": 1513.00, "CTR": 1.5, "Conversions": 45, "Conv. Rate": 5.1, "Margin/Conv": 16, "CPA": 33.62, "POAS": -52.4},
    {"Campaign": "Wedding tie", "Budget": 2000, "Impressions": 47528, "Top Imp. Rate": 34.0, "Clicks": 495, "Avg CPC": 4.00, "Total Cost": 1980.00, "CTR": 1.0, "Conversions": 58, "Conv. Rate": 11.7, "Margin/Conv": 75, "CPA": 34.14, "POAS": 119.7},
])

adgroup_data = pd.DataFrame([
    {"Campaign": "Homepage", "Ad Group": "Homepage", "Impressions": 12133, "Top Imp. Rate": 1.5, "Clicks": 689, "Avg CPC": 0.63, "Total Cost": 434.07, "CTR": 5.7, "Conversions": 42, "Conv. Rate": 6.1, "Margin/Conv": 15, "CPA": 10.33, "POAS": 45.0},
    {"Campaign": "Floral tie", "Ad Group": "Floral tie collection", "Impressions": 26619, "Top Imp. Rate": 3.7, "Clicks": 794, "Avg CPC": 1.408, "Total Cost": 1117.75, "CTR": 3.0, "Conversions": 72, "Conv. Rate": 9.1, "Margin/Conv": 18, "CPA": 15.52, "POAS": 16.0},
    {"Campaign": "Floral tie", "Ad Group": "Floral bow tie collection", "Impressions": 6866, "Top Imp. Rate": 1.5, "Clicks": 316, "Avg CPC": 1.52, "Total Cost": 480.32, "CTR": 4.6, "Conversions": 29, "Conv. Rate": 9.2, "Margin/Conv": 18, "CPA": 16.56, "POAS": 9.0},
    {"Campaign": "Classic tie", "Ad Group": "Skinny tie", "Impressions": 45301, "Top Imp. Rate": 2.8, "Clicks": 687, "Avg CPC": 1.01, "Total Cost": 693.87, "CTR": 1.5, "Conversions": 32, "Conv. Rate": 4.7, "Margin/Conv": 16, "CPA": 21.68, "POAS": -26.0},
    {"Campaign": "Classic tie", "Ad Group": "Dotted navy tie", "Impressions": 15962, "Top Imp. Rate": 2.3, "Clicks": 203, "Avg CPC": 0.82, "Total Cost": 166.46, "CTR": 1.3, "Conversions": 13, "Conv. Rate": 6.4, "Margin/Conv": 16, "CPA": 12.80, "POAS": 25.0},
    {"Campaign": "Wedding tie", "Ad Group": "Wedding tie", "Impressions": 47528, "Top Imp. Rate": 4.1, "Clicks": 495, "Avg CPC": 4.00, "Total Cost": 1980.00, "CTR": 1.0, "Conversions": 58, "Conv. Rate": 11.7, "Margin/Conv": 75, "CPA": 34.14, "POAS": 120.0},
])

keyword_report_data = pd.DataFrame([
    {"Keyword": "necktie", "Competition": 3, "Top Bid": 1.80, "Avg Monthly": 100000, "CPC Bid": 2.30, "Quality Score": 7, "Impressions": 40657, "Top Imp. Rate": 64.4, "Clicks": 566, "CTR": 1.4, "Avg CPC": 2.30, "Total Cost": 1301.80, "Conversions": 25, "Conv. Rate": "4.4%", "CPA": "$52.1"},
    {"Keyword": "tie for suit", "Competition": 3, "Top Bid": 2.40, "Avg Monthly": 10000, "CPC Bid": 2.10, "Quality Score": 6, "Impressions": 2386, "Top Imp. Rate": 37.8, "Clicks": 19, "CTR": 0.8, "Avg CPC": 2.10, "Total Cost": 39.90, "Conversions": 1, "Conv. Rate": "5.3%", "CPA": "$39.9"},
    {"Keyword": "floral tie", "Competition": 3, "Top Bid": 1.71, "Avg Monthly": 9500, "CPC Bid": 2.10, "Quality Score": 10, "Impressions": 5303, "Top Imp. Rate": 88.4, "Clicks": 675, "CTR": 12.7, "Avg CPC": 2.10, "Total Cost": 1417.50, "Conversions": 89, "Conv. Rate": "13.2%", "CPA": "$15.9"},
    {"Keyword": "floral wedding tie", "Competition": 3, "Top Bid": 2.50, "Avg Monthly": 9000, "CPC Bid": 2.60, "Quality Score": 10, "Impressions": 4255, "Top Imp. Rate": 74.9, "Clicks": 459, "CTR": 10.8, "Avg CPC": 2.60, "Total Cost": 1193.40, "Conversions": 83, "Conv. Rate": "18.1%", "CPA": "$14.4"},
    {"Keyword": "floral necktie", "Competition": 3, "Top Bid": 1.88, "Avg Monthly": 8700, "CPC Bid": 2.10, "Quality Score": 9, "Impressions": 3976, "Top Imp. Rate": 72.4, "Clicks": 138, "CTR": 3.5, "Avg CPC": 2.10, "Total Cost": 289.80, "Conversions": 23, "Conv. Rate": "16.7%", "CPA": "$12.6"},
    {"Keyword": "pink floral tie", "Competition": 3, "Top Bid": 1.30, "Avg Monthly": 8500, "CPC Bid": 1.50, "Quality Score": 10, "Impressions": 4458, "Top Imp. Rate": 83.1, "Clicks": 533, "CTR": 12.0, "Avg CPC": 1.50, "Total Cost": 799.50, "Conversions": 178, "Conv. Rate": "33.4%", "CPA": "$4.5"},
    {"Keyword": "blue floral tie", "Competition": 3, "Top Bid": 0.95, "Avg Monthly": 7500, "CPC Bid": 1.20, "Quality Score": 10, "Impressions": 4306, "Top Imp. Rate": 90.9, "Clicks": 564, "CTR": 13.1, "Avg CPC": 1.20, "Total Cost": 676.80, "Conversions": 141, "Conv. Rate": "25.0%", "CPA": "$4.8"},
    {"Keyword": "tie for blue suit", "Competition": 3, "Top Bid": 1.80, "Avg Monthly": 980, "CPC Bid": 2.50, "Quality Score": 6, "Impressions": 371, "Top Imp. Rate": 60.0, "Clicks": 5, "CTR": 1.3, "Avg CPC": 2.50, "Total Cost": 12.50, "Conversions": 0, "Conv. Rate": "-", "CPA": "-"},
    {"Keyword": "floral tie for sale", "Competition": 3, "Top Bid": 2.40, "Avg Monthly": 880, "CPC Bid": 2.60, "Quality Score": 9, "Impressions": 390, "Top Imp. Rate": 70.2, "Clicks": 13, "CTR": 3.3, "Avg CPC": 2.60, "Total Cost": 33.80, "Conversions": 6, "Conv. Rate": "46.2%", "CPA": "$5.6"},
    {"Keyword": "black and white floral tie", "Competition": 3, "Top Bid": 0.85, "Avg Monthly": 120, "CPC Bid": 0.90, "Quality Score": 8, "Impressions": 46, "Top Imp. Rate": 61.0, "Clicks": 1, "CTR": 2.2, "Avg CPC": 0.90, "Total Cost": 0.90, "Conversions": 0, "Conv. Rate": "-", "CPA": "-"},
    {"Keyword": "unique floral tie", "Competition": 2, "Top Bid": 0.95, "Avg Monthly": 700, "CPC Bid": 1.00, "Quality Score": 8, "Impressions": 268, "Top Imp. Rate": 75.8, "Clicks": 12, "CTR": 4.5, "Avg CPC": 1.00, "Total Cost": 12.00, "Conversions": 0, "Conv. Rate": "-", "CPA": "-"},
    {"Keyword": "red tie with black suit", "Competition": 2, "Top Bid": 0.65, "Avg Monthly": 550, "CPC Bid": 0.715, "Quality Score": 5, "Impressions": 138, "Top Imp. Rate": 49.5, "Clicks": 2, "CTR": 1.4, "Avg CPC": 0.715, "Total Cost": 1.43, "Conversions": 0, "Conv. Rate": "-", "CPA": "-"},
    {"Keyword": "tie and handkerchief set", "Competition": 2, "Top Bid": 0.50, "Avg Monthly": 550, "CPC Bid": 0.62, "Quality Score": 4, "Impressions": 124, "Top Imp. Rate": 44.6, "Clicks": 1, "CTR": 0.8, "Avg CPC": 0.62, "Total Cost": 0.62, "Conversions": 0, "Conv. Rate": "-", "CPA": "-"},
    {"Keyword": "how to tie a tie", "Competition": 1, "Top Bid": 0.25, "Avg Monthly": 500000, "CPC Bid": 0.27, "Quality Score": 5, "Impressions": 122727, "Top Imp. Rate": 64.8, "Clicks": 2863, "CTR": 2.3, "Avg CPC": 0.27, "Total Cost": 773.01, "Conversions": 14, "Conv. Rate": "0.5%", "CPA": "$55.2"},
    {"Keyword": "best tie knot", "Competition": 1, "Top Bid": 0.10, "Avg Monthly": 9000, "CPC Bid": 0.10, "Quality Score": 4, "Impressions": 1636, "Top Imp. Rate": 48.0, "Clicks": 28, "CTR": 1.7, "Avg CPC": 0.10, "Total Cost": 2.80, "Conversions": 1, "Conv. Rate": "3.6%", "CPA": "$2.8"},
])

keyword_report_data["Competition"] = keyword_report_data["Competition"].map(COMP_REVERSE)

keyword_research_data = pd.DataFrame([
    {"Keyword": "necktie", "Competition": 3, "Top of Page Bid": 1.80, "Avg Monthly Searches": 100000},
    {"Keyword": "tie for suit", "Competition": 3, "Top of Page Bid": 2.40, "Avg Monthly Searches": 10000},
    {"Keyword": "floral tie", "Competition": 3, "Top of Page Bid": 1.71, "Avg Monthly Searches": 9500},
    {"Keyword": "floral wedding tie", "Competition": 3, "Top of Page Bid": 2.50, "Avg Monthly Searches": 9000},
    {"Keyword": "floral necktie", "Competition": 3, "Top of Page Bid": 1.88, "Avg Monthly Searches": 8700},
    {"Keyword": "pink floral tie", "Competition": 3, "Top of Page Bid": 1.30, "Avg Monthly Searches": 8500},
    {"Keyword": "blue floral tie", "Competition": 3, "Top of Page Bid": 0.95, "Avg Monthly Searches": 7500},
    {"Keyword": "tie for blue suit", "Competition": 3, "Top of Page Bid": 1.80, "Avg Monthly Searches": 980},
    {"Keyword": "floral tie for sale", "Competition": 3, "Top of Page Bid": 2.40, "Avg Monthly Searches": 880},
    {"Keyword": "black and white floral tie", "Competition": 3, "Top of Page Bid": 0.85, "Avg Monthly Searches": 120},
    {"Keyword": "unique floral tie", "Competition": 2, "Top of Page Bid": 0.95, "Avg Monthly Searches": 700},
    {"Keyword": "red tie with black suit", "Competition": 2, "Top of Page Bid": 0.65, "Avg Monthly Searches": 550},
    {"Keyword": "tie and handkerchief set", "Competition": 2, "Top of Page Bid": 0.50, "Avg Monthly Searches": 550},
    {"Keyword": "how to tie a tie", "Competition": 1, "Top of Page Bid": 0.25, "Avg Monthly Searches": 500000},
    {"Keyword": "best tie knot", "Competition": 1, "Top of Page Bid": 0.10, "Avg Monthly Searches": 9000},
])
keyword_research_data["Competition"] = keyword_research_data["Competition"].map(COMP_REVERSE)


# ═══════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════

st.markdown("""
<div class="google-ads-header">
    <div class="google-ads-logo">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><circle cx="12" cy="12" r="10" fill="none" stroke="white" stroke-width="2"/><text x="12" y="16" text-anchor="middle" font-size="12" fill="white" font-weight="bold">G</text></svg>
        DAZI Paid Search Dashboard
    </div>
    
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📈 Campaign Report", "🔑 Keyword Report", "🔍 Keyword Research", "📢 Ads & Landing Page"])


# ─── TAB 1: Campaign Report ───
with tab1:
    st.markdown('<div class="section-title">Campaign Overview</div>', unsafe_allow_html=True)
    total_budget = campaign_data["Budget"].sum()
    total_impressions = campaign_data["Impressions"].sum()
    total_clicks = campaign_data["Clicks"].sum()
    total_cost = campaign_data["Total Cost"].sum()
    total_conversions = campaign_data["Conversions"].sum()
    overall_ctr = total_clicks / total_impressions * 100 if total_impressions > 0 else 0
    overall_conv_rate = total_conversions / total_clicks * 100 if total_clicks > 0 else 0
    overall_cpa = total_cost / total_conversions if total_conversions > 0 else 0
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    m1.metric("Total Budget", f"${total_budget:,}")
    m2.metric("Impressions", f"{total_impressions:,}")
    m3.metric("Clicks", f"{total_clicks:,}")
    m4.metric("Total Cost", f"${total_cost:,.2f}")
    m5.metric("Conversions", f"{total_conversions:,}")
    m6.metric("Avg CPA", f"${overall_cpa:.2f}")
    st.markdown("")

    st.markdown('<div class="section-title">Campaign Report</div>', unsafe_allow_html=True)
    st.dataframe(campaign_data, use_container_width=True, hide_index=True,
        column_config={
            "Budget": st.column_config.NumberColumn(format="$%d"),
            "Impressions": st.column_config.NumberColumn(format="%d"),
            "Top Imp. Rate": st.column_config.NumberColumn(format="%.0f%%"),
            "Clicks": st.column_config.NumberColumn(format="%d"),
            "Avg CPC": st.column_config.NumberColumn(format="$%.2f"),
            "Total Cost": st.column_config.NumberColumn(format="$%,.0f"),
            "CTR": st.column_config.NumberColumn(format="%.1f%%"),
            "Conversions": st.column_config.NumberColumn(format="%d"),
            "Conv. Rate": st.column_config.NumberColumn(format="%.1f%%"),
            "Margin/Conv": st.column_config.NumberColumn(format="$%d"),
            "CPA": st.column_config.NumberColumn(format="$%.2f"),
            "POAS": st.column_config.NumberColumn("POAS", format="%.1f%%"),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Ad Group Report</div>', unsafe_allow_html=True)
    st.dataframe(adgroup_data, use_container_width=True, hide_index=True,
        column_config={
            "Impressions": st.column_config.NumberColumn(format="%d"),
            "Top Imp. Rate": st.column_config.NumberColumn(format="%.1f%%"),
            "Clicks": st.column_config.NumberColumn(format="%d"),
            "Avg CPC": st.column_config.NumberColumn(format="$%.2f"),
            "Total Cost": st.column_config.NumberColumn(format="$%,.0f"),
            "CTR": st.column_config.NumberColumn(format="%.1f%%"),
            "Conversions": st.column_config.NumberColumn(format="%d"),
            "Conv. Rate": st.column_config.NumberColumn(format="%.1f%%"),
            "Margin/Conv": st.column_config.NumberColumn(format="$%d"),
            "CPA": st.column_config.NumberColumn(format="$%.2f"),
            "POAS": st.column_config.NumberColumn("POAS", format="%.0f%%"),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Metric Definitions</div>', unsafe_allow_html=True)
    for term, defn in {
        "Budget": "The amount of money DAZI is willing to spend on their ads within a specific time period.",
        "Impressions": "The total number of times an ad appears.",
        "Search Top Impression Rate (%)": "The percentage of times an ad appears in the top positions of the search results.",
        "Clicks": "The number of times users clicked on the ad.",
        "CTR (Click-Through Rate)": "The likelihood of receiving a click per impression (Clicks / Impressions).",
        "Avg. CPC (Cost per Click)": "The average amount an advertiser actually pays per click.",
        "Total Cost": "The total advertising expenditure.",
        "Conversions": "The total number of desired actions (e.g., purchases, sign-ups) completed.",
        "Conversion Rate": "The percentage of users who take a desired action (Conversions / Clicks).",
        "CPA (Cost per Acquisition)": "The cost of acquiring a customer (Total Cost / Conversions).",
        "POAS (Profit on Ad Spend)": "Measures how profitable the ad campaign is. Calculated as (Margin per Conversion − CPA) ÷ CPA.",
    }.items():
        with st.expander(f"**{term}**"):
            st.markdown(defn)


# ─── TAB 2: Keyword Report ───
with tab2:
    st.markdown('<div class="section-title">Ad Group: Floral Ties — Keyword Performance Report</div>', unsafe_allow_html=True)
    st.markdown("This report shows the performance of each keyword in the floral ties ad group.")
    st.markdown("")
    kr_impressions = keyword_report_data["Impressions"].sum()
    kr_clicks = keyword_report_data["Clicks"].sum()
    kr_cost = keyword_report_data["Total Cost"].sum()
    kr_conv = keyword_report_data["Conversions"].sum()
    kr_ctr = kr_clicks / kr_impressions * 100 if kr_impressions > 0 else 0
    kr_cpa = kr_cost / kr_conv if kr_conv > 0 else 0
    k1, k2, k3, k4, k5, k6 = st.columns(6)
    k1.metric("Impressions", f"{kr_impressions:,}")
    k2.metric("Clicks", f"{kr_clicks:,}")
    k3.metric("CTR", f"{kr_ctr:.1f}%")
    k4.metric("Total Cost", f"${kr_cost:,.2f}")
    k5.metric("Conversions", f"{kr_conv:,}")
    k6.metric("Avg CPA", f"${kr_cpa:.2f}")
    st.markdown("")

    st.dataframe(keyword_report_data, use_container_width=True, hide_index=True, height=580,
        column_config={
            "Competition": st.column_config.TextColumn(),
            "Top Bid": st.column_config.NumberColumn(format="$%.2f"),
            "Avg Monthly": st.column_config.NumberColumn(format="%d"),
            "CPC Bid": st.column_config.NumberColumn(format="$%.2f"),
            "Quality Score": st.column_config.NumberColumn(format="%d"),
            "Impressions": st.column_config.NumberColumn(format="%d"),
            "Top Imp. Rate": st.column_config.NumberColumn(format="%.1f%%"),
            "Clicks": st.column_config.NumberColumn(format="%d"),
            "CTR": st.column_config.NumberColumn(format="%.1f%%"),
            "Avg CPC": st.column_config.NumberColumn(format="$%.2f"),
            "Total Cost": st.column_config.NumberColumn(format="$%,.0f"),
            "Conversions": st.column_config.NumberColumn(format="%d"),
            "Conv. Rate": st.column_config.TextColumn(),
            "CPA": st.column_config.TextColumn(),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Metric Definitions</div>', unsafe_allow_html=True)
    for term, defn in {
        "Competition": "The level of competition for a keyword based on the number of advertisers bidding on it.",
        "Top of Page Bid Estimate": "An estimated CPC bid required for your ad to appear at the top of the search results page.",
        "Avg. Monthly Searches": "The average monthly search volume for a keyword.",
        "CPC Bid": "The maximum amount DAZI is willing to pay per click on an ad.",
        "Ad Quality Score": "A quality score assigned by Google (1 = low; 10 = high) based on ad relevance, expected CTR, and landing page experience.",
        "Impressions": "The total number of times an ad appears for a keyword.",
        "Search Top Impression Rate (%)": "The percentage of times an ad appears in the top positions of the search results.",
        "Clicks": "The number of times users clicked on the ad.",
        "CTR (Click-Through Rate)": "The likelihood of receiving a click per impression (Clicks / Impressions).",
        "Avg. CPC (Cost per Click)": "The average amount an advertiser actually pays per click.",
        "Total Cost": "The total advertising expenditure.",
        "Conversions": "The total number of desired actions (e.g., purchases) completed.",
        "Conversion Rate": "The percentage of users who take a desired action (Conversions / Clicks).",
        "CPA (Cost per Acquisition)": "The cost of acquiring a customer (Total Cost / Conversions).",
    }.items():
        with st.expander(f"**{term}**"):
            st.markdown(defn)


# ─── TAB 3: Keyword Research ───
with tab3:
    st.markdown('<div class="section-title">Keyword Research</div>', unsafe_allow_html=True)
    st.markdown(f"**Landing page:** [www.daziusa.com/collections/floral](https://www.daziusa.com/collections/floral)")
    st.markdown("")

    st.dataframe(keyword_research_data, use_container_width=True, hide_index=True,
        column_config={
            "Competition": st.column_config.TextColumn(),
            "Top of Page Bid": st.column_config.NumberColumn(format="$%.2f"),
            "Avg Monthly Searches": st.column_config.NumberColumn(format="%d"),
        })
    st.markdown("")

    st.markdown('<div class="section-title">Discussion Questions</div>', unsafe_allow_html=True)
    st.info("**Which keywords will yield more impressions?**\n\nConsider both the monthly search volume and the competition level.")
    st.info("**Which keywords will yield higher conversion rates?**\n\nThink about search intent — keywords indicating purchase intent (e.g., 'floral tie for sale') tend to convert better than informational queries (e.g., 'how to tie a tie').")
    st.markdown("")

    st.markdown('<div class="section-title">Metric Definitions</div>', unsafe_allow_html=True)
    for term, defn in {
        "Competition": "Degree of competition for the keyword, estimated based on the number of advertisers bidding on the keyword.",
        "Top of Page Bid Estimate": "An estimate for the CPC bid required for your ad to show at the top of search results page.",
        "Avg Monthly Searches": "The average monthly search volume for each keyword. Indicates the popularity of keywords among searchers.",
    }.items():
        with st.expander(f"**{term}**"):
            st.markdown(defn)


# ─── TAB 4: Ads & Landing Page ───
with tab4:
    st.markdown('<div class="section-title">Ad Group: Floral Ties</div>', unsafe_allow_html=True)
    st.markdown(f"**Landing page:** [www.daziusa.com/collections/floral](https://www.daziusa.com/collections/floral)")
    st.markdown("")
    st.markdown('<div class="section-title">Ad Copy Examples</div>', unsafe_allow_html=True)
    col_ad1, col_ad2 = st.columns(2)
    with col_ad1:
        st.markdown("""<div class="ad-copy-box"><div><span class="ad-label">Ad</span> <span class="ad-url">https://www.daziusa.com/neckties/floral</span></div><div class="ad-headline">Shop Floral Ties For Weddings - Free Shipping On Orders $40+</div><div class="ad-description">Browse Our Original <b>Floral Ties</b>, <b>Floral</b> Bow <b>Ties</b>, And Other Essentials. Shop DAZI® Today! Free Shipping Over $40. Best Quality. Great For <b>Weddings</b>. Styles: White <b>Floral</b>, Blue Bloom.</div></div>""", unsafe_allow_html=True)
    with col_ad2:
        st.markdown("""<div class="ad-copy-box"><div><span class="ad-label">Ad</span> <span class="ad-url">https://www.daziusa.com/neckties/floral</span></div><div class="ad-headline">Shop Floral Ties - DAZI® Original Floral Ties - daziusa.com</div><div class="ad-description">Browse Our Original <b>Floral Ties</b>, <b>Floral</b> Bow <b>Ties</b>, And More. Shop & Save Today! Best Quality.</div></div>""", unsafe_allow_html=True)
    st.markdown("")
    st.markdown('<div class="section-title">Landing Page Preview</div>', unsafe_allow_html=True)
    st.markdown("The ads direct users to the DAZI floral ties collection page:")
    st.image("Floral.png", use_container_width=True)
    st.markdown("")
    st.caption("Landing page: www.daziusa.com/collections/floral — Products priced at $32.00 each")