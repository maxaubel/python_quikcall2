# Motorola QuikCall II Python

Some tinkering to detect QuikCall II tones send via radio. I use a RTL-SDR receiver hooked to GQRX and send the audio via a virtual interface to `detect_tones.py`. I wrote some A/B QuikCall II tones in a dictionary, with their corresponding frequencies. You might want to set these according to your needs. 