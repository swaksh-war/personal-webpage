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
        st.image(r"https://www.google.com/url?sa=i&url=https%3A%2F%2Fleetcode.com%2Fsubscribe%2F&psig=AOvVaw1XrEMyTfrx-i2bDtl0hv7K&ust=1652296699193000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLjltoHT1fcCFQAAAAAdAAAAABAN")
    with text_col:
        st.subheader("My preffered coding platform for practising DSA")
        st.write("""Anyone can use LeetCode as their Placement preparation training ground for Technical rounds""")
        st.markdown("[Link to My LeetCode profile](https://leetcode.com/swaksh-war/)")

with st.container():
    linkedin_container, github_container, instagram_container = st.columns((1,1,1))
    with linkedin_container:
        st.image(r"https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3ALinkedIn_logo_initials.png&psig=AOvVaw1nOpaaUjbnANWQhE470IQL&ust=1652296728363000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCPj_mI_T1fcCFQAAAAAdAAAAABAD")
        st.markdown("[Link to my profile.](https://www.linkedin.com/in/swakshwar-ghosh-076425211/)")
    
    with github_container:
        st.image(r"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fgithub-logo_25231&psig=AOvVaw1i2aQ3HzotMR1CX7lZm-vn&ust=1652296748245000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCNCyo5rT1fcCFQAAAAAdAAAAABAD")
        st.markdown("[Link to my profile.](https://github.com/swaksh-war/)")
    
    with instagram_container:
        st.image(r"https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3AInstagram_logo_2016.svg&psig=AOvVaw3WbcMVPOmfV0r5mb1NTn0A&ust=1652296774976000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCOi8-aXT1fcCFQAAAAAdAAAAABAD")
        st.markdown("[Link to my profile.](https://www.instagram.com/swaksh.war/?hl=en)")