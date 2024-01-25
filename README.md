# example-ssr-csr
This FastAPI application, named "Token," is designed to generate authentication tokens using a simple and secure approach. The application supports both Server-Side Rendering (SSR) and Client-Side Rendering (CSR) for token generation. Additionally, it provides an endpoint for obtaining access tokens through a POST request.

## Features
**SSR Token Generation:** Access the /ssr endpoint to generate a token using Server-Side Rendering. The generated token is based on a predefined username and is showcased in the provided HTML template.

**CSR Token Generation:** Access the /csr endpoint to render a Client-Side Rendering template. This template can be customized based on your specific requirements.

**Access Token Retrieval:** Utilize the /token endpoint with a POST request to obtain an access token. This requires providing a valid username and password. The application uses a simple authentication mechanism with fake user credentials stored in the configuration.
 
To run it, follow the steps below:

1. Place in directory **./src**:
```sh
cd src
```

2. Install additional libraries:
```sh
pip install -r requirements.txt
```

3. Run the application:
```sh
python manager.py
```