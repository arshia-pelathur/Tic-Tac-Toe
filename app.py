import streamlit as st
import numpy as np
from game_logic import TicTacToe  # Import the TicTacToe class from game_logic.py

# Initialize session state for game
if "game" not in st.session_state:
    st.session_state.game = TicTacToe()
    st.session_state.is_user_turn = True  # User should start first

# Load external CSS for dark theme
with open("style.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# Game logic reference
game = st.session_state.game

# Streamlit layout
st.title("Tic Tac Toe: AI vs You")
st.write("Play against the AI. You are 'X', and the AI is 'O'.")


# Display the board as a grid
for row in range(3):
    cols = st.columns(3, gap="medium")
    for col in range(3):
        with cols[col]:
            label = game.board[row, col] or " "
            if st.button(label, key=f"{row}-{col}", use_container_width=True):
                if game.make_move(row, col, "X") and st.session_state.is_user_turn:
                    # Update the session state to reflect user's move
                    st.session_state.game = game
                    st.session_state.is_user_turn = False  # User's turn is over
                    st.rerun()  # Rerun to reflect the user's move

# After the user's move, AI makes a move if the game is not over and it is AI's turn
if not game.current_winner and not game.is_draw() and not st.session_state.is_user_turn:
    ai_move = game.get_ai_move()
    if ai_move is not None:
        ai_row, ai_col = ai_move
        game.make_move(ai_row, ai_col, "O")
        st.session_state.game = game
        st.session_state.is_user_turn = True  # AI's turn is over, user's turn next
        st.rerun()  # Rerun to reflect the AI's move

# Display winner or game status
if game.current_winner:
    winner = "You" if game.current_winner == "X" else "AI"
    st.success(f"{winner} won the game!")
elif game.is_draw():
    st.success("It's a draw!")

# Restart the game
if st.button("Restart Game"):
    # Clear session state to remove the previous game data
    del st.session_state["game"]
    del st.session_state["is_user_turn"]
    # Rerun the application to reflect the reset state
    st.rerun()
