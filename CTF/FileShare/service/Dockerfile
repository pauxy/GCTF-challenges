FROM ubuntu:latest
FROM python:3-onbuild
ENV user=fileshare
RUN useradd -m $user
RUN mkdir /home/$user/flag
RUN mkdir /home/$user/files
COPY ./files/* /home/$user/files/
COPY ./flag/* /home/$user/flag/
COPY ./FS.py /home/$user/FS.py
RUN chown root:$user /home/$user/FS.py
RUN chmod 440 /home/$user/FS.py
RUN chmod +x /home/$user/FS.py
RUN chown root:$user /home/$user/files
RUN chmod 440 /home/$user/files
RUN chown root:$user /home/$user/flag
RUN chmod 440 /home/$user/flag
EXPOSE 49760
CMD ["python3","/home/fileshare/FS.py"]
