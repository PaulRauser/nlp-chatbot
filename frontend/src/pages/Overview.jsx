import { useState } from "react";
import Footer from "../components/Footer.jsx";

function Overview() {
    const [selectedTheme, setSelectedTheme] = useState("dark-theme");

    const setTheme = (theme) => {
        document.body.classList.remove("dark-theme", "light-theme", "race-theme");
        document.body.classList.add(theme);
        setSelectedTheme(theme);
    };

    return (
        <>
            <div className="mainContainer">
                <iframe
                    class="backgroundVideo"
                    src="https://www.youtube.com/embed/2ZjPFBwEx0I?si=BuAztgiYCa12yTU0&autoplay=1&mute=1&loop=1&playlist=2ZjPFBwEx0I"
                    title="Background video"
                    frameborder="0"
                    allow="autoplay; encrypted-media; picture-in-picture fullscreen"
                    allowfullscreen
                ></iframe>
                <div className="header">
                    <div className="logoSection">
                        LOGO <br></br> HERE
                    </div>
                    <div className="themeSelector">
                        <span
                            onClick={() => setTheme("dark-theme")}
                            className="selectorButton"
                        ></span>
                        <span
                            onClick={() => setTheme("light-theme")}
                            className="selectorButton"
                        ></span>
                        <span
                            onClick={() => setTheme("race-theme")}
                            className="selectorButton"
                        ></span>
                    </div>
                </div>
                <div className="botContainer"></div>
                <Footer />
            </div>
        </>
    );
}

export default Overview;
