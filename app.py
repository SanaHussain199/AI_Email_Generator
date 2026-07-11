import streamlit as st

st.set_page_config(page_title="AI Email Generator", page_icon="📧")

st.title("📧 AI Professional Email Generator")
st.write("Generate professional emails easily.")

email_type = st.selectbox(
    "Email Type",
    [
        "Job Application",
        "Follow-up",
        "Complaint",
        "Thank You",
        "Leave Request",
        "Sales",
        "Meeting Request",
    ],
)

recipient = st.text_input("Recipient Name")
sender = st.text_input("Sender Name")
company = st.text_input("Company Name")
subject = st.text_input("Email Subject")
purpose = st.text_area("Purpose of Email")

email_length = st.selectbox(
    "Email Length",
    ["Short", "Medium", "Long"],
)

tone = st.selectbox(
    "Tone",
    ["Professional", "Friendly", "Formal"],
)

if st.button("Generate Email"):

    # Validation
    if not recipient or not sender or not subject or not purpose:
        st.error("Please fill in all required fields.")
    else:

        email = f"""
Subject: {subject}

Dear {recipient},

I hope you are doing well.

This is a {tone.lower()} {email_type.lower()} email.

Purpose:
{purpose}

Email Length:
{email_length}

Thank you for your time.

Best Regards,

{sender}
{company}
"""

        st.subheader("Generated Email")
        st.text_area("Output", email, height=250)

        # Download Button
        st.download_button(
            label="📥 Download Email",
            data=email,
            file_name="professional_email.txt",
            mime="text/plain"
        )