def save_s3_cache(base_folder, cache_data):
    """Save cache.json to S3 bucket with date and sequence number format"""
    try:
        # Get current date in MMDD format
        current_date = datetime.now().strftime("%m%d")
        
        # List existing caches for the same date
        cache_prefix = f"{base_folder}/cache/cache_{current_date}_"
        response = s3_client.list_objects_v2(
            Bucket=BUCKET_NAME,
            Prefix=cache_prefix
        )
        
        # Find the next available number
        existing_numbers = []
        if 'Contents' in response:
            for obj in response['Contents']:
                key = obj['Key']
                if key.endswith('.json'):
                    try:
                        num = int(key.split('_')[-1].split('.')[0])
                        existing_numbers.append(num)
                    except ValueError:
                        continue
        
        next_number = max(existing_numbers) + 1 if existing_numbers else 1
        
        # Construct the new cache path
        cache_path = f"{base_folder}/cache/cache_{current_date}_{next_number}.json"
        
        # Convert data to JSON string
        cache_content = json.dumps(cache_data, indent=4)
        
        # Upload to S3
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=cache_path,
            Body=cache_content.encode('utf-8'),
            ContentType='application/json'
        )
        logger.info(f"Successfully saved cache to S3: {cache_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to save cache to S3: {str(e)}")
        return False
`
