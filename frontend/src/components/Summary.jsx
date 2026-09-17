export default function Summary({ text }) {
    return (
        <div style={{
            background: "#f5f5f5",
            borderRadius: 8,
            padding: 20,
            marginBottom: 24
        }}>
            <h3>Document Summary</h3>
             <p style={{ lineHeight: 1.7 }}>{text}</p>
        </div>

    );
}