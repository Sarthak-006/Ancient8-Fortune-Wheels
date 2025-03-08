# Digital Matka - Modern Implementation of the Traditional Number Game

![Matka Game Banner](https://img.shields.io/badge/Digital-Matka-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Digital Matka is a modern, interactive web application built with Streamlit that simulates the traditional Indian Matka gambling game. This application is designed for educational purposes only to demonstrate how the Matka game works.

## 📋 Features

- **Multiple Game Variants**: Play popular Matka variants like Kalyan, Worli, Milan Day, etc.
- **Interactive UI**: Modern and responsive user interface with animations
- **Real-time Results**: Simulated opening and closing results
- **Bet Types**: Support for all major bet types (Single, Jodi, Patti, Sangam)
- **Player Statistics**: Track your betting history and performance
- **Responsive Design**: Works on desktop and mobile devices
- **Virtual Balance**: Start with ₹1000 virtual currency

## 🚀 Quick Start

### Live Demo

Try the application online:
[Digital Matka Demo](https://matka-game.streamlit.app/)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/digital-matka.git
   cd digital-matka
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   The app will be available at http://localhost:8501

## 🎮 How to Play

1. Enter your player name
2. Choose a Matka game variant from the sidebar
3. Select the type of bet you want to place
4. Enter your bet amount and number(s)
5. Wait for the results to see if you've won

## 🌟 Bet Types Explained

| Bet Type | Description | Payout Ratio |
|----------|-------------|--------------|
| Single | Betting on a single digit (0-9) | 9x |
| Jodi | Betting on a pair of digits (00-99) | 90x |
| Single Patti | Betting on three unique digits | 150x |
| Double Patti | Betting on three digits with one repeating | 300x |
| Triple Patti | Betting on three identical digits | 1000x |
| Half Sangam | Combination of Single and Patti | 1200x |
| Full Sangam | Combination of Open Patti and Close Patti | 5000x |

## 🔧 Technical Details

The application is built using:

- **Python 3.9+**: Core programming language
- **Streamlit 1.31+**: For the web application framework
- **Pandas**: For data handling and manipulation
- **Plotly**: For interactive visualizations
- **Streamlit Extras**: For enhanced UI components

## 🚀 Deploying to Streamlit Cloud

1. **Push your code to GitHub**
   
   First, create a repository on GitHub and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/digital-matka.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository, branch (main), and the path to the app file (app.py)
   - Click "Deploy"

## 📝 Educational Disclaimer

This application is created for educational and entertainment purposes only. No real money is involved, and the application does not promote or encourage actual gambling. The intent is to demonstrate:

1. How the traditional Matka game works
2. The mathematical probabilities involved
3. Modern web application development with Python and Streamlit

## 📱 Screenshots

![Screenshot 1](https://via.placeholder.com/800x400?text=Game+Interface)
![Screenshot 2](https://via.placeholder.com/800x400?text=Betting+Screen)
![Screenshot 3](https://via.placeholder.com/800x400?text=Results+Display)

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

⭐ If you found this project interesting, please consider giving it a star on GitHub!

Created with ❤️ using Streamlit 