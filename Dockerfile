# Use Python 3.6 for URLNet
FROM python:3.6

# Set working directory inside container
WORKDIR /app

# Install required Python packages
RUN pip install --no-cache-dir \
    tensorflow==1.8.0 \
    tflearn==0.3.2 \
    numpy==1.14.5 \
    h5py==2.7.1 \
    scipy==1.0.0 \
    tqdm==4.64.1

# Copy your repository files into the container
COPY . .

# Make scripts executable
RUN chmod +x *.sh

# Default command (can be overridden when running container)
CMD ["bash"]
