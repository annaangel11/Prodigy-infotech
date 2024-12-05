import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from scapy.all import sniff, IP, TCP, UDP, Raw
import sys

# Variable to control sniffing state
sniffing = False

# Function to handle packets and update the GUI
def packet_handler(packet):
    if IP in packet:  # Check if the packet has an IP layer
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Determine protocol and ports
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            protocol_color = 'lightgreen'
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            protocol_color = 'lightblue'
        else:
            protocol = "Other"
            src_port = None
            dst_port = None
            protocol_color = 'lightcoral'

        # Update the text area with packet details
        text_area.insert(tk.END, f"Protocol: ", 'protocol_label')
        text_area.insert(tk.END, f"{protocol} ", ('protocol', protocol_color))
        text_area.insert(tk.END, f"| Source: ", 'src_label')
        text_area.insert(tk.END, f"{ip_src}:{src_port} ", 'src_ip')
        text_area.insert(tk.END, f"-> Destination: ", 'dst_label')
        text_area.insert(tk.END, f"{ip_dst}:{dst_port}\n", 'dst_ip')

        # Optionally, display raw payload data
        if Raw in packet:
            payload = packet[Raw].load
            text_area.insert(tk.END, f"Payload: {payload}\n", 'payload')
        
        text_area.insert(tk.END, "-" * 50 + "\n", 'separator')

        # Scroll down to the latest packet
        text_area.see(tk.END)

# Start packet sniffing in a separate thread
def start_sniffing(interface):
    global sniffing
    sniffing = True
    sniff(iface=interface, prn=packet_handler, store=False, stop_filter=lambda x: not sniffing)

# Function to start sniffing and disable the "Start" button
def start_sniffer():
    interface = interface_entry.get()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    # Run sniffing in a separate thread
    sniffer_thread = threading.Thread(target=start_sniffing, args=(interface,), daemon=True)
    sniffer_thread.start()

# Function to stop the sniffer
def stop_sniffer():
    global sniffing
    sniffing = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Packet Sniffer")
root.configure(bg='#282c34')
root.geometry("800x600")  # Increase window size for better aspect ratio

# Interface Label and Entry
interface_label = tk.Label(root, text="Network Interface:", font=("Helvetica", 12), fg="white", bg='#282c34')
interface_label.pack(pady=5)
interface_entry = tk.Entry(root, font=("Helvetica", 12), width=15)
interface_entry.pack(pady=5)
interface_entry.insert(0, "eth0")  # Default interface

# Text area to display packets
text_area = scrolledtext.ScrolledText(root, width=100, height=25, bg='#2e3238', fg='white', font=("Consolas", 10), wrap=tk.WORD)
text_area.pack(pady=10)

# Tags for coloring different sections
text_area.tag_config('protocol_label', foreground='cyan')
text_area.tag_config('protocol', foreground='lightgreen')
text_area.tag_config('src_label', foreground='yellow')
text_area.tag_config('src_ip', foreground='lightblue')
text_area.tag_config('dst_label', foreground='orange')
text_area.tag_config('dst_ip', foreground='lightpink')
text_area.tag_config('payload', foreground='white')
text_area.tag_config('separator', foreground='gray')

# Start Button
start_button = tk.Button(root, text="Start Sniffing", command=start_sniffer, font=("Helvetica", 12), bg="green", fg="white")
start_button.pack(pady=5)

# Stop Button
stop_button = tk.Button(root, text="Stop", state=tk.DISABLED, command=stop_sniffer, font=("Helvetica", 12), bg="red", fg="white")
stop_button.pack(pady=5)

# Run the main loop
root.mainloop()

