def queries_login():
    data = "SELECT user_fullname FROM appl.appl_mst_user WHERE user_username = %s AND user_password = %s"
    return data

def queries_last_open():
    data = "UPDATE APPL.APPL_MST_USER SET CUST_LAST_LOGIN = %s"
    return data