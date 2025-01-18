import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import requests
from wordcloud import WordCloud

# Set Streamlit page configuration
st.set_page_config(
    page_title="Brad's Biography and Thesis Defense",
    layout="wide",
    initial_sidebar_state="expanded",
)

def add_background():
    background_css = """
    <style>
    body {
        background: linear-gradient(135deg, #2c3e50, #4ca1af);
        color: white;
    }
    .stButton > button {
        background-color: #4ca1af;
        color: white;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton > button:hover {
        background-color: #2c3e50;
    }
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

add_background()

def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading image: {e}")
        return None

def main():
    st.title("Brad's Biography and Thesis Defense")

    # Add a header image with cyber security theme
    banner_image = load_image_from_url(
        "https://media.istockphoto.com/id/2150426978/photo/cybersecurity-and-privacy-concepts-to-protect-data-lock-icon-and-internet-network.jpg"
    )
    if banner_image:
        st.image(banner_image, use_column_width=True, caption="Cybersecurity and Privacy Concepts")

    # Biography Section
    with st.container():
        st.header("Biography")
        st.write(
            "Hello! I'm Brad, a US Navy veteran, avid AI researcher, and cybersecurity professional. "
            "I enjoy spending my free time as a beach bum and cherish moments with my family. "
            "I am currently pursuing a PhD in Artificial Intelligence at Capitol Technology University, with my defense planned for Winter 2025."
        )
        # Add a career highlights timeline
        st.subheader("Career Highlights")
        fig, ax = plt.subplots(facecolor="#4ca1af")
        ax.barh(
            ["Cybersecurity Professional", "US Navy Service", "PhD Research", "AI & Cybersecurity"], 
            [10, 10, 5, 8], color='white', edgecolor='black'
        )
        ax.set_title("Brad's Career Timeline", color='white')
        ax.tick_params(colors='white')
        fig.patch.set_facecolor("#4ca1af")
        st.pyplot(fig)

    # Thesis Defense Section
    with st.container():
        st.header("Thesis Defense")
        st.write(
            "My PhD thesis is titled 'Leveraging Artificial Intelligence for Enhanced Cybersecurity Solutions: Challenges, Opportunities, and Future Directions.' "
            "The research focuses on integrating AI technologies into cybersecurity frameworks to predict vulnerabilities, identify threats in real time, and implement automated mitigation strategies."
        )
        st.write(
            "The tool I developed as part of this research integrates data from CVE.org and Red Hat API for comprehensive vulnerability assessments, "
            "including predictive analysis, anomaly detection, and sandboxing capabilities. This tool is a cornerstone of my defense, showcasing its production-ready automation capabilities."
        )
        # Add a thesis framework image
        thesis_image = load_image_from_url(
            "https://cdn.pixabay.com/photo/2023/05/08/09/57/ai-generated-hacker-safety-computer-8002660_960_720.jpg"
        )
        if thesis_image:
            st.image(thesis_image, caption="AI-Powered Cybersecurity Framework", use_column_width=True)

    # Goals Section
    with st.container():
        st.header("Goals")
        st.write("Here are my short-term and long-term goals:")
        st.markdown(
            "- Achieve a production-ready, fully automated vulnerability management program within one year.\n"
            "- Complete my PhD and secure a high-paying remote research role in AI and cybersecurity.\n"
            "- Develop AI models that redefine threat detection and response in cybersecurity.\n"
            "- Launch my home health aid business, Caring Hands Home Health Aid Services, in Orlando, FL in two years.\n"
            "- Maintain a balanced and healthy lifestyle while excelling professionally."
        )
        # Add a goals distribution pie chart
        goals_labels = ["Vulnerability Management", "PhD Completion", "AI Models", "Business Launch", "Personal Growth"]
        goals_sizes = [25, 20, 30, 15, 10]
        fig2, ax2 = plt.subplots(facecolor="#4ca1af")
        ax2.pie(goals_sizes, labels=goals_labels, autopct='%1.1f%%', startangle=140, colors=["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"])
        ax2.set_title("Goals Distribution", color='white')
        fig2.patch.set_facecolor("#4ca1af")
        st.pyplot(fig2)

    # Key Points from Resume Section
    with st.container():
        st.header("Key Points from My Resume")
        st.write("Here are some highlights of my professional and academic journey:")
        st.markdown(
            "- **Core Competencies:** Information Security Standards, Project Management, Governance Risk Compliance (GRC), Vulnerability Management, and Artificial Intelligence.\n"
            "- **Professional Experience:**\n"
            "  - Cybersecurity roles at various organizations.\n"
            "  - Extensive experience in Vulnerability management, security assesments, engagements, IAM, IT audit, and compliance.\n"
            "- **Technical Skills:** Proficient in Python, CUDA, TensorFlow, VMware, and Linux Administration.\n"
            "- **Research Contributions:** Developing research papers on AI-driven cybersecurity solutions and presented findings at conferences.\n"
            "- **Leadership:** Over a decade of leadership experience, including service in the US Navy."
        )
        # Add a word cloud for resume keywords
        resume_text = "Information Security Standards Project Management Governance Risk Compliance Vulnerability Management Artificial Intelligence Python CUDA TensorFlow VMware Linux Administration Leadership"
        wordcloud = WordCloud(width=800, height=400, background_color='#4ca1af', colormap='viridis').generate(resume_text)
        fig3, ax3 = plt.subplots()
        ax3.imshow(wordcloud, interpolation='bilinear')
        ax3.axis('off')
        fig3.patch.set_facecolor("#4ca1af")
        st.pyplot(fig3)

    # Closing Section
    with st.container():
        st.header("Let's Connect")
        st.write(
            "If you'd like to learn more about my work or connect with me, feel free to reach out!"
        )
        st.markdown(
            "[Connect with me on LinkedIn](https://www.linkedin.com/in/bradolton/)"
        )

if __name__ == "__main__":
    main()

