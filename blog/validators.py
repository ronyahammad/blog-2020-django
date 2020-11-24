from django.core.exceptions import ValidationError
def validate_file_size(value):
    filesize= value.size
    
    if filesize > 2097152:
        raise ValidationError("The maximum file size should not be more than 2MB")
    else:
        return value