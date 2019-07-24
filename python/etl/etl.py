def transform(legacy):
    return {value.lower() : key for key, values in legacy.items() for value in values}