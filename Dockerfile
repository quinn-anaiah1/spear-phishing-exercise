# Use Ubuntu as base (same as SEED VM)
FROM ubuntu:20.04

LABEL maintainer="Anaiah Quinn"

# Avoid interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Update and install required packages
RUN apt update && \
    apt install -y python3 python3-pip git apache2 curl wget net-tools && \
    apt clean

# Clone Social Engineering Toolkit
RUN git clone https://github.com/trustedsec/social-engineer-toolkit.git /opt/set

# Install Python dependencies
RUN grep -v pymssql /opt/set/requirements.txt > /opt/set/clean-reqs.txt && \
    pip3 install -r /opt/set/clean-reqs.txt


# Set working directory
WORKDIR /opt/set

# Expose web server port
EXPOSE 80

# Start Apache and run SETCMD service apache2 start && python3 setoolkit
CMD service apache2 start && tail -f /dev/null
#["/bin/bash"]
