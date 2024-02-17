#dockerfile
FROM python
COPY . ./
CMD ["python3","calculator.py"]
