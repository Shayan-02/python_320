from tkinter import *
from tkinter import messagebox, filedialog


def show_info():
    """Show a simple informational messagebox."""
    messagebox.showinfo("Information", "This is an informational message.")


def show_warning():
    """Show a warning messagebox."""
    messagebox.showwarning("Warning", "This is a warning message.")


def show_error():
    """Show an error messagebox."""
    messagebox.showerror("Error", "This is an error message.")


def ask_question():
    """Show a yes/no question box."""
    result = messagebox.askquestion("Confirmation", "Do you want to continue?")
    if result == "yes":
        messagebox.showinfo("Response", "You chose to continue.")
    else:
        messagebox.showinfo("Response", "You chose not to continue.")


def ask_ok_cancel():
    """Show an OK/Cancel dialog."""
    result = messagebox.askokcancel("OK/Cancel", "Do you want to proceed?")
    if result:
        messagebox.showinfo("Response", "You clicked OK.")
    else:
        messagebox.showinfo("Response", "You clicked Cancel.")


def open_file():
    """Open a file using the filedialog and display the selected file's path."""
    file_path = filedialog.askopenfilename(
        title="Open a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        text_widget.insert(END, f"Selected file: {file_path}\n")


def save_file():
    """Save the current content in the text widget to a file."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get("1.0", END))
        messagebox.showinfo("Save File", f"File saved as {file_path}")


# Create the main window
root = Tk()
root.title("Tkinter MessageBox and FileDialog")
root.geometry("500x400")

# Add a label
label = Label(root, text="Welcome to Tkinter messagebox & filedialog demo!", font=("Arial", 16))
label.pack(pady=10)

# Add a button to show info messagebox
info_button = Button(root, text="Show Info", command=show_info)
info_button.pack(pady=5)

# Add a button to show warning messagebox
warning_button = Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=5)

# Add a button to show error messagebox
error_button = Button(root, text="Show Error", command=show_error)
error_button.pack(pady=5)

# Add a button for yes/no confirmation
question_button = Button(root, text="Ask Question", command=ask_question)
question_button.pack(pady=5)

# Add a button for OK/Cancel dialog
ok_cancel_button = Button(root, text="Ask OK/Cancel", command=ask_ok_cancel)
ok_cancel_button.pack(pady=5)

# Add a button to open a file dialog
open_button = Button(root, text="Open File", command=open_file)
open_button.pack(pady=5)

# Add a button to save the file using file dialog
save_button = Button(root, text="Save File", command=save_file)
save_button.pack(pady=5)

# Add a text widget to display file content
text_widget = Text(root, height=10, width=50)
text_widget.pack(pady=10)

# Start the Tkinter loop
root.mainloop()
