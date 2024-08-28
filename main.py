import os
import time
import logging
from secret import get_secret_by_name


logging.basicConfig(level=logging.INFO)


def certificates(country, state, locality, organization, cert_name, key_name, days, common_name, target_folder = None):
    """
    Common name is the domain name. 
    The certificates will only work for the domain name specified in the common name.
    """
    if target_folder:
        cert_name = f"{target_folder}/{cert_name}"
        key_name = f"{target_folder}/{key_name}"
    
    command = f'openssl req -newkey rsa:2048 -sha256 -nodes -x509 -days {days} -keyout {key_name}.key -out {cert_name}.crt -subj "/C={country}/ST={state}/L={locality}/O={organization}/CN={common_name}"'        
    additional_command = f"openssl x509 -in {cert_name}.crt -out {cert_name}.pem -outform PEM"
    os.system(command)
    os.system(additional_command)

def get_certificates(env_file=False, days="365"):
    cert_name = get_secret_by_name("CERT_NAME", env_file=env_file)
    key_name = get_secret_by_name("KEY_NAME", env_file=env_file)
    target_folder = get_secret_by_name("TARGET_FOLDER", env_file=env_file)
    common_name = get_secret_by_name("CERT_COMMON_NAME", "", env_file=env_file)
    country = get_secret_by_name("CERT_COUNTRY", env_file=env_file)
    state = get_secret_by_name("CERT_STATE", env_file=env_file)
    locality = get_secret_by_name("CERT_LOCALITY", env_file=env_file)
    organization = get_secret_by_name("CERT_ORGANIZATION", env_file=env_file)
    return certificates(country, state, locality, organization, cert_name, key_name, days, common_name, target_folder)


def refresher(env_file=False, days="365"):
    while True:
        result = get_certificates(env_file, days)
        if not result:
            logging.info("Certificates have been updated.")
        else:
            logging.error("Certificates could not be updated.")
        eep = int(days) * 24 * 3600
        time.sleep(eep)


if __name__ == "__main__":
    # Test it out here: 
    env_file = True
    # Docker container:
    env_file = False

    refresher(env_file)
