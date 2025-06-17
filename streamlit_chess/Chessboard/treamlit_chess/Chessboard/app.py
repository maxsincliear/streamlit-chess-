import streamlit as st
import streamlit.components.v1 as components
import chess

# Initialize game
if "board" not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

# Declare custom component path
_chessboard = components.declare_component("Chessboard", path="./streamlit_chess/Chessboard")

st.title("♟ Streamlit Chess - Interactive")

# Handle move from the board
move = _chessboard()
if move:
    from_sq = move['from']
    to_sq = move['to']

    move = chess.Move.from_uci(from_sq + to_sq)

    if move in board.legal_moves:
        board.push(move)
    else:
        st.error("Invalid move!")

# Display FEN for debug
st.text(f"Current FEN: {board.fen}")
