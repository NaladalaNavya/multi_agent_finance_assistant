import streamlit as st
import requests
import tempfile
from streamlit_webrtc import webrtc_streamer
import av

st.set_page_config(page_title="Finance Assistant", layout="centered")
st.title("📈 Multi-Agent Finance Assistant")

option = st.radio("Choose your input type:", ["Text", "Microphone"])

# --- Text-based query ---
if option == "Text":
    user_input = st.text_input("Ask your market query:")
    if st.button("Submit") and user_input:
        try:
            response = requests.post(
                "http://localhost:8009/ask/text",
                params={"query": user_input},
                timeout=10
            )
            st.markdown("### 📢 Assistant's Response")
            st.write(response.json().get("response"))
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Text error: {e}")

# --- Microphone-based query using legacy webrtc_streamer ---
elif option == "Microphone":
    st.info("🎙 Speak into your mic and click 'Submit Voice'")

    ctx = webrtc_streamer(key="audio", sendback_audio=True)

    if st.button("Submit Voice"):
        if ctx.audio_receiver:
            try:
                audio_frames = ctx.audio_receiver.get_frames(timeout=5)

                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
                    with av.open(tmpfile.name, mode='w', format='wav') as container:
                        stream = container.add_stream("pcm_s16le")
                        for frame in audio_frames:
                            container.mux(frame)
                    tmp_path = tmpfile.name

                files = {'file': open(tmp_path, 'rb')}
                response = requests.post(
                    "http://localhost:8009/ask/audio",
                    files=files,
                    timeout=10
                )
                st.markdown("### 🎤 Assistant's Response")
                st.write(response.json().get("response"))

            except Exception as e:
                st.error(f"❌ Voice processing failed: {e}")
        else:
            st.warning("No audio captured. Please speak and try again.")
