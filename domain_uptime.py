import yaml
import argparse
import requests
import time
import re


# in the form base-url:[amount_up,total_requests]
request_results = {}



#--------------------------------------
# Sends the request and calculates latency
# -------------------------------------  
def send_request(request_elements):
    url = request_elements.get("url")
    method = request_elements.get("method", "GET").upper()
    header = request_elements.get("headers", {})
    body = request_elements.get("body", None)

    start = time.time()
    if method == "GET":
        response = requests.get(url, headers=header)
    else:
        response = requests.post(url, headers=header,data=body)
    end = time.time()
    latency = (end-start)*1000
    return response.status_code, latency
   
#--------------------------------------
# Checks if the response is UP or DOWN and adds to tally
# -------------------------------------      
def validate(url,code,latency):
    pattern = r'([a-zA-Z0-9-]+\.[a-zA-Z]{2,})'
    match = re.search(pattern, url)
    url = match.group(1)
    request_results.setdefault(url, [0, 0])
    if 200<= code <=299 and latency<500:
        # add 1 to UPs 
        request_results[url][0]+=1 
    request_results[url][1]+=1 # total +=1
   
           
        
    
#--------------------------------------
# Print out the output to the CMD line
# -------------------------------------   
def create_output():
    for k,v in request_results.items():
        perc = round(100*(v[0]/v[1])) # Percentage is Ups/total * 100
        print(f"{k} has {perc} availibilty percentage")

#--------------------------------------
# Convert Yaml to dict
# ------------------------------------- 
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)



#--------------------------------------
# Process YAML, send requests, print output
# -------------------------------------  
def main():   
    parser = argparse.ArgumentParser()
    parser.add_argument("yaml_path", type=str,help="Path to yaml")
    args = parser.parse_args()
    try:
        endpoints = load_yaml(args.yaml_path)
    except:
        print("File not present or yaml constructed wrong")
        return
    last_time = 0
    while True:
        # Every 15 seconds:
        curr_time = time.time()
        if curr_time-last_time>15:
            for k in endpoints:
                curr_url = k['url']
                code, latency = send_request(k)
                validate(curr_url,code,latency)
            create_output()
            print(request_results)
            print("-------------------------------------------")
            last_time = curr_time
        
    

if __name__=="__main__":
    main()


# Process Urls
# iterate through URLs
    # Every 15 secs:
    #   Send req. get the info and print it
    