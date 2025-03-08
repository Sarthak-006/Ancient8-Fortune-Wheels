import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta
import time
from PIL import Image
import io
import base64
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stateful_button import button
from streamlit_card import card

# Set page configuration
st.set_page_config(
    page_title="Ancient8 Fortune Wheels - Crypto Gaming Experience",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for modern UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Color palette with rich teal, amber and coral tones */
    :root {
        /* Primary colors */
        --teal-light: #66E0D0;       /* Soft teal for most text */
        --teal-medium: #40C4B0;      /* Medium teal for regular text */
        --teal-dark: #2A9D8F;        /* Darker teal for emphasis */
        
        /* Accent colors */
        --amber-light: #FFD166;      /* Light amber for highlights */
        --amber: #FFBF00;            /* Amber for headings */
        --amber-dark: #E6A800;       /* Dark amber for borders/emphasis */
        
        /* Complementary accent */
        --coral-light: #FF9E80;      /* Light coral for accents */
        --coral: #FF7F50;            /* Coral for special elements */
        --coral-dark: #E86C3A;       /* Dark coral for emphasis */
        
        /* Background colors */
        --dark-bg-1: #0A1621;        /* Deep navy background */
        --dark-bg-2: #152736;        /* Secondary background */
        --dark-bg-3: #203A4D;        /* Element background */
    }
    
    h1, h2, h3, h4 {
        font-family: 'Orbitron', sans-serif;
        font-weight: 600;
        color: var(--amber);
        text-shadow: 0 0 10px rgba(255, 191, 0, 0.5);
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: linear-gradient(135deg, var(--dark-bg-1) 0%, var(--dark-bg-2) 100%);
    }
    
    /* Regular buttons styling */
    .stButton button {
        background: linear-gradient(90deg, var(--teal-dark) 0%, var(--teal-medium) 100%);
        color: var(--dark-bg-1);
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(42, 157, 143, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(42, 157, 143, 0.4);
    }
    
    /* Special styling for Place Bet button - CORAL */
    [data-testid="stForm"] [kind="formSubmit"] button {
        background: linear-gradient(90deg, var(--coral) 0%, var(--coral-dark) 100%);
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 18px;
        padding: 0.7rem 1.5rem;
        border-radius: 8px;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(255, 127, 80, 0.4);
        margin-top: 10px;
        color: var(--dark-bg-1);
    }
    
    [data-testid="stForm"] [kind="formSubmit"] button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(255, 127, 80, 0.6);
    }
    
    .crypto-card {
        background: linear-gradient(135deg, var(--dark-bg-2) 0%, var(--dark-bg-3) 100%);
        color: var(--teal-light);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid var(--teal-medium);
        transition: all 0.3s ease;
    }
    
    .crypto-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    .highlight {
        background-color: rgba(255, 191, 0, 0.15);
        padding: 5px;
        border-radius: 3px;
        color: var(--amber-light);
    }
    
    .result-card {
        background: rgba(32, 58, 77, 0.8);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid var(--coral);
        color: var(--teal-light);
        backdrop-filter: blur(10px);
    }
    
    .game-option {
        margin: 10px;
        padding: 15px;
        border-radius: 10px;
        background: rgba(32, 58, 77, 0.6);
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        color: var(--teal-light);
    }
    
    .game-option:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px);
        background: rgba(32, 58, 77, 0.8);
    }
    
    .info-box {
        background-color: rgba(42, 157, 143, 0.15);
        border-left: 4px solid var(--teal-medium);
        padding: 10px 15px;
        margin-bottom: 15px;
        border-radius: 4px;
        color: var(--teal-light);
    }
    
    .matka-card {
        background: linear-gradient(135deg, var(--dark-bg-2) 0%, var(--dark-bg-3) 100%);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 20px;
        margin: 10px 0;
        transition: transform 0.3s ease;
        color: var(--teal-light);
        border: 1px solid rgba(64, 196, 176, 0.3);
    }
    
    .matka-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        border: 1px solid rgba(64, 196, 176, 0.6);
    }
    
    .crypto-stats {
        background: linear-gradient(135deg, var(--dark-bg-1) 0%, var(--dark-bg-2) 100%);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
        border: 1px solid rgba(64, 196, 176, 0.3);
        color: var(--teal-light);
    }
    
    .token-symbol {
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        color: var(--coral);
    }
    
    /* Apply dark theme */
    .stApp {
        background-color: var(--dark-bg-1);
        color: var(--teal-light);
    }
    
    /* Sidebar styling with TEAL text */
    div[data-testid="stSidebar"] {
        background-color: #152736;
        border-right: 1px solid var(--teal-dark);
    }
    
    /* Basic teal text colors for sidebar elements */
    div[data-testid="stSidebar"] *, 
    div[data-testid="stSidebar"] .element-container div,
    div[data-testid="stSidebar"] p,
    div[data-testid="stSidebar"] span,
    div[data-testid="stSidebar"] label,
    div[data-testid="stSidebar"] div {
        color: var(--teal-medium) !important;
    }
    
    /* Headers and titles in sidebar */
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h4,
    div[data-testid="stSidebar"] .css-10trblm {
        color: var(--amber) !important;
        font-size: 1.5rem;
        margin-bottom: 5px;
    }
    
    /* Sidebar paragraphs */
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: var(--teal-light) !important;
    }
    
    /* Sidebar buttons */
    div[data-testid="stSidebar"] button {
        background-color: var(--teal-dark);
        color: var(--dark-bg-1) !important;
    }
    
    /* Sidebar selectbox */
    div[data-testid="stSidebar"] .stSelectbox [data-baseweb=select] {
        border-color: var(--teal-dark) !important;
        background-color: var(--dark-bg-2) !important;
    }
    
    /* Sidebar expanders */
    div[data-testid="stSidebar"] .stExpander {
        border: 1px solid var(--teal-dark);
        border-radius: 4px;
        background-color: var(--dark-bg-3);
    }
    
    .stNumberInput [data-baseweb=input],
    .stTextInput input,
    .stSelectbox [data-baseweb=select] div,
    .stRadio label {
        color: var(--teal-light) !important;
        font-weight: 500 !important;
        border-color: var(--teal-medium) !important;
    }
    
    .stNumberInput [data-baseweb=input]::placeholder,
    .stTextInput input::placeholder {
        color: rgba(102, 224, 208, 0.5) !important;
    }
    
    div[data-baseweb="select"] > div {
        color: var(--teal-light) !important;
        background-color: var(--dark-bg-3) !important;
        border-color: var(--teal-medium) !important;
    }
    
    div[data-baseweb="select"] > div:hover {
        border-color: var(--teal-light) !important;
    }
    
    div[data-testid="stForm"] {
        background: rgba(32, 58, 77, 0.7);
        border-radius: 10px;
        padding: 20px;
        border: 1px solid var(--teal-medium);
    }
    
    h1 {
        text-shadow: 0 0 10px rgba(255, 191, 0, 0.5);
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(64, 196, 176, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(64, 196, 176, 0); }
        100% { box-shadow: 0 0 0 0 rgba(64, 196, 176, 0); }
    }
    
    .pulse {
        animation: pulse 2s infinite;
        border-radius: 10px;
    }
    
    label, p, span, div {
        color: var(--teal-light) !important;
    }
    
    div[data-testid="stSidebar"] label, 
    div[data-testid="stSidebar"] p, 
    div[data-testid="stSidebar"] span, 
    div[data-testid="stSidebar"] div {
        color: var(--teal-medium) !important;
    }
    
    .stRadio label, .stCheckbox label {
        color: var(--teal-light) !important;
        font-weight: 500 !important;
    }
    
    div[data-testid="stSidebar"] .stRadio label, 
    div[data-testid="stSidebar"] .stCheckbox label {
        color: var(--teal-light) !important;
    }
    
    input, textarea, [data-baseweb=select] {
        color: var(--teal-light) !important;
        border: 1px solid var(--teal-medium) !important;
    }
    
    [data-testid="stMarkdownContainer"] p, li {
        color: var(--teal-light) !important;
    }
    
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p, 
    div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] li {
        color: var(--teal-light) !important;
    }
    
    .css-10trblm {
        color: var(--amber) !important;
    }
    
    div[data-testid="stSidebar"] .css-10trblm {
        color: var(--amber) !important;
    }
    
    .stProgress > div > div {
        background-color: var(--teal-medium);
    }
    
    .stProgress {
        color: var(--teal-light);
    }
    
    [data-baseweb="menu"] {
        background-color: var(--dark-bg-3) !important;
    }
    
    [data-baseweb="menu"] ul li {
        color: var(--teal-light) !important;
    }
    
    [data-baseweb="menu"] ul li:hover {
        background-color: rgba(64, 196, 176, 0.2) !important;
    }
    
    div[data-baseweb="notification"] {
        background-color: var(--dark-bg-2) !important;
        border-color: var(--teal-medium) !important;
        color: var(--teal-light) !important;
    }
    
    section [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    
    h2, h3 {
        background: linear-gradient(90deg, var(--amber-light) 0%, var(--amber) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 1.5rem !important;
        letter-spacing: 1px;
        text-shadow: none;
    }
    
    div[data-testid="stForm"] label {
        color: var(--amber-light) !important;
        font-size: 1.1rem;
        font-weight: 600 !important;
        margin-bottom: 5px;
        font-family: 'Orbitron', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'balance' not in st.session_state:
    st.session_state.balance = 1000
if 'history' not in st.session_state:
    st.session_state.history = []
if 'game_results' not in st.session_state:
    st.session_state.game_results = {}
if 'open_result' not in st.session_state:
    st.session_state.open_result = None
if 'close_result' not in st.session_state:
    st.session_state.close_result = None
if 'current_game' not in st.session_state:
    st.session_state.current_game = "Crypto Kalyan"
if 'player_name' not in st.session_state:
    st.session_state.player_name = "Crypto Gamer"
if 'first_time' not in st.session_state:
    st.session_state.first_time = True

# Game Definitions
GAME_VARIANTS = {
    "Crypto Kalyan": {"open_time": "14:30", "close_time": "16:30", "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]},
    "Web3 Worli": {"open_time": "10:00", "close_time": "12:00", "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]},
    "Metaverse Milan": {"open_time": "12:00", "close_time": "14:00", "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]},
    "NFT Night": {"open_time": "20:30", "close_time": "22:30", "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]},
    "Token Bazar": {"open_time": "13:00", "close_time": "15:00", "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}
}

# Bet types and their payout ratios
BET_TYPES = {
    "Single": {"description": "Betting on a single digit (0-9)", "payout": 9},
    "Double": {"description": "Betting on a pair of digits (00-99)", "payout": 90},
    "Triple": {"description": "Betting on three unique digits (e.g., 123)", "payout": 150},
    "Quadruple": {"description": "Betting on three digits with one repeating (e.g., 112)", "payout": 300},
    "Quintuple": {"description": "Betting on three identical digits (e.g., 777)", "payout": 1000},
    "Half Combo": {"description": "Combination of Single and Triple", "payout": 1200},
    "Full Combo": {"description": "Combination of Open Triple and Close Triple", "payout": 5000}
}

# Functions for game logic
@st.cache_data
def validate_jodi(jodi):
    """Validate that jodi is a two-digit number"""
    try:
        jodi_num = int(jodi)
        return 0 <= jodi_num <= 99
    except ValueError:
        return False

@st.cache_data
def validate_pana(pana):
    """Validate that pana is a three-digit number"""
    try:
        pana_num = int(pana)
        return 100 <= pana_num <= 999
    except ValueError:
        return False

def calculate_result():
    """Calculate game result (3 cards/numbers drawn)"""
    # Drawing 3 cards (numbers from 0-9)
    cards = [random.randint(0, 9) for _ in range(3)]
    
    # Calculate sum and last digit
    total_sum = sum(cards)
    last_digit = total_sum % 10
    
    # Full result in the format: card1,card2,card3 * last_digit
    result_text = f"{cards[0]},{cards[1]},{cards[2]} * {last_digit}"
    
    # Result number: sum of cards and last digit
    result_number = int(f"{total_sum % 10}")
    
    # Result pana: 3 digits
    result_pana = f"{cards[0]}{cards[1]}{cards[2]}"
    
    return {
        "cards": cards,
        "sum": total_sum,
        "last_digit": last_digit,
        "text": result_text,
        "number": result_number,
        "pana": result_pana
    }

def check_win(bet_type, bet_value, result, bet_amount):
    """Check if the bet is a winner and calculate winnings"""
    winnings = 0
    won = False
    
    if bet_type == "Single":
        if str(bet_value) == str(result["last_digit"]):
            winnings = bet_amount * BET_TYPES["Single"]["payout"]
            won = True
            
    elif bet_type == "Double":
        if str(bet_value) == f"{st.session_state.open_result['last_digit']}{st.session_state.close_result['last_digit']}":
            winnings = bet_amount * BET_TYPES["Double"]["payout"]
            won = True
            
    elif bet_type == "Triple":
        if str(bet_value) == str(result["pana"]):
            winnings = bet_amount * BET_TYPES["Triple"]["payout"]
            won = True
            
    elif bet_type == "Quadruple":
        if str(bet_value) == str(result["pana"]):
            winnings = bet_amount * BET_TYPES["Quadruple"]["payout"]
            won = True
            
    elif bet_type == "Quintuple":
        if str(bet_value) == str(result["pana"]):
            winnings = bet_amount * BET_TYPES["Quintuple"]["payout"]
            won = True
    
    return {"won": won, "winnings": winnings}

def simulate_results():
    """Simulate open and close results for demo purposes"""
    if st.session_state.open_result is None:
        st.session_state.open_result = calculate_result()
    
    if st.session_state.close_result is None:
        st.session_state.close_result = calculate_result()
        
        # Create Jodi result (combination of open and close)
        jodi = f"{st.session_state.open_result['last_digit']}{st.session_state.close_result['last_digit']}"
        st.session_state.jodi_result = jodi

# App Sidebar
with st.sidebar:
    colored_header(label="🎮 Crypto Gamer Dashboard", description="Your gaming statistics", color_name="violet-70")
    
    # Player profile
    if st.session_state.first_time:
        st.session_state.player_name = st.text_input("Enter Your Crypto Alias", value="Crypto Gamer")
        if st.button("Start Gaming"):
            st.session_state.first_time = False
            st.rerun()
    
    if not st.session_state.first_time:
        col1, col2 = st.columns([1, 2])
        with col1:
            # Generate avatar URL based on username
            avatar_url = f"https://api.dicebear.com/7.x/micah/svg?seed={st.session_state.player_name}&backgroundColor=6E01EF"
            st.image(avatar_url, width=80)
        
        with col2:
            st.markdown(f"### {st.session_state.player_name}")
            st.markdown(f"**Balance**: <span class='token-symbol'>OP</span> {st.session_state.balance:.2f}", unsafe_allow_html=True)
        
        st.divider()
        
        # Game Selection
        st.subheader("Select Game Variant")
        selected_game = st.selectbox("Choose a game variant", list(GAME_VARIANTS.keys()))
        
        if selected_game != st.session_state.current_game:
            st.session_state.current_game = selected_game
            st.session_state.open_result = None
            st.session_state.close_result = None
            st.rerun()
        
        game_info = GAME_VARIANTS[st.session_state.current_game]
        
        # Display game details
        with st.expander("Game Schedule", expanded=True):
            st.write(f"**Opening Time**: {game_info['open_time']}")
            st.write(f"**Closing Time**: {game_info['close_time']}")
            st.write("**Playing Days**:")
            st.write(", ".join(game_info['days']))
            
        # Display winning history
        with st.expander("Your Recent Results", expanded=False):
            if len(st.session_state.history) > 0:
                hist_df = pd.DataFrame(st.session_state.history)
                st.dataframe(hist_df[['game', 'bet_type', 'amount', 'result']], use_container_width=True)
            else:
                st.info("No game history yet. Start playing!")
                
        # Simple visualization
        if len(st.session_state.history) > 0:
            with st.expander("Performance Chart", expanded=False):
                hist_df = pd.DataFrame(st.session_state.history)
                results = hist_df['result'].tolist()
                wins = results.count('Win')
                losses = results.count('Loss')
                
                fig = px.pie(
                    names=['Wins', 'Losses'],
                    values=[wins, losses],
                    color=['Wins', 'Losses'],
                    color_discrete_map={'Wins': '#6E01EF', 'Losses': '#F43F5E'},
                    hole=0.4
                )
                fig.update_layout(
                    margin=dict(l=20, r=20, t=30, b=20),
                    height=250,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white')
                )
                st.plotly_chart(fig, use_container_width=True)
                
        # Reset game button
        if st.button("Reset Game", help="Reset your balance and game history"):
            st.session_state.balance = 1000
            st.session_state.history = []
            st.session_state.open_result = None
            st.session_state.close_result = None
            st.success("Game reset successfully!")
            time.sleep(1)
            st.rerun()

# Main game interface
colored_header(label="🎰 Ancient8 Fortune Wheels", description="Web3 Gaming with Crypto Rewards", color_name="violet-70")

# Introduction and tutorial
with st.expander("How to Play - Quick Guide", expanded=st.session_state.first_time):
    st.markdown("""
    ## Ancient8 Fortune Wheels - Gaming Guide
    
    **Ancient8 Fortune Wheels** is a Web3 gaming experience inspired by traditional number-based games but with a modern crypto twist.
    
    ### Game Rules
    
    1. **Choose a Game Variant**: Select from our collection of crypto-themed games
    2. **Select Bet Type**: Choose what kind of bet you want to place
    3. **Place Your Bet**: Enter your bet amount in OP tokens and select your numbers
    4. **Wait for Results**: Each game has two draws - opening and closing
    5. **Check Results**: See if your numbers match the results
    6. **Collect Winnings**: If you win, your OP token balance will be updated automatically
    7. **Track Performance**: Monitor your gaming history in the dashboard
    
    ### Bet Types
    """)
    
    # Display bet types in a nicely formatted way
    col1, col2 = st.columns(2)
    for i, (bet_name, bet_info) in enumerate(BET_TYPES.items()):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="info-box">
                <strong>{bet_name}</strong>: {bet_info['description']}<br>
                <em>Payout ratio: {bet_info['payout']}x</em>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight pulse">⚠️ Reminder: This is a simulation for entertainment purposes only. Gaming can be addictive and may lead to financial losses.</div>
    """, unsafe_allow_html=True)

# Main Game Container
if not st.session_state.first_time:
    # Game header
    st.subheader(f"Playing: {st.session_state.current_game}")
    
    # Simulate game results (for demonstration)
    simulate_results()
    
    # Crypto market animation
    st.markdown("""
    <div class="crypto-stats">
        <h4>Live Crypto Market</h4>
        <div style="display: flex; justify-content: space-between;">
            <div>OP/USDT: <span style="color: #22C55E;">$3.45 (+5.2%)</span></div>
            <div>ETH/USDT: <span style="color: #22C55E;">$3,245.78 (+2.1%)</span></div>
            <div>A8/USDT: <span style="color: #22C55E;">$0.87 (+8.3%)</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display results
    st.markdown("### Today's Results")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <h4>Opening Result</h4>
            <p>{st.session_state.open_result['text']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <h4>Closing Result</h4>
            <p>{st.session_state.close_result['text']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="result-card" style="border-left: 5px solid #8B5CF6;">
        <h4>Combined Result</h4>
        <p style="font-size: 1.2rem; font-weight: bold;">{st.session_state.open_result['last_digit']}{st.session_state.close_result['last_digit']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Place bet section
    st.markdown("### Place Your Bet")
    
    with st.form("bet_form"):
        # Bet type selection
        bet_type = st.selectbox("Select Bet Type", list(BET_TYPES.keys()))
        
        # Dynamic form based on bet type
        if bet_type == "Single":
            bet_value = st.number_input("Enter a digit (0-9)", min_value=0, max_value=9, step=1)
            bet_timing = st.radio("Select Timing", ["Open", "Close"])
            
        elif bet_type == "Double":
            bet_value = st.text_input("Enter a two-digit number (00-99)")
            bet_timing = "Full Day"
            
        elif bet_type in ["Triple", "Quadruple", "Quintuple"]:
            bet_value = st.text_input("Enter a three-digit number (100-999)")
            bet_timing = st.radio("Select Timing", ["Open", "Close"])
            
        elif bet_type == "Half Combo":
            col1, col2 = st.columns(2)
            with col1:
                digit = st.number_input("Enter Single Digit (0-9)", min_value=0, max_value=9, step=1)
            with col2:
                patti = st.text_input("Enter Triple (3 digits)")
            bet_value = f"{digit}-{patti}"
            bet_timing = st.radio("Select Combination", ["Open Single + Close Triple", "Open Triple + Close Single"])
            
        elif bet_type == "Full Combo":
            col1, col2 = st.columns(2)
            with col1:
                open_pana = st.text_input("Enter Open Triple (3 digits)")
            with col2:
                close_pana = st.text_input("Enter Close Triple (3 digits)")
            bet_value = f"{open_pana}-{close_pana}"
            bet_timing = "Full Day"
        
        # Bet amount
        bet_amount = st.number_input("Bet Amount (OP Tokens)", min_value=10, max_value=st.session_state.balance, step=10)
        
        # Display payout info
        st.info(f"Potential winnings: OP {bet_amount * BET_TYPES[bet_type]['payout']:.2f} (Payout ratio: {BET_TYPES[bet_type]['payout']}x)")
        
        # Submit button
        submitted = st.form_submit_button("Place Bet")
        
    # Process bet submission
    if submitted:
        valid_bet = True
        error_message = ""
        
        # Validate bet values
        if bet_type == "Double" and not validate_jodi(bet_value):
            valid_bet = False
            error_message = "Double must be a two-digit number between 00-99"
            
        elif bet_type in ["Triple", "Quadruple", "Quintuple"] and not validate_pana(bet_value):
            valid_bet = False
            error_message = "Triple must be a three-digit number between 100-999"
        
        # Process valid bet
        if valid_bet:
            # Deduct bet amount
            st.session_state.balance -= bet_amount
            
            # Determine result based on timing
            result = st.session_state.open_result if bet_timing == "Open" else st.session_state.close_result
            
            # Check if bet is a winner
            if bet_type == "Single":
                win_check = check_win(bet_type, bet_value, result, bet_amount)
                win_status = win_check["won"]
                winnings = win_check["winnings"]
                
            elif bet_type == "Double":
                jodi_result = f"{st.session_state.open_result['last_digit']}{st.session_state.close_result['last_digit']}"
                win_status = str(bet_value) == jodi_result
                winnings = bet_amount * BET_TYPES["Double"]["payout"] if win_status else 0
                
            elif bet_type in ["Triple", "Quadruple", "Quintuple"]:
                win_status = str(bet_value) == result["pana"]
                winnings = bet_amount * BET_TYPES[bet_type]["payout"] if win_status else 0
                
            else:
                # For simplicity, we'll use random win determination for combo bets in this demo
                win_status = random.random() < 0.05  # 5% chance to win combo bets
                winnings = bet_amount * BET_TYPES[bet_type]["payout"] if win_status else 0
            
            # Update balance and history
            if win_status:
                st.session_state.balance += winnings
                result_text = "Win"
                st.balloons()
                st.success(f"🎉 Congratulations! You won OP {winnings:.2f} tokens!")
            else:
                result_text = "Loss"
                st.error("Sorry, you lost this bet. Try again!")
            
            # Record this bet in history
            st.session_state.history.append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "game": st.session_state.current_game,
                "bet_type": bet_type,
                "bet_value": bet_value,
                "timing": bet_timing,
                "amount": bet_amount,
                "result": result_text,
                "winnings": winnings if win_status else 0
            })
            
            # Force refresh
            time.sleep(2)
            st.rerun()
        else:
            st.error(error_message)
    
    # Game Info Section
    st.markdown("### Popular Game Variants")
    
    # Create a row of cards for different games
    cols = st.columns(3)
    for i, (game_name, game_data) in enumerate(list(GAME_VARIANTS.items())[:3]):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="matka-card">
                <h4>{game_name}</h4>
                <p><strong>Open:</strong> {game_data['open_time']}<br>
                <strong>Close:</strong> {game_data['close_time']}</p>
                <p><em>Gaming days:</em> {", ".join(game_data['days'][:3])}...</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tips for Players
    with st.expander("Tips for Players"):
        st.markdown("""
        ### 🎯 Tips for Crypto Gamers
        
        1. **Start Small**: Begin with smaller bets to understand the game mechanics
        2. **Learn the Odds**: Different bet types have different payout ratios
        3. **Track Results**: Monitor patterns in results over time
        4. **Manage Your Tokens**: Set a budget and stick to it
        5. **Understand the Game**: Learn all the terminology and calculation methods
        
        Remember, this is primarily a game of chance. Play responsibly!
        """)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 20px; background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border-radius: 10px; color: white;">
    <p>Ancient8 Fortune Wheels - Web3 Gaming Experience</p>
    <p style="font-size: 0.8rem;">Created for educational and entertainment purposes only. No real cryptocurrency is involved.</p>
    <p style="font-size: 0.7rem;">© 2025 Ancient8 - All rights reserved</p>
</div>
""", unsafe_allow_html=True) 