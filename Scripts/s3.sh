# Set the limit
MAX_DURATION=5

while [ $SECONDS -lt $MAX_DURATION ]; do
    aws s3 cp app.log s3://log-sentinel-storage/ --region ap-south-1

    echo "Upload synced. Time elapsed: ${SECONDS}s"

    sleep 2
done

echo "5 seconds reached. Terminating script."
exit 0