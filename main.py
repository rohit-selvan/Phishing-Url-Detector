import tkinter as tk
from tkinter import messagebox
import re

class PhishingURLDetector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Phishing URL Detector")
        self.geometry("600x400")
        self.configure(bg="#e8f4f8")  
        self.create_widgets()

    def create_widgets(self):
    
        tk.Label(self, text="Phishing URL Detector", font=("Verdana", 24, "bold"), bg="#e8f4f8", fg="#2c3e50").pack(pady=20)
        
        
        tk.Label(self, text="Enter a URL to analyze:", font=("Verdana", 12), bg="#e8f4f8").pack(pady=5)
        self.url_entry = tk.Entry(self, font=("Verdana", 12), width=50)
        self.url_entry.pack(pady=10)
        
    
        tk.Button(self, text="Analyze", command=self.analyze_url, font=("Verdana", 14), bg="#3498db", fg="white", width=15).pack(pady=10)
        
       
        self.result_label = tk.Label(self, text="", font=("Verdana", 14), bg="#e8f4f8", wraplength=500)
        self.result_label.pack(pady=20)

    def analyze_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return
        
        result = self.check_phishing(url)
        if result:
            self.result_label.config(text=f"⚠️ The URL '{url}' is potentially a phishing link!", fg="red")
        else:
            self.result_label.config(text=f"✅ The URL '{url}' appears safe.", fg="green")
    
    def check_phishing(self, url):
      
        phishing_patterns = [
            r"http://",              
            r"[-_]{2,}",             
            r"[0-9]{5,}",            
            r"free|win|bonus|offer", 
            r"\.tk|\.ml|\.ga|\.cf"    
        ]
        
        for pattern in phishing_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                return True
        
        
        if len(url) > 75:
            return True
        
        return False

if __name__ == "__main__":
    app = PhishingURLDetector()
    app.mainloop()
