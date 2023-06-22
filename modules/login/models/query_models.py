def queries_login():
    data = "SELECT CUST_USERNAME, CUST_PASSWORD FROM APPL.APPL_MST_USER WHERE CUST_USERNAME = %s AND CUST_PASSWORD = %s"
    return data

def queries_last_open():
    data = "UPDATE APPL.APPL_MST_USER SET CUST_LAST_LOGIN = %s"
    return data