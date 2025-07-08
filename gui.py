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