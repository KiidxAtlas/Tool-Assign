import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tool Assign")
        self.geometry("800x600")
        self.configure(bg="white")

        # Create a frame for the main content
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Add a label to the main frame
        self.label = ctk.CTkLabel(self.main_frame, text="Welcome to Tool Assign", font=("Arial", 24))
        self.label.pack(pady=20)
        
class AssignPopup(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Assign Tool")
        self.geometry("400x300")
        self.configure(bg="white")

        # Create a frame for the popup content
        self.popup_frame = ctk.CTkFrame(self, corner_radius=10)
        self.popup_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Add a label to the popup frame
        self.label = ctk.CTkLabel(self.popup_frame, text="Assign a Tool", font=("Arial", 18))
        self.label.pack(pady=20)