# Python
import boto
from boto.s3.lifecycle import Lifecycle, Transition, Rule

AWS_ACCESS_KEY_ID = "XXXXXXXXXXXXXXXXXXXX"
AWS_ACCESS_KEY_SECRET = "XXxxxxxxXxXXxXXXXXXXxxxx"



conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY_SECRET)

def backup_transition(bucket_name, bucket_folder):
    # Engaging to backup transition
    S3_BUCKET = bucket_name
    bucket = conn.get_bucket(S3_BUCKET)

    ruleid = "rule_id_"+str(bucket_folder)

    to_glacier = Transition(days=0, storage_class='GLACIER')
    rule = Rule(ruleid, bucket_folder, 'Enabled', transition=to_glacier)

    lifecycle = Lifecycle()
    lifecycle.append(rule)

    # ready to backup
    # configuring the bucket with this lifecycle policy
    bucket.configure_lifecycle(lifecycle) 
    # retrieve the current lifecycle policy of the bucket.
    current = bucket.get_lifecycle_config() 
    print current[0].transition
    


def backup_restore():
    # restoring files from glacier
    if not bucket.list():
        return False

    for key in bucket.list():
        key, key.storage_class
        data = bucket.get_key(key)
        data.restore(days=0)
        data.ongoing_restore
        data.expiry_date
        
    return True


