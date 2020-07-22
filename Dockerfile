FROM python:3

RUN mkidr /app

#Getting the app file ready
COPY ./ /app

WORKDIR /app


#install the required dependencies for the app
RUN pip install -r ./requirements.txt


#Run the app
RUN python app.py
CMD ["python" ,'MainGame.py']




