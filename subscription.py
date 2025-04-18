# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:53:24 2025

@author: user
"""

import streamlit as st
def main():
    
    st.title("`Subscription Plans`")
    
    st.subheader("Choose Your Plan")
    
    plans = {
        "`WellnessHub Lite`": {
            "Price": "199 INR/month",
            "Features": ["24 x 7 Service", "Unlimited access"]
        },
        "`WellnessHub Pro`": {
            "Price": "499 INR/month",
            "Features": ["24 x 7 Service", "Unlimited access", "Chatbot Support"]
        },
        "`WellnessHub Ultimate`": {
            "Price": "9999 INR/year",
            "Features": ["24 x 7 Service", "Unlimited access", "Chatbot Support","First Access to new upcoming prediction models", "10 months (paid) + 2 months (free)"]
        }
    }
    
    for plan, details in plans.items():
        st.write(f"**{plan}**")
        st.write(f"Price: {details['Price']}")
        st.write("Features:")
        for feature in details["Features"]:
            st.write(f"- {feature}")
        st.write("---")