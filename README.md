# XML Schema Validator for Berlin Geodata

Tool for validating geodata in GML format against XML-Schemas.

This tool is a prototype for a test operation, which can be further developed if necessary. For example, further schemata can easily be stored for validation. For questions and feedback please contact odis@technologiestiftung-berlin.de.

## Background

The Berlin administration provides geodata via the FIS-Broker as Open Data. In addition to data sets that are recorded and maintained directly by an administrative office throughout Berlin, i.e. spatially covering the entire city area, there is a multitude of other geodata that are the decentralized responsibility of the districts. Some of these data show a strong schematic heterogeneity among each other and can only be merged with a high effort. For this purpose, several workshops with employees of the district survey offices were conducted and standardized data schemes and presentation requirements were created for sample data sets. These data schemes are stored in this tool. By uploading or inserting a geodata set in GML file format, it can be validated against the corresponding schema. If the validator returns errors, the geodataset must be corrected to adapt it to the required schema. 

## Deployment

To run this on your vercel account. Do the following.

1. Clone the repo to your computer
2. deploy it to vercel once `vercel` (all updates to the production are done with `vercel --prod`)
3. Setup your secret `vercel env add secret` (will prompt for your secret. Make it long and safe it somewhere)
4. Pull it into a .env file `vercel env pull`
5. Deploy again (`vercel --prod`) or run it on dev mode (`vercel dev`)
6. Hit the login endpoint with a POST request to get a token

```bash
  curl --location --request POST 'http://localhost:3000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"foo",
    "password":"bar"
}'
```

7. use the token returned to hit your main endpoint

```bash
curl --location --request POST 'http://localhost:3000' \
--header 'Authorization: 1234...'
