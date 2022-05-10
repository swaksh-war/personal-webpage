import streamlit as st

st.markdown("# Swakshwar Ghosh")
st.markdown("### Developer and Problem Solving Enthusiast")

st.markdown("""
        I am a budding software developer and a problem solving enthusiast,
        Currently Pursuing my B.Tech from Lovely Proffessional University, Jalandhar, Punjab.
        I mostly do DSA and make different projects mostly on backend using Django and Django Rest Framework 
""")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(r"static\LeetCode.png")
    with text_col:
        st.subheader("My preffered coding platform for practising DSA")
        st.write("""Anyone can use LeetCode as their Placement preparation training ground for Technical rounds""")
        st.markdown("[Link to My LeetCode profile](https://leetcode.com/swaksh-war/)")

with st.container():
    image_lkdn = r"static\linkedin.png"
    image_insta = r"static\Instagram.png"
    image_github = r"static\github.png"
    linkedin_container, github_container, instagram_container = st.columns((1,1,1))
    with linkedin_container:
        st.image(image_lkdn)
        st.markdown("[Link to my profile.](https://www.linkedin.com/in/swakshwar-ghosh-076425211/)")
    
    with github_container:
        st.image(image_github)
        st.markdown("[Link to my profile.](https://github.com/swaksh-war/)")
    
    with instagram_container:
        st.image(image_insta)
        st.markdown("[Link to my profile.](https://www.instagram.com/swaksh.war/?hl=en)")