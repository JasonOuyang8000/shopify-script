# Shopify Script in Python

1. Install Necessary libraries and Setup Virtual Environment
2. Libraries: Shopify-sdk for python, dotenv for keys, and maybe a JSON builder for creating and outputting the JSON File (will look more as I get basics out there.).
3. Environment has been Setup but it seems like I would need to use Requests either in REST or GraphQL instead of Shopify-sdk (Need password or Secret Key) 
4. I will give GraphQL a first try as I never worked with it before. If I can't get it working, I will use REST instead. (Will test first with POSTMAN)
5. I was able to access the endpoint but got errors with GRAPHQL endpoints. I will use REST API instead now. 
6. I was able to see all the products but I need to specifically point to the catalog collection. Found it through custom collections
7. Now, I can go back to script.py => Connect to API => Use Collection id and Products.json endpoint => Get JSON and create/write file to current folder.

## Final Thoughts
I've learn a bit about how Shopify API works but I do want to see how GRAPLQL queries would work. I was not able 
to do so for this assessment. In terms of optimization, I think I can first make a request to see all the available collections and 
then make another request to decide which products to retrieve based off the collection id.