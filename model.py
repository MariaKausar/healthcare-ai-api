def predict_risk(text):
    text = text.lower()
    
    if "cancer" in text or "tumor" in text:
        return "High Risk"
    elif "pain" in text or "fever" in text:
        return "Medium Risk"
    else:
        return "Low Risk"