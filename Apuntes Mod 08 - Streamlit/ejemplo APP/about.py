import streamlit as st


def about_app():
    st.subheader("Nothing Here! :no_pedestrians:")

    st.markdown(body = '<iframe title="Report Section" width="1000" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiZDQyZTBiMDItYTQ5Zi00MDY4LTk1MDItNWFlNDkwYzdhNDE3IiwidCI6ImJjODI5OTJkLWNjMDEtNGVlNy1iZTEzLTFiZTk3Y2Y4NzM3ZSIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>',
                unsafe_allow_html = True)

if __name__ == "__about_app__":
    about_app()