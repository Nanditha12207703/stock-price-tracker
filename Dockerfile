# Step 1: Start with an official Python image
FROM python:3.8-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container
COPY . /app

# Step 4: Install the required Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Step 5: Expose port 8501 for Streamlit to run
EXPOSE 8501

# Step 6: Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
