from django.utils.timezone import localtime

def get_duration(employee):
    if employee.leaved_at is None: 
        total_seconds = (localtime() - localtime(employee.entered_at)).total_seconds()
    else:
        total_seconds = (employee.leaved_at - employee.entered_at).total_seconds()
    return total_seconds

def format_time(total_seconds):
    hours = int(round(total_seconds // 3600))
    minutes = int(round(total_seconds % 3600 // 60))
    seconds = round(total_seconds - hours * 3600 - minutes * 60)
    return f'{hours}:{minutes}:{seconds}'