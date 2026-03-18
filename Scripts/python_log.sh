
echo "Log generation started..."

timeout 10s python3 log_generator.py
sleep 2

echo "10 seconds reached. Terminating the script."
exit 0