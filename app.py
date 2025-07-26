import streamlit as st
import re

def clean_input(text):
    """Clean and normalize input text"""
    if not text:
        return ""
    # Remove extra spaces and convert to lowercase
    return re.sub(r'\s+', ' ', text.strip().lower())

def generate_email_formats(first_name, last_name, domain):
    """Generate 4 common email formats"""
    
    # Clean inputs
    first_name = clean_input(first_name)
    last_name = clean_input(last_name) if last_name else ""
    domain = clean_input(domain)
    
    # Remove @ from domain if user included it
    domain = domain.replace('@', '')
    
    # Remove special characters from names (keep only letters and numbers)
    first_clean = re.sub(r'[^a-zA-Z0-9]', '', first_name)
    last_clean = re.sub(r'[^a-zA-Z0-9]', '', last_name) if last_name else ""
    
    formats = []
    
    if last_name:
        # Format 1: firstname.lastname@domain.com
        formats.append(f"{first_clean}.{last_clean}@{domain},")
        
        # Format 2: firstname@domain.com
        formats.append(f"{first_clean}@{domain},")
        
        # Format 3: lastname@domain.com
        formats.append(f"{last_clean}@{domain},")
        
        # Format 4: flastname@domain.com
        formats.append(f"{first_clean[0]}{last_clean}@{domain}")
    else:
        # If only first name provided
        formats.append(f"{first_clean}@{domain}")
        formats.append(f"{first_clean}.contact@{domain}")
        formats.append(f"info.{first_clean}@{domain}")
        formats.append(f"{first_clean}.admin@{domain}")
    
    return formats

def main():
    st.set_page_config(
        page_title="Email Format Generator",
        page_icon="📧",
        layout="centered"
    )
    
    st.title("Siddhant's Format Lab")
    st.markdown("Generate common email formats from a person's name and domain")
    
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input(
            "First Name*", 
            placeholder="e.g., John",
            help="Enter the person's first name"
        )
    
    with col2:
        last_name = st.text_input(
            "Last Name", 
            placeholder="e.g., Doe",
            help="Enter the person's last name (optional)"
        )
    
    domain = st.text_input(
        "Domain*", 
        placeholder="e.g., company.com or @company.com",
        help="Enter the company domain (with or without @)"
    )
    
    # Generate button
    if st.button("Generate Email Formats", type="primary"):
        if not first_name or not domain:
            st.error("Please provide at least First Name and Domain!")
        else:
            # Generate email formats
            email_formats = generate_email_formats(first_name, last_name, domain)
            
            st.success(f"Generated email formats for **{first_name.title()} {last_name.title() if last_name else ''}**:")
            
          #   # Display results
          #   for i, email in enumerate(email_formats, 1):
          #       st.code(email, language=None)
            
            # Copy all formats as text
            
            all_emails = "\n".join(email_formats)
            
            st.text_area(
                
                "All formats():", 
                value=all_emails, 
                height=120,
                help="You can copy all formats from here"
                )
        
            
            
            
    
    # Instructions
    with st.expander("How it works Let's see"):
        st.markdown("""
        1. **Enter First Name**: Required field (e.g., "siddhant")
        2. **Enter Last Name**: Optional field (e.g., "parulekar")
        3. **Enter Domain**: Required field (e.g., "company.com" or "@company.com")
        4. **Click Generate**: Get 4 common email format variations
        
        **Common formats generated:**
        - firstname.lastname@domain.com
        - firstname@domain.com
        - lastname@domain.com
        - flastname@domain.com
        
        **Note:** Special characters are automatically removed from names to ensure valid email formats.
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("Thanku For Using SidFormats")

if __name__ == "__main__":
    main()