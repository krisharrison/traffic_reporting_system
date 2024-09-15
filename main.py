import requests
import json

response_api = requests.get("https://{baseURL}/traffic/services/{versionNumber}/incidentDetails?key={KiLGscijJLMBPhpleztf5K8JlMDAslDl}&ids={ids}&fields={fields}&language={language}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}")
