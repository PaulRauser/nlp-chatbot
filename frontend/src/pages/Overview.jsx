import { useState } from "react";
import Footer from "../components/Footer.jsx";
import axios from "axios";

import logo from "../assets/Logo_Nürburgring_Circuit.svg";

function Overview() {
    const [selectedTheme, setSelectedTheme] = useState("dark-theme");
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([]);

    const setTheme = (theme) => {
        document.body.classList.remove("dark-theme", "light-theme", "race-theme");
        document.body.classList.add(theme);
        setSelectedTheme(theme);
    };

    const handleInput = (event) => {
        setInput(event.target.value);
    };

    const handleSendMessage = async () => {
        if (!input) {
            console.warn("No input provided");
            return;
        }

        try {
            const response = await axios.post("http://localhost:5001/test", {
                text: input,
            });

            const responseText = response.data.text;

            setMessages((prevMessages) => [
                { sender: "testUser", text: input },
                ...prevMessages,
            ]);
            setMessages((prevMessages) => [
                { sender: "bot", text: responseText },
                ...prevMessages,
            ]);
        } catch (error) {
            console.error("Error:", error);
        } finally {
            setInput("");
        }
    };

    const handleKeyPress = (event) => {
        if (event.key === "Enter") {
            handleSendMessage();
        }
    };

    return (
        <>
            <div className="mainContainer">
                <div className="header">
                    <div className="logoSection">
                        <img className="logo" src={logo} alt="nürburgring logo" />
                    </div>
                    <div className="themeSelector">
                        <span
                            onClick={() => setTheme("light-theme")}
                            className="selectorButton"
                        ></span>
                        <span
                            onClick={() => setTheme("dark-theme")}
                            className="selectorButton"
                        ></span>
                        <span
                            onClick={() => setTheme("race-theme")}
                            className="selectorButton"
                        ></span>
                    </div>
                </div>
                <div className="contentContainer">
                    {selectedTheme === "race-theme" && (
                        <iframe
                            class="backgroundVideo"
                            src="https://www.youtube.com/embed/mn07l5d55Jw?si=LEmX5oL89-KQLArj&autoplay=1&mute=1&loop=1&playlist=mn07l5d55Jw&controls=0&modestbranding=1&rel=0&iv_load_policy=3&playsinline=1&vq=hd1080"
                            title="Background video"
                            frameborder="0"
                            allow="autoplay; encrypted-media; fullscreen"
                            allowfullscreen
                        ></iframe>
                    )}
                    <div className="botContainer">
                        <div className="botHeader">
                            <div className="certaintyHeader">Certainty Score</div>
                            <div className="certaintyMeter"></div>
                        </div>

                        <div className="botMain">
                            {messages.map((message, index) => (
                                <div
                                    className={
                                        message.sender === "bot" ? "botReply" : "botQuestion"
                                    }
                                    key={index}
                                >
                                    <div className="text">{message.text}</div>
                                </div>
                            ))}
                        </div>
                        <div className="inputContainer">
                            <input
                                onChange={handleInput}
                                onKeyDown={handleKeyPress}
                                className="botInput"
                                type="text"
                                value={input}
                                placeholder="Type your question..."
                            ></input>
                            <svg
                                onClick={handleSendMessage}
                                id="sendIcon"
                                viewBox="0 0 24 24"
                                fill="none"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path d="M11.5003 12H5.41872M5.24634 12.7972L4.24158 15.7986C3.69128 17.4424 3.41613 18.2643 3.61359 18.7704C3.78506 19.21 4.15335 19.5432 4.6078 19.6701C5.13111 19.8161 5.92151 19.4604 7.50231 18.7491L17.6367 14.1886C19.1797 13.4942 19.9512 13.1471 20.1896 12.6648C20.3968 12.2458 20.3968 11.7541 20.1896 11.3351C19.9512 10.8529 19.1797 10.5057 17.6367 9.81135L7.48483 5.24303C5.90879 4.53382 5.12078 4.17921 4.59799 4.32468C4.14397 4.45101 3.77572 4.78336 3.60365 5.22209C3.40551 5.72728 3.67772 6.54741 4.22215 8.18767L5.24829 11.2793C5.34179 11.561 5.38855 11.7019 5.407 11.8459C5.42338 11.9738 5.42321 12.1032 5.40651 12.231C5.38768 12.375 5.34057 12.5157 5.24634 12.7972Z" />
                            </svg>
                        </div>
                    </div>
                </div>
                <Footer />
            </div>
        </>
    );
}

export default Overview;
