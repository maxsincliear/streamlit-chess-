// Chessboard.jsx
import React, { useState } from "react";
import { Chessboard } from "react-chessboard";

function MyChessboard({ onMove }) {
    const [gamePosition, setGamePosition] = useState("start");

    return (
        <Chessboard
            position={gamePosition}
            onPieceDrop={(source, target) => {
                onMove({ from: source, to: target });
                // Update view immediately
                setGamePosition((prev) => {
                    // Ideally you validate move first
                    // But here we just move blindly
                    // Handle validation in Streamlit afterwards
                    return { ...prev }; 
                });
                return true;
            }}
        />
    )
}

export default MyChessboard;
