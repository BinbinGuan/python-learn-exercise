# def div(a, b):
# try:
#     print(a / b)
# except ZeroDivisionError:
#     print("Error: b should not be 0 !!")
# except Exception as e:
#     print("Unexpected Error: {}".format(e))
# else:
#     print('Run into else only when everything goes well')
# finally:
#     print('Always run into finally block.')


# tests
# div(2, 0)
# div(2, 'bad type')
# div(1, 2)

# Mutiple exception in one line
def div(a, b):
    try:
        print(a / b)
    except (ZeroDivisionError, TypeError) as e:
        print(e)

# Except block is optional when there is finally
# try:
#     open(database)
# finally:
#     close(database)

# # catch all errors and log it
# try:
#     def(1,0);
# except:
#     # get detail from logging module
#     logging.exception('Exception caught!')
#
#     # get detail from sys.exc_info() method
#     error_type, error_value, trace_back = sys.exc_info()
#     print(error_value)
#     raise
#
#
# name = getattr(test, 'name', 'default')
