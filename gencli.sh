docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://api.swaggerhub.com/apis/hcadavid6/slurm-rest_api_ro/0.0.38 \
    -g python \
    -o /local
