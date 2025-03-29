import socket

def packet_sniffer():
    """
    captures and displays packets in hex format
    requires administrative privileges to run
    """
    try:
    # Create a raw socket to capture packets
        sniffer = socket.socket(socket.AF_INET , socket.SOCK_RAW , socket.IPPROTO_IP)

        # bind to all avcailable network interfaces
        sniffer.bind(("0.0.0.0" , 0))

        # include IP headers in captured packets
        sniffer.setsockopt(socket.IPPROTO_IP , socket.IP_HDRINCL , 1)

        print(f"Sniffer started ... press Ctrl+C to stop")

        # capture and display packets in hex format

        while True:
            raw_packet = sniffer.recvfrom(65565)[0]
            print(f"captured packet: {raw_packet.hex()}")

    except KeyboardInterrupt:
        print("\nStopping sniffer...")
        sniffer.close()

if __name__ == "__main__":
    packet_sniffer()